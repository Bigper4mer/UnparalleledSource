# HiveForge Command Center

The Command Center is the built-in local operations dashboard for HiveForge. It monitors commands run through HiveForge and accepts explicit lifecycle events from compatible agent runtimes.

If you are new to HiveForge, start with [`GETTING_STARTED.md`](GETTING_STARTED.md). For all runtime command syntax, use [`COMMAND_REFERENCE.md`](COMMAND_REFERENCE.md).

## Launch

```bash
hiveforge dashboard
```

The default address is:

```text
http://127.0.0.1:8744
```

Use another port when needed:

```bash
hiveforge dashboard --port 8844
```

Avoid opening the browser automatically:

```bash
hiveforge dashboard --no-open
```

## Instrument a command

```bash
hiveforge run --task "Prompt library health check" -- your-command --flag
```

The wrapper records start, safe heartbeat events, exit status and duration. It does not capture command output, prompt text, credentials or environment variables.

Example:

```bash
hiveforge run --task "Repository tests" -- npm test
```

## Inspect state

```bash
hiveforge status
hiveforge status --json
```

## Instrument an external agent

```bash
RUN_ID=$(hiveforge start "Normalize reusable proposal prompt" --phase "Inspecting sources")
hiveforge event "$RUN_ID" "Classifying" "Resolving scope and asset type"
APPROVAL_ID=$(hiveforge approval "$RUN_ID" "Promote prompt" "Canonical write requires review")
hiveforge decide "$APPROVAL_ID" approve
hiveforge finish "$RUN_ID" completed "Prompt validated and routed"
```

Report connector health explicitly:

```bash
hiveforge connector "Google Drive" connected
hiveforge connector "GitHub" connected
```

## Data location

Runtime state is stored at:

```text
${XDG_STATE_HOME:-$HOME/.local/state}/unps-hiveforge/state.json
```

Override it with `HIVEFORGE_STATE_DIR`. The store keeps at most 50 runs and 100 events per run.

## Security boundary

- The web server binds to localhost only.
- Dashboard mutations require a per-process session token.
- Cross-origin access is not enabled.
- Static assets use a restrictive Content Security Policy.
- Operators must keep summaries free of client-sensitive or regulated data.
- The dashboard does not make an arbitrary AI session observable; the host runtime must emit events through HiveForge telemetry commands.

## Command Center vs ToolJet

Use the **Command Center** when:

- you are one user or a small local team;
- you want immediate run/approval/connector visibility;
- you do not need a shared governed capability registry.

Use the optional **ToolJet cockpit** when:

- several users need a shared view;
- you need agent/capability/dependency/test registries;
- you need a controlled promotion queue and role-aware review;
- you want a visual routing simulator.

The two interfaces should use the same underlying lifecycle concepts. ToolJet does not become the canonical source of BRAIN or project truth.

See [`TOOLJET_SETUP.md`](TOOLJET_SETUP.md) for deployment and registry guidance.
