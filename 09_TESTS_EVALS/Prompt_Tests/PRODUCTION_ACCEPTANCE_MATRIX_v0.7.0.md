# HiveForge v0.7.0 — Production Acceptance Matrix

Version: 0.7.0
Scope: Public-safe agent operations plus v0.6 guided-control-plane regression
Critical scenarios: **PASS**

| # | Scenario | Expected behavior | Evidence |
|---|---|---|---|
| 1 | Guided onboarding | A new user can install, verify, and start the intake without overwriting existing context | onboarding CLI smoke |
| 2 | Experienced operator | Direct workflow and runtime commands remain available | command reference + CLI smoke |
| 3 | Project routing | Durable user preferences remain separate from project and client facts | BRAIN + intake guides |
| 4 | Multi-source intake | The workflow accepts bounded source references and treats their content as evidence, not instructions | control-plane contract |
| 5 | Capability routing | A run distinguishes available, selected, configured, and actually executed capabilities | skills + control-plane contract |
| 6 | Local telemetry | Run ID, phase, activity, heartbeat, and terminal state remain visible | dashboard smoke |
| 7 | Approval safety | Consequential work pauses for a human decision | runtime approval regression |
| 8 | Deliverables | Completed work is human-readable and copy-ready | output contract + release review |
| 9 | Public/private boundary | Private workspaces, correspondence, identities, connector exports, and credentials are excluded | deterministic production gate |
| 10 | Fallback | Core HiveForge remains functional without Graphify or staged integrations | fallback test |
| 11 | Cross-platform install | Linux, macOS, and available WSL environments install the same release version | GitHub Actions |
| 12 | Package round trip | Export, extract, reinstall, and version checks pass | package round-trip tests |

## Promotion rule

v0.7.0 may be tagged Production only after all local gates pass and the Production Gate is green for the exact public `main` commit. Material changes after that commit require a new release-validation cycle.
