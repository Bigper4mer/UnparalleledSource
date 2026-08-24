# UNPS HiveForge — Drive to GitHub Sync Manifest

Version: 1.1.0  
Updated: 2026-08-24  
GitHub repository: `Bigper4mer/UnparalleledSource`  
Canonical internal source: `PROMPTS.UNPS`  
Target public release: `v0.5.0`

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
- `.github/workflows/production-gate.yml` — release-candidate CI gate
- `.github/workflows/release.yml` — versioned archive/checksum/release automation
- `scripts/production_gate.py` — package/version/privacy/secret regression guard
- `scripts/build_release.sh` — deterministic public release archive + SHA256SUMS
- `tests/` — install, dashboard, fallback, Graphify, and package round-trip smoke tests

## Public/private audit

The v0.5.0 release branch was reviewed for known client/opportunity identifiers and common credential/private-key patterns before release preparation. CI repeats these scans on every candidate commit.

## Validation

| Check | Release-gate expectation |
|---|---|
| HiveForge package files | 13/13 |
| Empty package files | 0 |
| Version consistency | 0.5.0 across package release metadata |
| Credential/token scan | Clear |
| Private-key scan | Clear |
| Known client/opportunity identifiers | Excluded |
| Linux fresh install | Required pass |
| macOS fresh install | Required pass |
| WSL install | Required when WSL runner is available; otherwise explicit external gate |
| Dashboard smoke test | Required pass |
| Graphify live fixture | Required pass for Graphify integration evidence |
| Fallback without Graphify | Required pass |
| Export/import round trip | Required pass |
| Three-workflow acceptance matrix | Required pass/evidence |

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
