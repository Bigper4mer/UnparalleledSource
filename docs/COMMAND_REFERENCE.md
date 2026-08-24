# HiveForge Command Reference

This page documents the commands shipped with the HiveForge v0.5.0 launcher and local runtime.

## Discovery commands

| Command | Purpose | Example |
|---|---|---|
| `hiveforge help` | Show command list | `hiveforge help` |
| `hiveforge version` | Print installed HiveForge version | `hiveforge version` |
| `hiveforge path` | Print installation directory | `hiveforge path` |
| `hiveforge doctor` | Verify all 13 required package files are present | `hiveforge doctor` |
| `hiveforge bootstrap` | Print the four-file startup sequence and next routing step | `hiveforge bootstrap` |

Recommended first five commands:

```bash
hiveforge doctor
hiveforge version
hiveforge path
hiveforge bootstrap
hiveforge help
```

## Command Center

### `hiveforge dashboard`

Starts the localhost-only Command Center.

```bash
hiveforge dashboard
```

Useful server options supported by the dashboard script can be passed after the command:

```bash
hiveforge dashboard --no-open
hiveforge dashboard --port 8744 --no-open
hiveforge dashboard --verbose
```

The server accepts localhost interfaces only.

## Instrumented commands

### `hiveforge run`

Wrap an ordinary command with HiveForge run telemetry.

```bash
hiveforge run --task "Run the test suite" -- npm test
```

```bash
hiveforge run --task "Generate report" -- python3 report.py
```

The wrapped command's stdout/stderr remains the command's own output. HiveForge stores sanitized run state and heartbeat metadata rather than the command body or output.

### `hiveforge status`

Show current or most recent run:

```bash
hiveforge status
```

Machine-readable state:

```bash
hiveforge status --json
```

## External instrumentation commands

These are useful when a coding harness, workflow runner, or custom integration wants to report activity to HiveForge without using `hiveforge run`.

### Start a run

```bash
RUN_ID=$(hiveforge start "Prepare customer proposal")
```

Optional starting phase:

```bash
RUN_ID=$(hiveforge start "Prepare customer proposal" --phase "Source review")
```

### Record an event

Syntax:

```text
hiveforge event RUN_ID PHASE SUMMARY [--type EVENT_TYPE]
```

Example:

```bash
hiveforge event "$RUN_ID" "Research" "Validated primary sources"
```

Heartbeat-style event:

```bash
hiveforge event "$RUN_ID" "Executing" "Still running" --type heartbeat
```

### Finish a run

Completed:

```bash
hiveforge finish "$RUN_ID" completed "Deliverable verified"
```

Failed:

```bash
hiveforge finish "$RUN_ID" failed "Build failed during verification"
```

Allowed final statuses are `completed` and `failed`.

## Approval commands

### Request approval

```bash
APPROVAL_ID=$(hiveforge approval "$RUN_ID" \
  "Publish deliverable" \
  "Final document is ready for release")
```

The run moves to `waiting_approval`.

### Approve

```bash
hiveforge decide "$APPROVAL_ID" approve
```

### Deny

```bash
hiveforge decide "$APPROVAL_ID" deny
```

Consequential actions should be wired so the action occurs **after** approval, not before it.

## Connector health

Syntax:

```text
hiveforge connector NAME STATUS
```

Allowed statuses:

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

Connector status is operational telemetry; it does not establish authorization or credentials.

## Complete command map

```text
hiveforge
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
├── path
├── version
└── help
```

## Common copy/paste sequences

### Confirm installation

```bash
hiveforge doctor && hiveforge version && hiveforge bootstrap
```

### Open the dashboard without launching a browser automatically

```bash
hiveforge dashboard --no-open
```

### Instrument a real task

```bash
hiveforge run --task "Repository tests" -- sh -c 'npm test'
```

### See the full runtime state

```bash
hiveforge status --json
```

### Manually instrument a multi-step workflow

```bash
RUN_ID=$(hiveforge start "Example multi-step workflow" --phase "Intake")
hiveforge event "$RUN_ID" "Research" "Relevant evidence collected"
hiveforge event "$RUN_ID" "Verification" "Output checks passed"
hiveforge finish "$RUN_ID" completed "Workflow complete"
```

## HiveForge conversation commands

HiveForge also uses **workflow-language commands** such as `/brainstorm`, `/spec`, `/tickets`, `/plan`, `/implement`, `/review`, `/verify`, `/research`, `/diagram`, `/readme`, and `/retro` as routing conventions inside an agent conversation.

These are not necessarily shell executables. They tell the agent which operating mode you want.

Examples:

```text
/brainstorm Review this architecture and give me options. Do not change files.
```

```text
/research Determine the current vendor landscape and cite primary sources.
```

```text
/implement Execute the approved plan, run targeted tests, then verify.
```

```text
/retro Extract only reusable lessons from what went wrong and what worked.
```

See [`WORKFLOW_GUIDE.md`](WORKFLOW_GUIDE.md) for when to use each mode.