# UNPS Dependency Status Manifest

Version: 0.1.0  
Status: Candidate  
Owner: Unparalleled Source  
Updated: 2026-08-24

## Purpose

Provide one human-readable control point for dependency maturity, routing, promotion, and fallback. Dependencies are capabilities, not defaults: load or install only when the task requires them.

## Maturity states

- **CORE** — validated and approved for normal use.
- **CANDIDATE** — integrated and useful, but still needs broader real-work validation.
- **STAGED** — researched, documented, and ready for an isolated promotion test; not part of the default runtime.
- **REFERENCE** — discovery/reference source only; do not install automatically.
- **RESTRICTED** — only for explicitly justified/authorized use.
- **DEPRECATED** — retained for provenance or compatibility; do not select for new work.

## Current capability matrix

| Capability | Dependency | State | Preferred use | Promotion requirement |
|---|---|---|---|---|
| Connected UNPS data | Google Workspace connectors | CORE | Drive, Gmail, Calendar, Contacts | Maintain regression coverage |
| Repository operations | GitHub connector | CORE | repos, issues, PRs, source inspection | Maintain permissions + regression coverage |
| Structured web acquisition | Firecrawl | CORE | site/page extraction to clean Markdown/JSON | Keep source and extraction provenance |
| Repository intelligence | Graphify (`graphifyy`) | CANDIDATE | architecture, impact, path/explain, scoped hydration | Live graph + accuracy review |
| Compact public-page retrieval | `@only-cli/oc` | CANDIDATE | known public text-heavy URLs | Benchmark against normal retrieval |
| Media acquisition | `yt-dlp` | CANDIDATE | public/authorized media metadata/subtitles/media | Live install + bounded smoke test |
| Legacy media fallback | `youtube-dl` | REFERENCE | compatibility research only | Specific compatibility case only |
| Agent tool/action layer | Composio | STAGED | runtime discovery/auth/action across external apps | Isolated least-privilege pilot |
| Durable agent orchestration | LangGraph | STAGED | long-running stateful workflows, checkpoints, HITL | Restart/resume + approval + observability pilot |
| Human operations cockpit | ToolJet | STAGED | Agent & Capability Registry | Backed registry + RBAC + mutation-boundary test |
| Capability discovery | public-apis / free-for-dev / VoltAgent catalogs | REFERENCE | discover candidate APIs/skills/services | Each candidate passes normal dependency gate |
| Agent R&D patterns | MARKTECHPOST AI Agents tutorials | REFERENCE | implementation patterns and experiments | Extract only tested reusable patterns |
| Anti-detection browser automation | CloakBrowser | RESTRICTED | legitimate authorized cases only | Explicit need + policy/ToS review |

## Selection order

1. Existing deterministic/local capability.
2. Native connected connector/MCP.
3. Existing approved CLI/API/service.
4. Candidate dependency already in the registry.
5. Search approved reference catalogs.
6. Stage a new dependency only when expected value justifies maintenance, security, context, and lock-in cost.

## Promotion gate

A STAGED or CANDIDATE dependency may move to CORE only after:

1. current upstream maintenance is verified;
2. setup is reproducible and version policy is recorded;
3. permissions, secrets, network behavior, licensing, and prompt-injection surface are reviewed;
4. at least one representative UNPS workflow succeeds end to end;
5. failure/fallback behavior is verified;
6. token/context and operational cost are acceptable;
7. human-readable setup and rollback instructions exist;
8. a regression fixture exists when the dependency is material to core workflows.

## Version policy

Do not hard-code floating `latest` into production deployments. At promotion, pin an exact tested version or immutable image/tag and record the validation date.

## Portability rule

Agent packages reference required capabilities by role. If a preferred dependency is unavailable, BRAIN selects the nearest capability-equivalent fallback. No core agent should fail solely because one optional branded dependency is absent.
