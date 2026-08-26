#!/usr/bin/env python3
"""Deterministic production checks for the public HiveForge package."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "10_CUSTOM_AGENTS" / "UNPS_HiveForge"
VERSION = "0.7.0"

REQUIRED_PACKAGE_FILES = [
    "README.md", "BRAIN.md", "AGENT.md", "SYSTEM_INSTRUCTIONS.md",
    "PACKAGE_MANIFEST.md", "SKILLS.md", "WORKFLOWS.md", "MCP_PREFERENCES.md",
    "DEPENDENCIES.md", "OUTPUT_SCHEMAS.md", "TOOL_POLICY.md", "INSTALL.md", "CHANGELOG.md",
]

REQUIRED_SUPPORT_FILES = [
    "LICENSE",
    "DRIVE_SYNC_MANIFEST.md",
    "06_DEPENDENCIES/DEPENDENCY_STATUS_MANIFEST.md",
    "06_DEPENDENCIES/External_Services/Agent_Orchestration/COMPOSIO_STAGING.md",
    "06_DEPENDENCIES/External_Services/Agent_Orchestration/LANGGRAPH_STAGING.md",
    "06_DEPENDENCIES/Python/CLI_Tools/Media_Ingestion/MEDIA_INGESTION_TOOLING.md",
    "05_WORKFLOWS/Agent_Control_Plane/TOOLJET_AGENT_CAPABILITY_REGISTRY.md",
    "09_TESTS_EVALS/Prompt_Tests/PRODUCTION_ACCEPTANCE_MATRIX_v0.7.0.md",
    "docs/GETTING_STARTED.md",
    "docs/USER_INTAKE.md",
    "docs/WORKFLOW_GUIDE.md",
    "docs/COMMAND_REFERENCE.md",
    "docs/TOOLING_GUIDE.md",
    "docs/TOOLJET_SETUP.md",
    "docs/TROUBLESHOOTING.md",
    "docs/README.md",
    "docs/RELEASE_NOTES_v0.7.0.md",
    "examples/FIRST_RUN_PROMPT.md",
    "examples/USER_PROFILE_TEMPLATE.md",
    "examples/PROJECT_INTAKE_TEMPLATE.md",
    "tooljet/docker-compose.yml",
    "tests/onboarding_cli_smoke.sh",
]

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}

TEXT_SUFFIXES = {".md", ".txt", ".py", ".sh", ".json", ".yaml", ".yml", ".toml", ".html", ".css", ".js", ".svg"}


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


def check_files() -> None:
    for name in REQUIRED_PACKAGE_FILES:
        read(PACKAGE / name)
    for name in REQUIRED_SUPPORT_FILES:
        read(ROOT / name)
    print("PASS: required package/support/onboarding files")


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
        ROOT / "install.sh": "v0.7.0",
        ROOT / "dashboard" / "server.py": '"version": "0.7.0"',
        ROOT / "dashboard" / "static" / "index.html": "HiveForge v0.7.0",
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
    print("PASS: production status synchronized")


def check_onboarding_surface() -> None:
    root_readme = read(ROOT / "README.md")
    package_readme = read(PACKAGE / "README.md")
    launcher = read(ROOT / "bin" / "hiveforge")
    for link in (
        "docs/GETTING_STARTED.md", "docs/USER_INTAKE.md", "docs/WORKFLOW_GUIDE.md",
        "docs/COMMAND_REFERENCE.md", "docs/TOOLING_GUIDE.md", "docs/TOOLJET_SETUP.md",
        "examples/FIRST_RUN_PROMPT.md",
    ):
        if link not in root_readme:
            fail(f"root README missing onboarding link: {link}")
    if "docs/GETTING_STARTED.md" not in package_readme:
        fail("package README does not route users to Getting Started")
    for command in ("onboard", "docs", "profile-init", "project-init", "tooljet"):
        if command not in launcher:
            fail(f"launcher missing guided command: {command}")
    intake = read(ROOT / "docs" / "USER_INTAKE.md").lower()
    for prohibited in ("password", "api key", "token"):
        if prohibited not in intake:
            fail(f"user intake guide missing sensitive-data boundary: {prohibited}")
    print("PASS: guided onboarding surface")


def iter_text_files():
    excluded = {".git", "dist", "graphify-out", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in excluded for part in path.parts):
            continue
        yield path


def check_temp_artifacts() -> None:
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.upper()
        if name.startswith("TEMP_") or name.endswith("_TEMP") or name.endswith(".TEMP"):
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
    prohibited = {"clients", "client_data", "opportunities", "correspondence", "medical_records", "financial_records", "credentials", "secrets"}
    offenders = []
    for path in ROOT.rglob("*"):
        parts = {part.lower() for part in path.relative_to(ROOT).parts}
        if parts & prohibited:
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        fail("private-scope path detected in public mirror: " + ", ".join(offenders[:20]))
    print("PASS: public/private path boundary")


def check_acceptance() -> None:
    text = read(ROOT / "09_TESTS_EVALS" / "Prompt_Tests" / "PRODUCTION_ACCEPTANCE_MATRIX_v0.7.0.md")
    if "Critical scenarios: **PASS**" not in text:
        fail("v0.7.0 production acceptance evidence is incomplete")
    for phrase in ("Guided onboarding", "Experienced operator", "Project routing", "Fallback"):
        if phrase not in text:
            fail(f"acceptance matrix missing coverage: {phrase}")
    print("PASS: v0.7.0 acceptance evidence")


def check_optional_fallback() -> None:
    brain = read(PACKAGE / "BRAIN.md")
    deps = read(PACKAGE / "DEPENDENCIES.md")
    if "If Graphify is unavailable" not in brain:
        fail("BRAIN missing Graphify fallback contract")
    if "graphifyy==0.9.48" not in deps or "CANDIDATE" not in deps:
        fail("dependency policy does not keep Graphify optional/candidate")
    if "ToolJet" not in deps or "STAGED" not in deps:
        fail("dependency policy does not keep ToolJet staged")
    print("PASS: optional dependency maturity/fallback contract")


def main() -> int:
    check_files()
    check_versions()
    check_production_status()
    check_onboarding_surface()
    check_temp_artifacts()
    check_secrets()
    check_public_boundary()
    check_acceptance()
    check_optional_fallback()
    print("HiveForge production gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
