# UNPS HiveForge

> The Unparalleled Source agent foundry: a portable control plane for prompts, skills, workflows, connectors, dependencies, evaluations, and deployable Custom Agents.

**Version:** 0.5.0  
**Status:** Release Candidate  
**Canonical workspace:** `PROMPTS.UNPS`

## What it does

HiveForge performs the Prompt Database Agent role while presenting a stronger UNPS product identity. It keeps the UNPS Agent Engineering Library useful as a living operating system, inventories and normalizes reusable assets, prevents duplication, routes project files correctly, composes specialized Custom Agent packages, applies evaluation gates, and promotes only patterns proven through real UNPS work.

Public framework: [github.com/Bigper4mer/UnparalleledSource](https://github.com/Bigper4mer/UnparalleledSource)

## Optimized startup

```text
BRAIN.md
  → AGENT.md
  → SYSTEM_INSTRUCTIONS.md
  → PACKAGE_MANIFEST.md
  → task-specific workflow
  → required skills/connectors/dependencies/schema
```

Only the first four files belong in normal startup context. Everything else loads through progressive disclosure.

## Agent Command Center

The public distribution includes a localhost-only operational dashboard for instrumented HiveForge runs:

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
  → resolve client/project scope
  → inspect existing state
  → classify task and depth
  → retrieve minimum evidence
  → select workflow and skills
  → execute with authorized tools
  → verify
  → route and document
  → capture durable learning
```

## Capability maturity

HiveForge distinguishes `CORE`, `CANDIDATE`, `STAGED`, `REFERENCE`, `RESTRICTED`, and `DEPRECATED` dependencies. Optional capabilities do not become package requirements merely because they are available.

Current examples:

- Graphify — Candidate repository intelligence.
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

The v0.5.0 release gate is automated under `.github/workflows/production-gate.yml` and covers:

- package/version consistency;
- public/private and secret scans;
- Linux and macOS fresh installs;
- WSL validation when the runner exposes WSL;
- dashboard health smoke test;
- live Graphify fixture test;
- fallback without Graphify;
- package export/import round trip;
- three-workflow acceptance evidence.

Production promotion requires all mandatory gates to pass. Optional capabilities can remain Candidate/Staged without blocking the core package when fallback behavior is verified.

## Distribution

For a released immutable tag:

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh | sh
```

Release artifacts are accompanied by SHA-256 checksums.

---

**Unparalleled Source** — Reusable intelligence. Portable agents. Verified execution.
