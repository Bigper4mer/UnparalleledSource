# UNPS HiveForge

> The Unparalleled Source agent foundry: a portable control plane for prompts, skills, workflows, connectors, dependencies, evaluations, onboarding, and deployable Custom Agents.

**Version:** 0.6.0  
**Status:** Production  
**Canonical workspace:** `PROMPTS.UNPS`

## Start here

New users should begin with:

1. `docs/GETTING_STARTED.md`
2. `docs/USER_INTAKE.md`
3. `docs/WORKFLOW_GUIDE.md`
4. `docs/COMMAND_REFERENCE.md`

Fast path after installation:

```bash
hiveforge doctor
hiveforge version
hiveforge onboard
```

`hiveforge onboard` prints a copy/paste prompt for the first agent session. It asks HiveForge to learn only useful work preferences, inspect the current project/source of truth, recommend the smallest useful workflow, execute a real task, verify it, and capture only durable learning.

## Optimized startup

```text
BRAIN.md
  → AGENT.md
  → SYSTEM_INSTRUCTIONS.md
  → PACKAGE_MANIFEST.md
  → validated user working profile when relevant
  → current project/source of truth
  → task-specific workflow
  → required skills/connectors/dependencies/schema
```

Only the first four package files belong in normal startup context. Everything else loads through progressive disclosure.

## User context and learning

HiveForge keeps three scopes separate:

```text
USER
  role · goals · domain experience · working preferences · tool preferences

PROJECT
  client/internal scope · source of truth · decisions · status · project learnings

TASK
  goal · workflow · evidence · execution · verification
```

Durable learning moves upward cautiously:

```text
task → project → user/account → reusable skill/workflow → BRAIN
```

Never store passwords, API keys, auth tokens, regulated data, unrelated sensitive personal information, or one-off project exceptions as reusable user-profile data.

## Agent Command Center

The public distribution includes a localhost-only operations dashboard:

```bash
hiveforge dashboard
hiveforge run --task "Prompt library health check" -- your-command
```

It reports run status, elapsed time, heartbeat, approvals, recent runs, and connector health without storing prompt bodies, command output, credentials, or arbitrary environment variables.

## Guided commands

```text
hiveforge onboard
hiveforge docs
hiveforge profile-init [PATH]
hiveforge project-init [PATH]
```

Core runtime commands:

```text
hiveforge doctor
hiveforge bootstrap
hiveforge dashboard
hiveforge run
hiveforge status
hiveforge start
hiveforge event
hiveforge finish
hiveforge approval
hiveforge decide
hiveforge connector
```

Optional ToolJet evaluation commands:

```text
hiveforge tooljet status
hiveforge tooljet config
hiveforge tooljet up
hiveforge tooljet url
hiveforge tooljet down
```

## Package contents

| File | Purpose |
|---|---|
| `BRAIN.md` | Model-agnostic orchestration, routing, user-context and learning contract |
| `AGENT.md` | Identity, mission, responsibilities and maturity |
| `SYSTEM_INSTRUCTIONS.md` | Persistent operating policy |
| `PACKAGE_MANIFEST.md` | Startup, shared references and integrity rules |
| `SKILLS.md` | Task-to-skill routing |
| `WORKFLOWS.md` | Task-to-workflow routing |
| `MCP_PREFERENCES.md` | Connector selection and fallback order |
| `DEPENDENCIES.md` | Core and conditional runtime requirements |
| `OUTPUT_SCHEMAS.md` | Maintenance, asset and validation contracts |
| `TOOL_POLICY.md` | Authorization, evidence, security and mutation boundaries |
| `INSTALL.md` | Connected and portable deployment |
| `CHANGELOG.md` | Version history |

## Operating lifecycle

```text
request
  → understand user/task
  → resolve client/project scope
  → inspect source of truth
  → classify depth
  → retrieve minimum evidence
  → recommend/select workflow
  → load only required skills/tools
  → execute
  → verify
  → route/document
  → capture durable learning
```

## Capability maturity

HiveForge distinguishes `CORE`, `CANDIDATE`, `STAGED`, `REFERENCE`, `RESTRICTED`, and `DEPRECATED` dependencies.

Current examples:

- Graphify — Candidate repository intelligence with live `0.9.48` integration evidence.
- yt-dlp — Candidate media ingestion; youtube-dl is compatibility reference only.
- Composio — Staged external action/tool layer.
- LangGraph — Staged durable orchestration.
- ToolJet — Staged human operations cockpit and Agent & Capability Registry.

Optional capabilities do not become core requirements merely because they are available.

## Production validation

HiveForge v0.6.0 extends the hardened v0.5.0 control plane with guided onboarding. The production gate validates:

- package/version/status consistency;
- public/private and secret scans;
- onboarding documentation presence and safety boundaries;
- executable onboarding CLI behavior;
- user-profile and project-intake creation/no-overwrite behavior;
- ToolJet Compose configuration;
- fresh Linux, macOS and WSL installs;
- dashboard health smoke test;
- live Graphify fixture extraction and clustering;
- fallback without Graphify;
- package export/import round trips;
- acceptance evidence.

## Distribution

```bash
HIVEFORGE_REF=v0.6.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.6.0/install.sh | sh
```

Release artifacts include SHA-256 checksums.

---

**Unparalleled Source** — Reusable intelligence. Portable agents. Verified execution.
