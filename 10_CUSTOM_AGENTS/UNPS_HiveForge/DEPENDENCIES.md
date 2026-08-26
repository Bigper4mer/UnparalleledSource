# UNPS HiveForge — Dependencies

Version: 0.7.0
Status: Production

## Core

- A compatible instruction-following agent environment
- Access to the package Markdown files
- Access to `PROMPTS.UNPS` or a downloaded subset of its required assets
- UTF-8 Markdown/plain-text support

The core curation, routing, onboarding, and learning behavior has no mandatory Python or Node package dependency.

## Conditional dependencies

| Capability | Dependency | Maturity | Policy |
|---|---|---|---|
| Connected Drive maintenance | Authorized Google Drive/Workspace connector | CORE | Use least privilege |
| Repository operations | Authorized GitHub connector or Git client | CORE | Use repository permissions appropriate to task |
| Local Command Center | Python 3.9+ standard library | CORE-OPTIONAL | Required only for dashboard and telemetry commands |
| Repository intelligence | Python 3.10+, `graphifyy==0.9.48` | CANDIDATE | Use only when repository complexity justifies it |
| Compact page retrieval | Node.js 20+, `@only-cli/oc` | CANDIDATE | Prefer for known public text-heavy pages before heavier retrieval |
| Media ingestion | `yt-dlp` | CANDIDATE | Preferred media CLI; pin exact tested release at promotion |
| Legacy media compatibility | `youtube-dl` | REFERENCE | Do not select for new workflows by default |
| Structured crawling | Firecrawl connector/API | CORE/AVAILABLE | Avoid when simpler retrieval works |
| External action/tool layer | Composio | STAGED | Prefer native connectors first; pilot with isolated least-privilege session |
| Durable orchestration | LangGraph | STAGED | Use only for stateful/resumable workflows that need it |
| Human operations cockpit | ToolJet | STAGED | Presentation/control surface only; canonical policy remains outside ToolJet |
| Browser interaction | Approved browser automation capability | ON-DEMAND | Escalation only |

## Canonical dependency registry

See `06_DEPENDENCIES/DEPENDENCY_STATUS_MANIFEST.md` for maturity, promotion, fallback, and audit rules.

## Dependency governance

- Pin versions for production-critical external packages.
- Review permissions, maintenance, licensing, network behavior, data handling, prompt-injection surface, and overlap before adoption.
- Install optional extras only when a real workflow requires them.
- Store credential names as placeholders only; store actual secrets in approved secret management.
- Record production dependency changes in `CHANGELOG.md` and the canonical dependency registry.
- A missing optional dependency must trigger a capability-equivalent fallback or an explicit blocker, never invented success.
