# Install UNPS HiveForge

Version: 0.3.1  
Status: Candidate

## One-command installation

macOS, Linux, or WSL:

```bash
curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/main/install.sh | sh
```

The installer places the package under the user's local data directory, creates a `hiveforge` launcher under `~/.local/bin`, and validates all 13 required agent files.

After installation:

```bash
hiveforge doctor
hiveforge bootstrap
```

Custom target:

```bash
curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/main/install.sh \
  | sh -s -- --target /absolute/path/to/hiveforge
```

Existing installations are never silently overwritten. Use `--force` to preserve the existing installation as a timestamped backup before installing.

## Option A — Connected Drive deployment

1. Create or open a compatible Custom Agent environment.
2. Provide read access to the `PROMPTS.UNPS` Drive folder.
3. Load `BRAIN.md`, `AGENT.md`, `SYSTEM_INSTRUCTIONS.md`, and `PACKAGE_MANIFEST.md`.
4. Configure the Google Drive/Workspace connector with the minimum required permissions.
5. Keep all other skills, workflows, connectors, and dependencies reference-only until a task triggers them.
6. Run the validation checks below.

## Option B — Portable offline subset

1. Download this package folder as Markdown/plain text.
2. Download only the shared skills, workflows, connector profiles, and schemas required for the intended deployment.
3. Preserve the canonical folder names or update manifest references deliberately.
4. Configure model/harness mappings for the destination environment.
5. Do not bundle credentials or client data.
6. Run validation.

## Validation

Confirm that the agent can:

- identify `PROMPTS.UNPS` as the canonical library;
- distinguish prompts, skills, workflows, connectors, dependencies, schemas, evaluations, and Custom Agent builds;
- search before creating duplicate assets;
- resolve project/client scope before persistent writes;
- load only task-relevant assets;
- preserve authoritative originals and version history;
- apply tool authorization boundaries;
- produce a concise change report;
- route a reusable correction through the learning loop;
- fail safely when a connector, dependency, or destination is unavailable.

Use `09_TESTS_EVALS/Prompt_Tests/PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md` for the complete scenario set.

## Optional Graphify setup

Graphify is not required for Drive curation. For a sufficiently complex code repository only:

```bash
uv tool install graphifyy==0.9.48
graphify install --project --platform codex
graphify .
```

Keep Graphify at Candidate status until the live promotion gate in `GRAPHIFY_CAPABILITY.md` passes.
