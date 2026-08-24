# HiveForge Troubleshooting

Use this page when installation, routing, telemetry, tools or learning behavior does not match expectations.

## `hiveforge: command not found`

The installer normally creates a launcher under:

```text
~/.local/bin/hiveforge
```

Check:

```bash
ls -l ~/.local/bin/hiveforge
```

If `~/.local/bin` is not on PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then:

```bash
hiveforge doctor
```

The installer also prints the direct launcher path.

## `hiveforge doctor` fails

Run:

```bash
hiveforge path
```

Confirm the package contains the required files under:

```text
10_CUSTOM_AGENTS/UNPS_HiveForge/
```

Do not manually recreate missing files from memory. Reinstall from a trusted immutable release or restore the missing package content.

## Existing installation blocks reinstall

HiveForge refuses silent overwrite.

To preserve the current installation as a timestamped backup and reinstall:

```bash
HIVEFORGE_REF=v0.6.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.6.0/install.sh \
  | sh -s -- --force
```

## `hiveforge onboard` does not print the first-run prompt

Run:

```bash
hiveforge doctor
hiveforge docs
```

Confirm `examples/FIRST_RUN_PROMPT.md` exists inside the installation. Reinstall from the immutable release if it is missing.

## `profile-init` or `project-init` refuses to run

This is expected when the target file already exists. HiveForge intentionally refuses silent overwrite.

Use a different explicit path or edit the existing human-readable file.

## Dashboard does not open

Start without automatic browser launch:

```bash
hiveforge dashboard --no-open
```

Then open:

```text
http://127.0.0.1:8744
```

If the port is occupied:

```bash
hiveforge dashboard --port 8844 --no-open
```

Check runtime state:

```bash
hiveforge status --json
```

## Python is missing

Core HiveForge agent files and guided onboarding can still be used. Python 3 is required for the local Command Center and runtime telemetry commands.

## Graphify is unavailable

This should **not** block core HiveForge operation.

Fallback sequence:

```text
project instructions
→ repository search
→ exact relevant files
→ tests/build/runtime evidence
```

Install the tested candidate only when repository graph intelligence is justified:

```bash
python3 -m pip install graphifyy==0.9.48
```

## Graphify generated only `graph.json`

Run clustering after extraction:

```bash
graphify .
graphify cluster-only .
```

Then inspect:

```text
graphify-out/graph.json
graphify-out/GRAPH_REPORT.md
graphify-out/graph.html
```

## A connector is unavailable

HiveForge should choose a capability-equivalent fallback or state the blocker. Do not pretend a connected-system read or mutation succeeded when the connector was unavailable.

Useful telemetry:

```bash
hiveforge connector "Google Drive" degraded
hiveforge connector "GitHub" connected
```

## The agent is asking too many onboarding questions

Tell it:

```text
Use progressive HiveForge intake. Ask only what is necessary for the current task and retrieve anything available from authorized project sources before asking me to repeat it.
```

Returning users should receive a delta check rather than a full interview.

## The agent is too terse or too technical

```text
For this workflow, treat me as Guided. Explain terminology and give exact copy/paste commands.
```

or:

```text
For this repository task, treat me as Expert. Skip introductory explanations and focus on architecture, evidence, commands and trade-offs.
```

## HiveForge stored the wrong kind of learning

Use:

```text
Correct this learning at the narrowest appropriate scope. Remove the global/user-level assumption if it is project-specific or one-off, record the corrected rule in human-readable state, and add a regression guard only if the pattern is durable.
```

Learning should move gradually:

```text
task → project → user/account → reusable skill/workflow → BRAIN
```

## Files are being routed incorrectly

```text
Stop persistent writes. Resolve organization, client/account or Internal scope, project, artifact class, authority/status and lifecycle. Search for the established workspace before creating anything. If routing remains ambiguous, stage rather than guess.
```

## Duplicate folders or state files appeared

```text
Inspect the existing workspace, identify duplicate/competing roots and state files, determine the current canonical structure, propose a consolidation plan, and preserve history before moving or archiving anything.
```

## ToolJet commands fail

Check:

```bash
hiveforge tooljet status
```

`tooljet config`, `up`, and `down` require Docker + Docker Compose v2.

Validate:

```bash
docker compose version
hiveforge tooljet config
```

ToolJet remains optional and STAGED; its failure must not block core HiveForge.

## ToolJet is running but the HiveForge registry is empty

ToolJet itself does not automatically become the HiveForge registry. You still need the normalized registry backend/views described in [TOOLJET_SETUP.md](TOOLJET_SETUP.md) and the implementation contract under `05_WORKFLOWS/Agent_Control_Plane/TOOLJET_AGENT_CAPABILITY_REGISTRY.md`.

Verify:

1. registry source data exists;
2. read datasource is connected;
3. queries return rows;
4. canonical paths are resolvable;
5. role permissions allow the current user to read them.

## ToolJet should not be required for a solo setup

Correct. Minimum usable stack:

```text
HiveForge package
+ AI environment/harness
+ authorized project sources
```

The local Command Center is optional. ToolJet is an advanced shared cockpit.

## WSL shell errors or strange `set` failures

Ensure repository shell scripts use LF line endings. HiveForge's `.gitattributes` enforces LF for shell/runtime text files. Convert manually copied CRLF scripts before running them inside WSL.

## I do not know what workflow to use

```text
Inspect my goal and current state, then recommend the smallest HiveForge workflow. Explain why, what inputs you already have, what you still need, which tools you would load, and what the verification gate will be.
```

Or consult [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md).

## Reporting a problem

Include:

```text
HiveForge version
OS / environment
command or workflow
expected result
actual result
reproduction steps
relevant non-sensitive logs
whether optional tools were installed
```

Never paste credentials, auth cookies, private client data or secrets into public issue reports.
