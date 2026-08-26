# HiveForge Command Reference

This page documents the commands shipped with the HiveForge v0.7.0 launcher and local runtime.

## Recommended first commands

```bash
hiveforge doctor
hiveforge version
hiveforge onboard
hiveforge docs
```

## Guided onboarding commands

| Command | Purpose | Example |
|---|---|---|
| `hiveforge onboard` | Print the copy/paste first-run intake and startup workflow | `hiveforge onboard` |
| `hiveforge docs` | Show installed documentation paths | `hiveforge docs` |
| `hiveforge profile-init [PATH]` | Create a human-readable user working-profile template; refuses overwrite | `hiveforge profile-init` |
| `hiveforge project-init [PATH]` | Create an optional project-intake template; refuses overwrite | `hiveforge project-init ./HIVEFORGE_PROJECT.md` |

Default user profile path:

```text
~/.config/unps-hiveforge/USER_PROFILE.md
```

`project-init` is intentionally optional. Reuse an established README/status/ADR/project-state system when one already exists.

## Discovery and validation

| Command | Purpose |
|---|---|
| `hiveforge help` | Show command list |
| `hiveforge version` | Print installed HiveForge version |
| `hiveforge path` | Print installation directory |
| `hiveforge doctor` | Verify package and guided-onboarding assets |
| `hiveforge bootstrap` | Print startup sequence and routing guidance |

## Command Center

### `hiveforge dashboard`

Starts the localhost-only Command Center.

```bash
hiveforge dashboard
hiveforge dashboard --no-open
hiveforge dashboard --port 8844 --no-open
hiveforge dashboard --verbose
```

The server accepts localhost interfaces only.

## Instrumented commands

### `hiveforge run`

Wrap an ordinary command with HiveForge run telemetry.

```bash
hiveforge run --task "Run the test suite" -- npm test
```

The wrapped command owns its stdout/stderr. HiveForge stores sanitized run state and heartbeat metadata rather than command output or prompt content.

### `hiveforge status`

```bash
hiveforge status
hiveforge status --json
```

## External instrumentation

### Start

```bash
RUN_ID=$(hiveforge start "Prepare proposal" --phase "Source review")
```

### Event

```bash
hiveforge event "$RUN_ID" "Research" "Validated primary sources"
hiveforge event "$RUN_ID" "Executing" "Heartbeat" --type heartbeat
```

Syntax:

```text
hiveforge event RUN_ID PHASE SUMMARY [--type EVENT_TYPE]
```

### Finish

```bash
hiveforge finish "$RUN_ID" completed "Deliverable verified"
hiveforge finish "$RUN_ID" failed "Verification failed"
```

Allowed final statuses: `completed`, `failed`.

## Approval commands

Request:

```bash
APPROVAL_ID=$(hiveforge approval "$RUN_ID" \
  "Publish deliverable" \
  "Final document is ready for release")
```

Decide:

```bash
hiveforge decide "$APPROVAL_ID" approve
hiveforge decide "$APPROVAL_ID" deny
```

Consequential actions should occur **after** approval, not before it.

## Connector health

```text
hiveforge connector NAME STATUS
```

Statuses:

```text
connected
degraded
offline
unknown
```

Examples:

```bash
hiveforge connector "Google Drive" connected
hiveforge connector "GitHub" connected
hiveforge connector "ToolJet" unknown
```

Operational status does not grant authorization.

## Optional ToolJet commands

ToolJet is a STAGED team cockpit, not a core dependency.

```bash
hiveforge tooljet status
hiveforge tooljet config
hiveforge tooljet up
hiveforge tooljet url
hiveforge tooljet down
```

Behavior:

| Command | Result |
|---|---|
| `status` | Explain maturity, compose path, commands and guide |
| `config` | Validate/render Docker Compose configuration |
| `up` | Start local evaluation stack |
| `url` | Print `http://localhost:8080` |
| `down` | Stop/remove local evaluation stack |

`config`, `up`, and `down` require Docker + Docker Compose v2.

## Complete command map

```text
hiveforge
├── onboard
├── docs
├── profile-init [PATH]
├── project-init [PATH]
├── doctor
├── bootstrap
├── dashboard
├── run
├── status
├── start
├── event
├── finish
├── approval
├── decide
├── connector
├── tooljet
│   ├── status
│   ├── config
│   ├── up
│   ├── url
│   └── down
├── path
├── version
└── help
```

## Copy/paste sequences

### First-time user

```bash
hiveforge doctor && hiveforge version
hiveforge onboard
```

### Create optional human-readable user context

```bash
hiveforge profile-init
```

### Start from an existing project

```bash
hiveforge bootstrap
hiveforge docs
```

Then ask the loaded agent to inspect the existing project before creating any state file.

### Project without useful intake/status state

```bash
hiveforge project-init
```

### Local dashboard

```bash
hiveforge dashboard --no-open
```

### Real command telemetry

```bash
hiveforge run --task "Repository tests" -- npm test
```

### Full runtime state

```bash
hiveforge status --json
```

### Manual multi-step run

```bash
RUN_ID=$(hiveforge start "Example workflow" --phase "Intake")
hiveforge event "$RUN_ID" "Research" "Relevant evidence collected"
hiveforge event "$RUN_ID" "Verification" "Checks passed"
hiveforge finish "$RUN_ID" completed "Workflow complete"
```

### Optional shared cockpit

```bash
hiveforge tooljet config
hiveforge tooljet up
hiveforge tooljet url
```

## Conversation workflow commands

HiveForge also uses workflow-language commands inside an agent conversation. These are routing conventions, not necessarily shell executables.

| Conversation command | Intent |
|---|---|
| `/brainstorm` | Explore options without changing files |
| `/spec` | Turn intent into a durable definition |
| `/tickets` | Break settled work into bounded slices |
| `/plan` | Sequence execution |
| `/implement` | Execute approved work |
| `/review` | Critique independently |
| `/verify` | Prove completion |
| `/research` | Research current/uncertain facts |
| `/diagram` | Choose/render the right system view |
| `/readme` | Improve repository onboarding/documentation |
| `/retro` | Extract reusable learning |

Examples:

```text
/brainstorm Review this architecture. Give me options and trade-offs. Do not change files.
```

```text
/research Determine the current vendor landscape using authoritative sources and cite the evidence.
```

```text
/implement Execute the approved plan, run targeted tests, then verify.
```

```text
/retro Extract only reusable lessons from what failed and what worked.
```

See [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) for recommended inputs, outputs and triggers.
