#!/usr/bin/env python3
"""Deterministic release checks for the public HiveForge package."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "10_CUSTOM_AGENTS" / "UNPS_HiveForge"
VERSION = "0.5.0"

REQUIRED_PACKAGE_FILES = [
    "README.md",
    "BRAIN.md",
    "AGENT.md",
    "SYSTEM_INSTRUCTIONS.md",
    "PACKAGE_MANIFEST.md",
    "SKILLS.md",
    "WORKFLOWS.md",
    "MCP_PREFERENCES.md",
    "DEPENDENCIES.md",
    "OUTPUT_SCHEMAS.md",
    "TOOL_POLICY.md",
    "INSTALL.md",
    "CHANGELOG.md",
]

REQUIRED_SUPPORT_FILES = [
    "LICENSE",
    "DRIVE_SYNC_MANIFEST.md",
    "06_DEPENDENCIES/DEPENDENCY_STATUS_MANIFEST.md",
    "06_DEPENDENCIES/External_Services/Agent_Orchestration/COMPOSIO_STAGING.md",
    "06_DEPENDENCIES/External_Services/Agent_Orchestration/LANGGRAPH_STAGING.md",
    "06_DEPENDENCIES/Python/CLI_Tools/Media_Ingestion/MEDIA_INGESTION_TOOLING.md",
    "05_WORKFLOWS/Agent_Control_Plane/TOOLJET_AGENT_CAPABILITY_REGISTRY.md",
    "09_TESTS_EVALS/Prompt_Tests/PRODUCTION_ACCEPTANCE_MATRIX_v0.5.0.md",
]

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub personal token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".sh", ".json", ".yaml", ".yml", ".toml", ".html", ".css", ".js", ".svg"
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: pathlib.Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"empty required file: {path.relative_to(ROOT)}")
    return text


def check_package_files() -> None:
    for name in REQUIRED_PACKAGE_FILES:
        read(PACKAGE / name)
    for name in REQUIRED_SUPPORT_FILES:
        read(ROOT / name)
    print("PASS: required package/support files")


def check_versions() -> None:
    checks = {
        PACKAGE / "AGENT.md": f"version: {VERSION}",
        PACKAGE / "PACKAGE_MANIFEST.md": f"version: {VERSION}",
        PACKAGE / "README.md": f"**Version:** {VERSION}",
        PACKAGE / "DEPENDENCIES.md": f"Version: {VERSION}",
        PACKAGE / "INSTALL.md": f"Version: {VERSION}",
        PACKAGE / "CHANGELOG.md": f"## {VERSION} —",
        PACKAGE / "BRAIN.md": f"Version: {VERSION}",
        ROOT / "README.md": f"version-{VERSION}",
    }
    for path, needle in checks.items():
        if needle not in read(path):
            fail(f"version mismatch: {path.relative_to(ROOT)} missing {needle!r}")
    print(f"PASS: release metadata synchronized at {VERSION}")


def check_production_status() -> None:
    checks = {
        PACKAGE / "AGENT.md": "status: production",
        PACKAGE / "PACKAGE_MANIFEST.md": "status: production",
        PACKAGE / "BRAIN.md": "Status: Production",
        PACKAGE / "README.md": "**Status:** Production",
        PACKAGE / "DEPENDENCIES.md": "Status: Production",
        PACKAGE / "INSTALL.md": "Status: Production",
        PACKAGE / "CHANGELOG.md": "### Status\n\nProduction.",
        ROOT / "README.md": "status-production",
    }
    for path, needle in checks.items():
        if needle not in read(path):
            fail(f"production status mismatch: {path.relative_to(ROOT)} missing {needle!r}")
    root_readme = read(ROOT / "README.md")
    if "**Current maturity:** Production" not in root_readme:
        fail("root README is not marked Production")
    print("PASS: production status synchronized")


def iter_text_files():
    excluded_parts = {".git", "dist", "graphify-out", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in excluded_parts for part in path.parts):
            continue
        yield path


def check_temp_artifacts() -> None:
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        upper = path.name.upper()
        if "_TEMP" in upper or upper.startswith("TEMP_") or upper.endswith(".TEMP"):
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        fail("temporary artifacts present: " + ", ".join(offenders))
    print("PASS: no TEMP release artifacts")


def check_secrets() -> None:
    findings = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)} ({label})")
    if findings:
        fail("secret-like material detected: " + ", ".join(findings))
    print("PASS: secret/private-key scan")


def check_public_boundary() -> None:
    prohibited_paths = [
        "clients",
        "client_data",
        "opportunities",
        "correspondence",
        "medical_records",
        "financial_records",
        "credentials",
        "secrets",
    ]
    offenders = []
    for path in ROOT.rglob("*"):
        relative_parts = {part.lower() for part in path.relative_to(ROOT).parts}
        if any(name in relative_parts for name in prohibited_paths):
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        fail("private-scope path detected in public mirror: " + ", ".join(offenders[:20]))
    print("PASS: public/private path boundary")


def check_acceptance_evidence() -> None:
    path = ROOT / "09_TESTS_EVALS" / "Prompt_Tests" / "PRODUCTION_ACCEPTANCE_MATRIX_v0.5.0.md"
    text = read(path)
    if "Critical scenarios: **11/11 PASS**" not in text:
        fail("production acceptance evidence is incomplete")
    for workflow in ("Workflow A", "Workflow B", "Workflow C"):
        if workflow not in text:
            fail(f"missing acceptance workflow: {workflow}")
    print("PASS: three-workflow acceptance evidence")


def check_optional_fallback_contract() -> None:
    brain = read(PACKAGE / "BRAIN.md")
    deps = read(PACKAGE / "DEPENDENCIES.md")
    if "If Graphify is unavailable" not in brain:
        fail("BRAIN missing Graphify fallback contract")
    if "graphifyy==0.9.48" not in deps or "CANDIDATE" not in deps:
        fail("dependency policy does not keep Graphify optional/candidate")
    print("PASS: optional dependency fallback contract")


def main() -> int:
    check_package_files()
    check_versions()
    check_production_status()
    check_temp_artifacts()
    check_secrets()
    check_public_boundary()
    check_acceptance_evidence()
    check_optional_fallback_contract()
    print("HiveForge production gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
