# UNPS HiveForge Changelog

All material package changes are recorded here. Dates use `YYYY-MM-DD`.

## 0.6.0 — 2026-08-24

### Added

- Guided onboarding journey from discovery → install → intake → first verified task.
- `hiveforge onboard` for copy/paste first-run agent intake.
- `hiveforge docs` documentation router.
- `hiveforge profile-init [PATH]` human-readable user working-profile template.
- `hiveforge project-init [PATH]` optional project-intake template with no-overwrite protection.
- User intake guidance separating durable working preferences from project/client facts.
- Workflow guide with recommended inputs, starter prompts, and completion expectations.
- Complete CLI/runtime command reference.
- Tool/capability maturity guide and troubleshooting guide.
- ToolJet setup guide and optional Docker Compose evaluation stack.
- README visualizations for user journey, architecture, workflow lifecycle, learning loop, and ToolJet role.
- Production-gate coverage for onboarding documentation, executable onboarding CLI behavior, profile/project no-overwrite safeguards, and ToolJet Compose configuration.

### Changed

- BRAIN is now user-context-aware and performs minimum useful first-run intake plus returning-user delta checks.
- Agent/system behavior adapts to Guided, Working, or Expert operation by domain without treating experience as global.
- User working preferences are explicit human-readable state and remain separate from project/client facts.
- Package startup sequence now loads validated user context only when relevant.
- README and package documentation now prioritize a copy/paste startup path for inexperienced users while retaining expert/operator references.

### Security

- Reusable user profiles explicitly exclude passwords, API keys, tokens, private keys, auth cookies, regulated data, unrelated sensitive personal information, and one-off project exceptions.
- ToolJet remains a STAGED presentation/control surface and cannot replace canonical authorization/policy state.
- Profile and project initialization refuse silent overwrite.

### Validation

- Production Gate includes all v0.5.0 regression coverage plus guided-onboarding CLI and ToolJet configuration checks.
- v0.6.0 acceptance evidence is recorded in `09_TESTS_EVALS/Prompt_Tests/PRODUCTION_ACCEPTANCE_MATRIX_v0.6.0.md`.

### Status

Production.

## 0.5.0 — 2026-08-24

### Added

- Production release gate with version consistency, public/private boundary checks, secret scanning, install matrix, dashboard smoke test, Graphify fixture test, fallback validation, package export/import round trip, and release checksum generation.
- Dependency maturity manifest with `CORE`, `CANDIDATE`, `STAGED`, `REFERENCE`, `RESTRICTED`, and `DEPRECATED` states.
- Staging profiles for Composio and LangGraph.
- ToolJet Agent & Capability Registry implementation contract.
- Media ingestion policy preferring `yt-dlp` and keeping `youtube-dl` as compatibility reference only.
- Three-workflow production acceptance evidence.
- Cross-platform line-ending guard for Windows/WSL compatibility.

### Validation

- Static/privacy/secret gate: PASS.
- Fresh Linux install: PASS.
- Fresh macOS install: PASS.
- Fresh WSL/Ubuntu install: PASS.
- Dashboard health smoke test: PASS.
- Live Graphify 0.9.48 extraction + clustering fixture: PASS.
- Fallback without Graphify: PASS.
- Package export/import round trip on Linux and macOS: PASS.

### Status

Production.

## 0.4.0 — 2026-08-24

- Added the built-in HiveForge Command Center, run telemetry, approvals, connector health, and runtime instrumentation commands.

## 0.3.1 — 2026-08-24

- Added the non-root macOS/Linux/WSL installer and `hiveforge` launcher with validation/bootstrap/version commands.

## 0.3.0 — 2026-08-24

- Established the compact package manifest, progressive-disclosure startup set, workflow/skill/connectors/dependency/output routing, public GitHub framework, and HiveForge product identity.

## 0.2.0 — 2026-08-24

- Added model-agnostic BRAIN orchestration, client/project routing, continuous learning, and repository-intelligence routing.

## 0.1.0 — 2026-08-23

- Established the initial Prompt Database Agent identity, system instructions, and library structure.
