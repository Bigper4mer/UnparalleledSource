#!/usr/bin/env python3
"""Local-only HiveForge Command Center web server."""

from __future__ import annotations

import argparse
import json
import mimetypes
import pathlib
import secrets
import sys
import threading
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import runtime  # noqa: E402


DASHBOARD_ROOT = pathlib.Path(__file__).resolve().parent
INSTALL_ROOT = DASHBOARD_ROOT.parent
STATIC_ROOT = DASHBOARD_ROOT / "static"
ASSET_ROOT = INSTALL_ROOT / "assets"


def safe_file(root: pathlib.Path, relative: str) -> pathlib.Path | None:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


class DashboardHandler(BaseHTTPRequestHandler):
    server_version = "HiveForge/0.6"

    def send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path: pathlib.Path) -> None:
        body = path.read_bytes()
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; style-src 'self'; "
            "script-src 'self'; connect-src 'self'; object-src 'none'; frame-ancestors 'none'",
        )
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/api/state":
            state = runtime.read_state()
            state["session_token"] = self.server.session_token
            self.send_json(state)
            return
        if path == "/api/health":
            self.send_json({"status": "ok", "version": "0.6.0"})
            return
        if path in {"/", "/index.html"}:
            target = STATIC_ROOT / "index.html"
        elif path.startswith("/static/"):
            target = safe_file(STATIC_ROOT, path.removeprefix("/static/"))
        elif path.startswith("/assets/"):
            target = safe_file(ASSET_ROOT, path.removeprefix("/assets/"))
        else:
            target = None
        if target is None or not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        self.send_file(target)

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if self.headers.get("X-HiveForge-Token") != self.server.session_token:
            self.send_json({"error": "Invalid session token"}, HTTPStatus.FORBIDDEN)
            return
        if not path.startswith("/api/approvals/"):
            self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return
        try:
            length = min(int(self.headers.get("Content-Length", "0")), 4096)
            payload = json.loads(self.rfile.read(length) or b"{}")
            approval_id = path.rsplit("/", 1)[-1]
            runtime.decide_approval(approval_id, payload.get("decision", ""))
            self.send_json({"success": True})
        except (ValueError, json.JSONDecodeError) as error:
            self.send_json({"error": str(error)}, HTTPStatus.BAD_REQUEST)

    def log_message(self, format_string: str, *args) -> None:
        if getattr(self.server, "verbose", False):
            super().log_message(format_string, *args)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the HiveForge Command Center")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8744, type=int)
    parser.add_argument("--no-open", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        print("HiveForge dashboard binds to localhost only.", file=sys.stderr)
        return 2
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    server.session_token = secrets.token_urlsafe(24)
    server.verbose = args.verbose
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"HiveForge Command Center: {url}")
    print("Press Ctrl+C to stop.")
    if not args.no_open:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
