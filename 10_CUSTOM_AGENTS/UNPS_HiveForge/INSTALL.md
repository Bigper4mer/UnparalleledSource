# Install UNPS HiveForge

Version: 0.5.0  
Status: Release Candidate

## Production install

For the immutable v0.5.0 release tag:

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh | sh
```

The installer places the package under the user's local data directory, creates a `hiveforge` launcher under `~/.local/bin`, validates all 13 required agent files, and refuses to silently overwrite an existing installation.

After installation:

```bash
hiveforge doctor
hiveforge bootstrap
```

Launch the local Agent Command Center:

```bash
hiveforge dashboard
```

Python 3 is optional for the core package and required for dashboard and runtime telemetry commands. The dashboard binds to localhost and does not send run state to a cloud service.

## Release verification

Download the release archive and `SHA256SUMS`, then verify the checksum before installation when using a packaged release artifact.

Linux:

```bash
sha256sum -c SHA256SUMS
```

macOS:

```bash
shasum -a 256 -c SHA256SUMS
```

## Custom target

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh \
  | sh -s -- --target /absolute/path/to/hiveforge
```

Existing installations are never silently overwritten. Use `--force` to preserve the existing installation as a timestamped backup before installing.

## Option A — Connected Drive deployment

1. Create or open a compatible Custom Agent environment.
2. Provide read access to the `PROMPTS.UNPS` Drive folder.
3. Load `BRAIN.md`, `AGENT.md`, `SYSTEM_INSTRUCTIONS.md`, and `PACKAGE_MANIFEST.md`.
4. Configure the Google Drive/Workspace connector with minimum required permissions.
5. Keep all other skills, workflows, connectors, and dependencies reference-only until a task triggers them.
6. Run validation.

## Option B — Portable offline subset

1. Download this package folder as Markdown/plain text.
2. Download only shared skills, workflows, connector profiles, and schemas required for the intended deployment.
3. Preserve canonical folder names or deliberately update manifest references.
4. Configure model/harness mappings for the destination environment.
5. Do not bundle credentials or client data.
6. Run validation.

## Validation

Confirm that the agent can:

- identify `PROMPTS.UNPS` as the canonical internal library;
- distinguish prompts, skills, workflows, connectors, dependencies, schemas, evaluations, and Custom Agent builds;
- search before creating duplicate assets;
- resolve project/client scope before persistent writes;
- load only task-relevant assets;
- preserve authoritative originals and version history;
- apply tool authorization boundaries;
- produce a concise change report;
- route a reusable correction through the learning loop;
- fail safely when a connector, dependency, or destination is unavailable.

Use `09_TESTS_EVALS/Prompt_Tests/PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md` and `PRODUCTION_ACCEPTANCE_MATRIX_v0.5.0.md` for production evidence.

## Optional Graphify setup

Graphify is not required for core HiveForge operation. For a sufficiently complex code repository only:

```bash
python3 -m pip install graphifyy==0.9.48
graphify install --project --platform codex
graphify .
```

Graphify remains a Candidate capability even when the core HiveForge v0.5.0 package is Production. Its own promotion gate is independent.
