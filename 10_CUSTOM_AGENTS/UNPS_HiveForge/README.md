# UNPS HiveForge

> The Unparalleled Source agent foundry: a portable control plane for prompts, skills, workflows, connectors, dependencies, evaluations, and deployable Custom Agents.

**Version:** 0.5.0  
**Status:** Production  
**Canonical workspace:** `PROMPTS.UNPS`

## New user start

Install and verify:

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh | sh

hiveforge doctor
hiveforge version
hiveforge bootstrap
```

Then follow the repository's guided onboarding:

- [`docs/GETTING_STARTED.md`](../../docs/GETTING_STARTED.md) — discovery → install → intake → first task
- [`docs/USER_INTAKE.md`](../../docs/USER_INTAKE.md) — safe user/profile learning
- [`docs/WORKFLOW_GUIDE.md`](../../docs/WORKFLOW_GUIDE.md) — recommended workflows and inputs
- [`docs/COMMAND_REFERENCE.md`](../../docs/COMMAND_REFERENCE.md) — complete shell/runtime command reference
- [`docs/TOOLING_GUIDE.md`](../../docs/TOOLING_GUIDE.md) — tools, dependencies, maturity and routing
- [`docs/TOOLJET_SETUP.md`](../../docs/TOOLJET_SETUP.md) — optional shared team cockpit
- [`examples/FIRST_RUN_PROMPT.md`](../../examples/FIRST_RUN_PROMPT.md) — copy/paste first-run prompt

## What it does

HiveForge performs the Prompt Database Agent role while presenting a stronger UNPS product identity. It keeps the UNPS Agent Engineering Library useful as a living operating system, inventories and normalizes reusable assets, prevents duplication, routes project files correctly, composes specialized Custom Agent packages, applies evaluation gates, and promotes only patterns proven through real work.

Public framework: [github.com/Bigper4mer/UnparalleledSource](https://github.com/Bigper4mer/UnparalleledSource)

## Optimized startup

```text
BRAIN.md
  → AGENT.md
  → SYSTEM_INSTRUCTIONS.md
  → PACKAGE_MANIFEST.md
  → validated user/project context
  → task-specific workflow
  → required skills/connectors/dependencies/schema
```

Only the first four package files belong in normal startup context. Everything else loads through progressive disclosure.

## Recommended first-run behavior

A new HiveForge user should be guided through:

```mermaid
flowchart LR
    A[Verify package] --> B[Learn working preferences]
    B --> C[Inspect current project]
    C --> D[Identify source of truth]
    D --> E[Recommend workflow]
    E --> F[Execute one real task]
    F --> G[Verify]
    G --> H[Capture validated learning]
```

User-level preferences and project/client facts remain separate. Secrets and sensitive personal information do not belong in reusable profile or learning files.

## Agent Command Center

```bash
hiveforge dashboard
hiveforge run --task "Prompt library health check" -- your-command
```

It reports run status, elapsed time, heartbeat, pending approvals, recent runs, and connector health without storing command output, prompt bodies, or secrets.

## Package contents

| File | Purpose |
|---|---|
| `BRAIN.md` | Model-agnostic orchestration and routing contract |
| `AGENT.md` | Identity, mission, responsibilities, and maturity |
| `SYSTEM_INSTRUCTIONS.md` | Persistent operating policy |
| `PACKAGE_MANIFEST.md` | Startup, shared references, and integrity rules |
| `SKILLS.md` | Task-to-skill routing |
| `WORKFLOWS.md` | Task-to-workflow routing |
| `MCP_PREFERENCES.md` | Connector selection and fallback order |
| `DEPENDENCIES.md` | Core and conditional runtime requirements |
| `OUTPUT_SCHEMAS.md` | Maintenance, asset, and validation contracts |
| `TOOL_POLICY.md` | Authorization, evidence, security, and mutation boundaries |
| `INSTALL.md` | Connected and portable deployment |
| `CHANGELOG.md` | Version history |

## Operating lifecycle

```text
request
  → resolve user/project/client scope
  → inspect existing state
  → classify task and depth
  → retrieve minimum evidence
  → select workflow and skills
  → execute with authorized tools
  → verify
  → route and document
  → capture durable learning at the correct scope
```

## Capability maturity

HiveForge distinguishes `CORE`, `CANDIDATE`, `STAGED`, `REFERENCE`, `RESTRICTED`, and `DEPRECATED` dependencies. Optional capabilities do not become package requirements merely because they are available.

Current examples:

- Graphify — Candidate repository intelligence, with live v0.9.48 integration evidence.
- yt-dlp — Candidate media ingestion; youtube-dl is compatibility reference only.
- Composio — Staged external action/tool layer.
- LangGraph — Staged durable orchestration.
- ToolJet — Staged human operations cockpit and Agent & Capability Registry.

## Context efficiency

- Search before creating.
- Reference shared assets instead of copying them.
- Convert heavyweight text sources once for repeated use while preserving authoritative originals.
- Prefer deterministic tools and targeted retrieval before expensive model escalation.
- Use Graphify only when repository complexity justifies building a graph.
- Prefer native/connected tools before adding another external dependency.

## Production validation

HiveForge v0.5.0 earned Production status through the automated `.github/workflows/production-gate.yml` release gate. The validated release line covers:

- package/version/status consistency;
- public/private and secret scans;
- fresh Linux, macOS, and WSL installs;
- dashboard health smoke test;
- live Graphify v0.9.48 fixture extraction and clustering;
- fallback without Graphify;
- package export/import round trips;
- three-workflow acceptance evidence.

Optional capabilities can remain Candidate/Staged without blocking the core package when fallback behavior is verified.

---

**Unparalleled Source** — Reusable intelligence. Portable agents. Verified execution.
