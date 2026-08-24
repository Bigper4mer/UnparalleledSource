# UNPS HiveForge

> The Unparalleled Source agent foundry: a portable control plane for prompts, skills, workflows, connectors, dependencies, evaluations, and deployable Custom Agents.

**Version:** 0.4.0  
**Status:** Deployment-ready Candidate  
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

Only the first four files belong in the normal startup context. Everything else loads through progressive disclosure.

## Agent Command Center

The public distribution includes a localhost-only operational dashboard for
instrumented HiveForge runs:

```bash
hiveforge dashboard
hiveforge run --task "Prompt library health check" -- your-command
```

It reports run status, elapsed time, heartbeat, pending approvals, recent runs,
and connector health without storing command output, prompt bodies, or secrets.
See the public [Command Center guide](https://github.com/Bigper4mer/UnparalleledSource/blob/main/docs/COMMAND_CENTER.md).

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

## Custom Agent factory

The package composes shared UNPS intelligence into portable specialist builds such as Government Capture, Research Intelligence, Coding, and Document Production agents. Shared assets remain canonical in the main library; individual agents reference only what they need.

## Context efficiency

- Search before creating.
- Reference shared assets instead of copying them.
- Convert heavyweight text sources once for repeated use while preserving authoritative originals.
- Prefer deterministic tools and targeted retrieval before expensive model escalation.
- Use Graphify only when repository complexity justifies building a graph.

## Deployment

Follow `INSTALL.md`, then run `09_TESTS_EVALS/Prompt_Tests/PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md`.

## Current limitation

The package is complete enough to deploy as a Candidate. Production status remains gated on repeated acceptance-test passes across materially different UNPS workflows and a successful live Graphify extraction if Graphify is included in a production coding profile.

---

**Unparalleled Source** — Reusable intelligence. Portable agents. Verified execution.
