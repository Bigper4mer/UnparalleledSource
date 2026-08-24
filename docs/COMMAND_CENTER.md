# HiveForge Command Center

The Command Center is the built-in local operations dashboard for HiveForge.
It monitors commands run through HiveForge and accepts explicit lifecycle events
from compatible agent runtimes.

## Launch

```bash
hiveforge dashboard
```

The default address is `http://127.0.0.1:8744`. Use `--port` when that port is
already occupied:

```bash
hiveforge dashboard --port 8844
```

## Instrument a command

```bash
hiveforge run --task "Prompt library health check" -- your-command --flag
```

The wrapper records the start, safe heartbeat events, exit status, and duration.
It does not capture command output, prompt text, credentials, or environment
variables.

## Instrument an external agent

```bash
RUN_ID=$(hiveforge start "Normalize reusable proposal prompt" --phase "Inspecting sources")
hiveforge event "$RUN_ID" "Classifying" "Resolving scope and asset type"
hiveforge approval "$RUN_ID" "Promote prompt" "Canonical Drive write requires review"
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

Override it with `HIVEFORGE_STATE_DIR`. The store keeps at most 50 runs and 100
events per run.

## Security boundary

- The web server binds to localhost only.
- Dashboard mutations require a per-process session token.
- Cross-origin access is not enabled.
- Static assets use a restrictive Content Security Policy.
- Operators must keep summaries free of client-sensitive or regulated data.
- The dashboard does not make an arbitrary ChatGPT session observable; the host
  runtime must emit events through the HiveForge telemetry commands.

## ToolJet path

The event store is intentionally independent of the dashboard presentation.
When the approved PursuitOS ToolJet environment is available, the same lifecycle
contract can be moved behind PostgreSQL/REST without changing the agent status
model or operator approval states.
