# UNPS HiveForge — Drive to GitHub Sync Manifest

Version: 1.4.0
Updated: 2026-08-26
GitHub repository: `Bigper4mer/UnparalleledSource`  
Canonical internal source: `PROMPTS.UNPS`  
Production release line: `v0.7.0`

## Purpose

Record the public-safe subset of the canonical Drive library mirrored into GitHub. Drive remains the internal source of truth; GitHub provides a portable, reviewable, cloneable, guided agent package.

## Published package

The complete HiveForge package is mirrored under `10_CUSTOM_AGENTS/UNPS_HiveForge/`:

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

## Guided onboarding surface

The v0.7.0 public mirror also includes:

- `docs/GETTING_STARTED.md`
- `docs/USER_INTAKE.md`
- `docs/WORKFLOW_GUIDE.md`
- `docs/COMMAND_REFERENCE.md`
- `docs/TOOLING_GUIDE.md`
- `docs/TOOLJET_SETUP.md`
- `docs/TROUBLESHOOTING.md`
- `docs/README.md`
- `examples/FIRST_RUN_PROMPT.md`
- `examples/USER_PROFILE_TEMPLATE.md`
- `examples/PROJECT_INTAKE_TEMPLATE.md`
- `tooljet/docker-compose.yml`

## Published support files

The mirror includes public-safe shared assets referenced by the package, including library governance, file-routing and human-readable workspace standards, continuous learning, model/harness routing, connector policy, workspace hygiene, dependency maturity, Graphify repository intelligence, media ingestion policy, Composio/LangGraph staging profiles, ToolJet registry contract, and acceptance tests.

## Distribution tooling

- `install.sh` — non-root installer supporting immutable refs and optional archive SHA-256 verification
- `bin/hiveforge` — launcher for onboarding, validation, docs, profile/project intake, dashboard, telemetry and ToolJet evaluation commands
- `dashboard/` — local Agent Command Center, runtime telemetry, approvals and connector health
- `tooljet/` — optional STAGED ToolJet evaluation stack
- `.github/workflows/production-gate.yml` — cross-platform Production CI gate
- `.github/workflows/release.yml` — immutable tag/archive/checksum/release publication after a green `main` gate
- `scripts/production_gate.py` — package/version/status/privacy/secret/onboarding regression guard
- `scripts/build_release.sh` — deterministic public release archive + `SHA256SUMS`
- `tests/` — install, onboarding, dashboard, fallback, Graphify, ToolJet-config and package round-trip checks
- `.gitattributes` — deterministic LF line endings for Windows/WSL-sensitive files

## v0.7.0 validation contract

| Check | Requirement |
|---|---|
| HiveForge package files | PASS |
| Version/status consistency | 0.7.0 / Production |
| Credential/private-key scan | Clear |
| Public/private path boundary | Clear |
| Guided onboarding documentation | Present and linked |
| `hiveforge onboard` | PASS |
| `profile-init` / `project-init` no-overwrite | PASS |
| Linux fresh install | PASS |
| macOS fresh install | PASS |
| WSL/Ubuntu fresh install | PASS |
| Dashboard run/heartbeat/approval smoke test | PASS |
| Graphify live fixture | PASS — extraction + clustering |
| Fallback without Graphify | PASS |
| Export/import round trip | PASS — Linux + macOS |
| ToolJet Compose configuration | PASS while ToolJet remains STAGED |
| v0.7 acceptance matrix | PASS |

## Excluded by design

The GitHub mirror does not contain client or opportunity workspaces, private correspondence/contact information, credentials/tokens/secrets, regulated or sensitive records, private connector exports, or internal-only source documents not explicitly approved for publication.

## Synchronization rule

Material internal changes must be reviewed for public suitability before GitHub synchronization. Do not automate blind publication from Drive. Update package versions and changelogs when behavior changes, then re-run credential, privacy, install, onboarding, ToolJet-config and acceptance gates before publishing.
