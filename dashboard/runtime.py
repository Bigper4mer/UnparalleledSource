#!/usr/bin/env python3
"""Dependency-free HiveForge run telemetry and local state store."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import json
import os
import pathlib
import subprocess
import sys
import time
import uuid

try:
    import fcntl
except ImportError:  # pragma: no cover - POSIX installer targets provide fcntl.
    fcntl = None


SCHEMA_VERSION = 1
MAX_RUNS = 50
MAX_EVENTS_PER_RUN = 100
VALID_RUN_STATUSES = {
    "idle",
    "running",
    "waiting_approval",
    "completed",
    "failed",
    "offline",
}
VALID_CONNECTOR_STATUSES = {"connected", "degraded", "offline", "unknown"}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def state_directory() -> pathlib.Path:
    configured = os.environ.get("HIVEFORGE_STATE_DIR")
    if configured:
        return pathlib.Path(configured).expanduser()
    xdg_state = os.environ.get("XDG_STATE_HOME")
    if xdg_state:
        return pathlib.Path(xdg_state).expanduser() / "unps-hiveforge"
    return pathlib.Path.home() / ".local" / "state" / "unps-hiveforge"


def state_path() -> pathlib.Path:
    return state_directory() / "state.json"


def default_state() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "updated_at": utc_now(),
        "active_run_id": None,
        "runs": [],
        "approvals": [],
        "connectors": [
            {"name": "Google Drive", "status": "unknown", "checked_at": None},
            {"name": "GitHub", "status": "unknown", "checked_at": None},
        ],
    }


@contextlib.contextmanager
def locked_state():
    directory = state_directory()
    directory.mkdir(parents=True, exist_ok=True)
    lock_path = directory / "state.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_file:
        if fcntl:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        path = state_path()
        try:
            state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else default_state()
        except (json.JSONDecodeError, OSError):
            state = default_state()
        yield state
        state["updated_at"] = utc_now()
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, path)
        if fcntl:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def read_state() -> dict:
    with locked_state() as state:
        return json.loads(json.dumps(state))


def find_run(state: dict, run_id: str) -> dict:
    for run in state["runs"]:
        if run["id"] == run_id:
            return run
    raise ValueError(f"Unknown run: {run_id}")


def add_event(run: dict, event_type: str, phase: str, summary: str) -> None:
    event = {
        "id": uuid.uuid4().hex[:12],
        "type": event_type,
        "phase": phase,
        "summary": summary,
        "created_at": utc_now(),
    }
    run.setdefault("events", []).append(event)
    run["events"] = run["events"][-MAX_EVENTS_PER_RUN:]
    run["phase"] = phase
    run["last_heartbeat_at"] = event["created_at"]


def start_run(task: str, phase: str = "Starting") -> str:
    run_id = uuid.uuid4().hex[:12]
    now = utc_now()
    run = {
        "id": run_id,
        "task": task.strip() or "HiveForge task",
        "status": "running",
        "phase": phase,
        "started_at": now,
        "last_heartbeat_at": now,
        "finished_at": None,
        "duration_seconds": None,
        "summary": None,
        "events": [],
    }
    add_event(run, "run_started", phase, "Run started")
    with locked_state() as state:
        state["runs"].insert(0, run)
        state["runs"] = state["runs"][:MAX_RUNS]
        state["active_run_id"] = run_id
    return run_id


def emit_event(run_id: str, phase: str, summary: str, event_type: str = "progress") -> None:
    with locked_state() as state:
        run = find_run(state, run_id)
        if run["status"] not in {"running", "waiting_approval"}:
            raise ValueError(f"Run {run_id} is already {run['status']}")
        add_event(run, event_type, phase, summary)


def finish_run(run_id: str, status: str, summary: str) -> None:
    if status not in {"completed", "failed"}:
        raise ValueError("Finish status must be completed or failed")
    now = dt.datetime.now(dt.timezone.utc)
    with locked_state() as state:
        run = find_run(state, run_id)
        started = dt.datetime.fromisoformat(run["started_at"])
        run["status"] = status
        run["finished_at"] = now.isoformat(timespec="seconds")
        run["duration_seconds"] = max(0, int((now - started).total_seconds()))
        run["summary"] = summary
        add_event(run, f"run_{status}", status.title(), summary)
        if state.get("active_run_id") == run_id:
            state["active_run_id"] = None


def set_connector(name: str, status: str) -> None:
    normalized = status.lower()
    if normalized not in VALID_CONNECTOR_STATUSES:
        raise ValueError(f"Connector status must be one of: {', '.join(sorted(VALID_CONNECTOR_STATUSES))}")
    with locked_state() as state:
        connector = next((item for item in state["connectors"] if item["name"].lower() == name.lower()), None)
        if connector is None:
            connector = {"name": name, "status": normalized, "checked_at": utc_now()}
            state["connectors"].append(connector)
        else:
            connector.update(status=normalized, checked_at=utc_now())


def request_approval(run_id: str, title: str, details: str) -> str:
    approval_id = uuid.uuid4().hex[:12]
    with locked_state() as state:
        run = find_run(state, run_id)
        run["status"] = "waiting_approval"
        add_event(run, "approval_requested", "Waiting approval", title)
        state["approvals"].insert(
            0,
            {
                "id": approval_id,
                "run_id": run_id,
                "title": title,
                "details": details,
                "status": "pending",
                "created_at": utc_now(),
                "decided_at": None,
            },
        )
    return approval_id


def decide_approval(approval_id: str, decision: str) -> None:
    if decision not in {"approve", "deny"}:
        raise ValueError("Decision must be approve or deny")
    with locked_state() as state:
        approval = next((item for item in state["approvals"] if item["id"] == approval_id), None)
        if approval is None:
            raise ValueError(f"Unknown approval: {approval_id}")
        if approval["status"] != "pending":
            raise ValueError(f"Approval {approval_id} is already {approval['status']}")
        approval["status"] = "approved" if decision == "approve" else "denied"
        approval["decided_at"] = utc_now()
        run = find_run(state, approval["run_id"])
        if decision == "approve":
            run["status"] = "running"
            add_event(run, "approval_granted", "Resuming", approval["title"])
            state["active_run_id"] = run["id"]
        else:
            run["status"] = "failed"
            run["finished_at"] = utc_now()
            run["summary"] = f"Denied: {approval['title']}"
            add_event(run, "approval_denied", "Stopped", run["summary"])
            if state.get("active_run_id") == run["id"]:
                state["active_run_id"] = None


def run_command(task: str, command: list[str]) -> int:
    if not command:
        raise ValueError("A command is required after --")
    run_id = start_run(task, "Launching")
    print(f"HiveForge run: {run_id}", file=sys.stderr)
    emit_event(run_id, "Executing", "Command is running")
    process = subprocess.Popen(command)
    try:
        while process.poll() is None:
            time.sleep(2)
            emit_event(run_id, "Executing", "Heartbeat", "heartbeat")
        exit_code = process.returncode
    except KeyboardInterrupt:
        process.terminate()
        finish_run(run_id, "failed", "Interrupted by operator")
        return 130
    finish_run(
        run_id,
        "completed" if exit_code == 0 else "failed",
        "Command completed" if exit_code == 0 else f"Command exited with code {exit_code}",
    )
    return exit_code


def format_status(state: dict) -> str:
    active_id = state.get("active_run_id")
    if active_id:
        run = find_run(state, active_id)
        return f"{run['status'].upper()}  {run['task']}  ·  {run['phase']}  ·  {run['id']}"
    latest = state["runs"][0] if state["runs"] else None
    if latest:
        return f"IDLE  Latest: {latest['status'].upper()} — {latest['task']}"
    return "OFFLINE  No HiveForge runs recorded yet."


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="HiveForge runtime telemetry")
    sub = parser.add_subparsers(dest="command", required=True)
    start = sub.add_parser("start")
    start.add_argument("task")
    start.add_argument("--phase", default="Starting")
    event = sub.add_parser("event")
    event.add_argument("run_id")
    event.add_argument("phase")
    event.add_argument("summary")
    event.add_argument("--type", default="progress")
    finish = sub.add_parser("finish")
    finish.add_argument("run_id")
    finish.add_argument("status", choices=["completed", "failed"])
    finish.add_argument("summary")
    connector = sub.add_parser("connector")
    connector.add_argument("name")
    connector.add_argument("status", choices=sorted(VALID_CONNECTOR_STATUSES))
    approval = sub.add_parser("approval")
    approval.add_argument("run_id")
    approval.add_argument("title")
    approval.add_argument("details", nargs="?", default="")
    decide = sub.add_parser("decide")
    decide.add_argument("approval_id")
    decide.add_argument("decision", choices=["approve", "deny"])
    status = sub.add_parser("status")
    status.add_argument("--json", action="store_true")
    run = sub.add_parser("run")
    run.add_argument("--task", default="HiveForge command")
    run.add_argument("command_args", nargs=argparse.REMAINDER)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "start":
            print(start_run(args.task, args.phase))
        elif args.command == "event":
            emit_event(args.run_id, args.phase, args.summary, args.type)
        elif args.command == "finish":
            finish_run(args.run_id, args.status, args.summary)
        elif args.command == "connector":
            set_connector(args.name, args.status)
        elif args.command == "approval":
            print(request_approval(args.run_id, args.title, args.details))
        elif args.command == "decide":
            decide_approval(args.approval_id, args.decision)
        elif args.command == "status":
            state = read_state()
            print(json.dumps(state, indent=2) if args.json else format_status(state))
        elif args.command == "run":
            command = args.command_args[1:] if args.command_args[:1] == ["--"] else args.command_args
            return run_command(args.task, command)
        return 0
    except (OSError, ValueError) as error:
        print(f"HiveForge: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
