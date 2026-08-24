# UNPS HiveForge — Dependencies

Version: 0.4.0  
Status: Candidate

## Core

- A compatible instruction-following agent environment
- Access to the package Markdown files
- Access to `PROMPTS.UNPS` or a downloaded subset of its required assets
- UTF-8 Markdown/plain-text support

The core curation and routing behavior has no mandatory Python or Node package dependency.

## Conditional dependencies

| Capability | Dependency | Policy |
|---|---|---|
| Connected Drive maintenance | Authorized Google Drive/Workspace connector | Use least privilege |
| Local Command Center | Python 3.9+ standard library | Optional; required only for dashboard and telemetry commands |
| Repository work | Git client and repository-aware coding harness | Project dependent |
| Graphify repository intelligence | Python 3.10+, `graphifyy==0.9.48` | Candidate; install only when justified |
| NetworkX graph consumption | Compatible Python and NetworkX runtime | Optional |
| Only-CLI text retrieval | Node.js 20+, `@only-cli/oc` | Optional candidate |
| Structured crawling | Firecrawl connector/API | Optional; avoid when simpler retrieval works |
| Browser interaction | Approved browser automation capability | Escalation only |

## Dependency governance

- Pin versions for production-critical external packages.
- Review permissions, maintenance, licensing, network behavior, data handling, prompt-injection surface, and overlap before adoption.
- Install optional extras only when a real workflow requires them.
- Store credential names as placeholders only; store actual secrets in approved secret management.
- Record production dependency changes in `CHANGELOG.md` and the canonical dependency registry.
