# UNPS HiveForge — Drive to GitHub Sync Manifest

Version: 1.1.0  
Updated: 2026-08-24  
GitHub repository: `Bigper4mer/UnparalleledSource`  
Canonical internal source: `PROMPTS.UNPS`  
Published public release: `v0.5.0`

## Purpose

Record the public-safe subset of the canonical Drive library mirrored into GitHub. Drive remains the internal source of truth; GitHub provides a portable, reviewable, and cloneable agent package.

## Published package

The complete 13-file HiveForge package is mirrored under:

`10_CUSTOM_AGENTS/UNPS_HiveForge/`

- `README.md`
- `BRAIN.md`
- `AGENT.md`
- `SYSTEM_INSTRUCTIONS.md`
- `PACKAGE_MANIFEST.md`
- `SKILLS.md`
- `WORKFLOWS.md`
- `MCP_PREFERENCES.md`
- `DEPENDENCIES.md`
- `OUTPUT_SCHEMAS.md`
- `TOOL_POLICY.md`
- `INSTALL.md`
- `CHANGELOG.md`

## Published support files

The mirror also includes public-safe files referenced by the package:

- Library README, index, and bootstrap
- File-routing and human-readable workspace standard
- Continuous-learning and growth loop
- README design skill
- Source-ingestion normalization
- Ponytail token-efficient engineering skill
- Last-30-days research skill
- Graphify codebase-intelligence skill and dependency profile
- Dependency status manifest
- Media-ingestion policy
- Composio staging profile
- LangGraph staging profile
- ToolJet Agent & Capability Registry contract
- Connector registry
- Model and harness router
- Prompt Database Agent control-plane workflow
- Workspace hygiene workflow
- Prompt Database Agent acceptance evaluation
- v0.5.0 production acceptance evidence

## Distribution tooling

- `install.sh` — non-root installer supporting immutable refs and optional archive SHA-256 verification
- `bin/hiveforge` — launcher for validation, bootstrap, dashboard, telemetry, and runtime state
- `dashboard/` — local Agent Command Center, runtime telemetry, approvals, and connector health
- `.github/workflows/production-gate.yml` — cross-platform Production CI gate
- `.github/workflows/release.yml` — automatic immutable tag/archive/checksum/release publication after a green `main` gate
- `scripts/production_gate.py` — package/version/status/privacy/secret regression guard
- `scripts/build_release.sh` — deterministic public release archive + `SHA256SUMS`
- `tests/` — install, dashboard, fallback, Graphify, and package round-trip smoke tests
- `.gitattributes` — deterministic LF line endings for Windows/WSL-sensitive files

## Public/private audit

The v0.5.0 public distribution was reviewed for known client/opportunity identifiers and common credential/private-key patterns. CI repeats these scans on every release commit.

## Validation

| Check | v0.5.0 result |
|---|---|
| HiveForge package files | PASS — 13/13 |
| Empty package files | PASS — 0 |
| Version consistency | PASS — 0.5.0 |
| Production status consistency | PASS |
| Credential/token scan | PASS — clear |
| Private-key scan | PASS — clear |
| Known client/opportunity identifiers | PASS — excluded |
| Linux fresh install | PASS |
| macOS fresh install | PASS |
| WSL/Ubuntu fresh install | PASS |
| Dashboard smoke test | PASS |
| Graphify live fixture | PASS — extraction + clustering |
| Fallback without Graphify | PASS |
| Export/import round trip | PASS — Linux + macOS |
| Three-workflow acceptance matrix | PASS — critical scenarios 11/11 |

## Excluded by design

The GitHub mirror does not contain:

- client or opportunity workspaces;
- private correspondence or contact information;
- credentials, tokens, secrets, or connector exports;
- regulated, medical, financial, legal, HR, or personally identifiable data;
- unrelated prompt-library assets;
- reference PDFs or source documents not explicitly approved for publication.

## Synchronization rule

Material internal changes must be reviewed for public suitability before GitHub synchronization. Do not automate blind publication from Drive. Update package versions and changelogs when behavior changes, then re-run credential, privacy, install, and acceptance gates before publishing.
