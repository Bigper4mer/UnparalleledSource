# UNPS HiveForge Changelog

All material package changes are recorded here. Dates use `YYYY-MM-DD`.

## 0.5.0 — 2026-08-24

### Added

- Production release gate with version consistency, public/private boundary checks, secret scanning, install matrix, dashboard smoke test, Graphify fixture test, fallback validation, package export/import round trip, and release artifact checksum generation.
- Dependency maturity manifest with `CORE`, `CANDIDATE`, `STAGED`, `REFERENCE`, `RESTRICTED`, and `DEPRECATED` states.
- Staging profiles for Composio and LangGraph.
- ToolJet Agent & Capability Registry implementation contract.
- Media ingestion policy preferring `yt-dlp` and keeping `youtube-dl` as compatibility reference only.
- Three-workflow production acceptance evidence.
- Cross-platform line-ending guard for Windows/WSL compatibility.

### Changed

- Synced package version to BRAIN v0.5-era behavior.
- Installer now supports immutable release refs and release-artifact checksum verification.
- Public package metadata distinguishes core Production readiness from independently staged/candidate optional capabilities.
- Release automation now publishes only after the Production Gate succeeds on `main`.

### Security

- Added repository secret scan and public/private forbidden-term gate.
- Added explicit public distribution license notice preserving Unparalleled Source rights unless a separate license is granted.
- Release archives include SHA-256 checksums.

### Validation

- Static/privacy/secret gate: PASS.
- Three-workflow acceptance evidence: PASS.
- Fresh Linux install: PASS.
- Fresh macOS install: PASS.
- Fresh WSL/Ubuntu install: PASS.
- Dashboard health smoke test: PASS.
- Live Graphify 0.9.48 extraction + clustering fixture: PASS.
- Fallback without Graphify: PASS.
- Package export/import round trip on Linux and macOS: PASS.

### Status

Production. The immutable `v0.5.0` release is published automatically from the exact tested `main` commit after its Production Gate succeeds. Optional dependencies retain their independent maturity states.

## 0.4.0 — 2026-08-24

### Added

- Built-in HiveForge Command Center.
- Dependency-free local run telemetry, heartbeat, approvals, and connector health.
- `dashboard`, `run`, `status`, `start`, `event`, `finish`, `approval`, `decide`, and `connector` commands.

### Security

- Dashboard binds to localhost by default.
- Telemetry stores sanitized run metadata, not command output, prompt content, or credentials.

## 0.3.1 — 2026-08-24

### Added

- One-command, non-root installer for macOS, Linux, and WSL.
- `hiveforge` launcher with `doctor`, `bootstrap`, `path`, and `version` commands.
- Atomic staging, package validation, safe overwrite refusal, and recoverable backups.

### Changed

- GitHub is now a directly installable public-safe distribution, while Drive remains the canonical internal source.

## 0.3.0 — 2026-08-24

### Added

- Compact package manifest and optimized startup set.
- Skill and workflow routing manifests.
- MCP/connector preference profile.
- Core and optional dependency policy.
- Output schemas for maintenance, assets, and validation.
- Tool authorization, evidence, security, and economy policy.
- Connected-Drive and portable-subset installation instructions.
- Dedicated shared control-plane workflow and acceptance evaluation references.
- Public GitHub framework with a custom UNPS-branded repository experience.

### Renamed

- Product identity changed from Prompt Database Agent to **UNPS HiveForge**.
- Stable agent ID and Prompt Database Agent technical role were preserved.

### Optimized

- Progressive-disclosure load order: four startup files, all other assets on demand.
- Shared library policies are referenced rather than copied into the package.
- Graphify is routed only to sufficiently complex repositories and remains Candidate.
- Core agent operation no longer implies mandatory Python or Node dependencies.

### Status

Deployment-ready Candidate. Production promotion still requires repeated scenario passes on materially different UNPS workflows.

## 0.2.0 — 2026-08-24

- Added model-agnostic `BRAIN.md` orchestration.
- Added project/client routing and continuous-learning contracts.
- Added Graphify repository-intelligence gate.

## 0.1.0 — 2026-08-23

- Established the initial Prompt Database Agent identity, system instructions, and library structure.
