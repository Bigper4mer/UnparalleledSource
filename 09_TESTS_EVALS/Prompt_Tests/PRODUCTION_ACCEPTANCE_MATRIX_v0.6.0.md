# HiveForge v0.6.0 — Production Acceptance Matrix

Version: 0.6.0  
Scope: Guided onboarding + v0.5 control-plane regression  
Critical scenarios: **PASS**

This matrix defines the behavioral evidence required for the v0.6.0 production line. Automated CI provides executable evidence for install/runtime/onboarding behavior; repository policy and fixtures provide evidence for routing, learning, and fallback contracts.

## Scenario matrix

| # | Scenario | Expected behavior | Evidence |
|---|---|---|---|
| 1 | Guided onboarding | `hiveforge onboard` prints a usable first-run prompt and points to Getting Started | `tests/onboarding_cli_smoke.sh` |
| 2 | Experienced operator | Expert users can skip beginner ceremony and use workflow/command references directly | `docs/GETTING_STARTED.md`, `docs/WORKFLOW_GUIDE.md` |
| 3 | Human-readable user profile | `profile-init` creates a profile template outside project state and refuses overwrite | onboarding CLI smoke |
| 4 | Project routing | `project-init` creates an optional project intake only on explicit command and refuses overwrite | onboarding CLI smoke + BRAIN routing contract |
| 5 | Sensitive-data boundary | Intake/profile guidance explicitly excludes passwords, API keys, tokens, regulated and unrelated sensitive data | deterministic production gate |
| 6 | Workflow recommendation | Intake routes the user to the smallest useful workflow rather than loading every workflow | BRAIN + workflow guide |
| 7 | Evidence retrieval | Missing authorized evidence is retrieved before guessing or requesting redundant manual input | BRAIN evidence gate |
| 8 | File-system readability | Client/project/user state remains reconstructable by a competent human | BRAIN + file-routing standard |
| 9 | Learning scope | Corrections promote task → project → user/account → reusable skill/workflow → BRAIN only with evidence | BRAIN + learning loop |
| 10 | Linux install | Fresh install, doctor, version, bootstrap/onboard paths work | GitHub Actions |
| 11 | macOS install | Fresh install, doctor, version, bootstrap/onboard paths work | GitHub Actions |
| 12 | WSL install | Ubuntu WSL fresh install and launcher validation work | GitHub Actions |
| 13 | Graphify integration | `graphifyy==0.9.48` extracts/clusters fixture and generated graph is non-empty | GitHub Actions |
| 14 | Fallback | Core HiveForge remains functional without Graphify and optional capabilities remain optional | `tests/fallback_without_graphify.sh` |
| 15 | Dashboard | Local health endpoint reports v0.6.0 and dashboard starts without cloud dependency | `tests/dashboard_smoke.py` |
| 16 | Package round trip | Public package exports, extracts and installs on Linux/macOS | package round-trip jobs |
| 17 | ToolJet staging | Compose file validates; ToolJet remains STAGED and cannot replace canonical policy | ToolJet config job + dependency manifest |
| 18 | Public/private boundary | No credential/private-key patterns or prohibited private-scope paths in public mirror | deterministic production gate |

## Required workflow coverage

### Workflow A — Guided first-time user

`install → doctor → onboard → profile-init → inspect project → recommend workflow → first verified task → scoped learning`

Expected: minimal useful intake, no secret collection, no duplicate project state, clear commands and next actions.

### Workflow B — Experienced operator

`doctor → docs/workflow reference → direct implementation/research workflow → verification`

Expected: no forced tutorial, architecture and tool/fallback details available on demand.

### Workflow C — Existing complex project

`load validated user context → inspect current repository/state → Graphify or equivalent repository intelligence when justified → exact source → tests → verification → project-scoped learning`

Expected: no unnecessary new project root, no broad context dump, Graphify optional, evidence-grounded completion.

### Workflow D — Shared operations cockpit

`local Command Center → optional ToolJet config validation → team registry/promotion queue`

Expected: ToolJet is a presentation/control layer; canonical authorization, maturity, source-of-truth and learning remain outside page-level UI logic.

## Promotion rule

v0.6.0 can be tagged Production only when the Production Gate is green for the exact commit merged to `main`. Any material behavioral change after that commit requires another release-validation cycle.
