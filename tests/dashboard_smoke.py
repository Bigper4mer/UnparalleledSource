#!/usr/bin/env python3
"""Start the local Command Center and verify its health endpoint."""

from __future__ import annotations

import json
import pathlib
import socket
import subprocess
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SERVER = ROOT / "dashboard" / "server.py"


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def main() -> int:
    port = free_port()
    process = subprocess.Popen(
        [sys.executable, str(SERVER), "--no-open", "--port", str(port)],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        url = f"http://127.0.0.1:{port}/api/health"
        last_error: Exception | None = None
        for _ in range(40):
            if process.poll() is not None:
                stdout, stderr = process.communicate(timeout=1)
                raise RuntimeError(f"dashboard exited early\nstdout={stdout}\nstderr={stderr}")
            try:
                with urllib.request.urlopen(url, timeout=1) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                if payload.get("status") != "ok" or payload.get("version") != "0.5.0":
                    raise RuntimeError(f"unexpected health payload: {payload}")
                print("HiveForge dashboard smoke test: PASS")
                return 0
            except Exception as error:  # noqa: BLE001
                last_error = error
                time.sleep(0.25)
        raise RuntimeError(f"dashboard health endpoint never became ready: {last_error}")
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
