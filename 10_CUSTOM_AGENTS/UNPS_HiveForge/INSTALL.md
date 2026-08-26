# Install UNPS HiveForge

Version: 0.7.0
Status: Production

## Production install

For the immutable v0.7.0 release tag:

```bash
HIVEFORGE_REF=v0.7.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.7.0/install.sh | sh
```

The installer places the package under the user's local data directory, creates a `hiveforge` launcher under `~/.local/bin`, validates the required agent and onboarding files, and refuses to silently overwrite an existing installation.

## First run

```bash
hiveforge doctor
hiveforge version
hiveforge onboard
```

`hiveforge onboard` prints a copy/paste startup prompt that guides the agent through minimum useful intake, current-project inspection, workflow recommendation, first-task execution, verification, and scoped learning.

Useful optional setup:

```bash
hiveforge profile-init
hiveforge project-init
hiveforge docs
hiveforge dashboard
```

- `profile-init` creates a human-readable working-preference template and refuses to overwrite an existing profile.
- `project-init` creates an optional project-intake file only when the user explicitly requests it; reuse an established README/status/ADR system when one already exists.
- `dashboard` launches the localhost Command Center.

## Release verification

Download the release archive and `SHA256SUMS`, then verify before installation when using a packaged release artifact.

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
HIVEFORGE_REF=v0.7.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.7.0/install.sh \
  | sh -s -- --target /absolute/path/to/hiveforge
```

Existing installations are never silently overwritten. Use `--force` to preserve the existing installation as a timestamped backup before installing.

## Option A — Connected workspace deployment

1. Create or open a compatible agent environment.
2. Provide only authorized access to the relevant project/library sources.
3. Load `BRAIN.md`, `AGENT.md`, `SYSTEM_INSTRUCTIONS.md`, and `PACKAGE_MANIFEST.md`.
4. Run the first-use intake or load an already validated user working profile.
5. Resolve current client/project/internal scope and source of truth.
6. Keep all other skills, workflows, connectors, and dependencies reference-only until a task triggers them.
7. Run validation before consequential changes.

## Option B — Portable offline subset

1. Download this package folder as Markdown/plain text.
2. Download only shared skills, workflows, connector profiles, and schemas required for the intended deployment.
3. Preserve canonical folder names or deliberately update manifest references.
4. Configure model/harness mappings for the destination environment.
5. Do not bundle credentials or client data.
6. Run `hiveforge doctor` and the applicable acceptance tests.

## Optional ToolJet cockpit

ToolJet is STAGED and not required for core HiveForge.

```bash
hiveforge tooljet status
hiveforge tooljet config
hiveforge tooljet up
hiveforge tooljet url
```

The evaluation stack requires Docker + Docker Compose v2 and defaults to `http://localhost:8080`. Keep canonical policy, authorization, and source-of-truth state outside ToolJet UI logic.

## Validation

Confirm that HiveForge can:

- identify the canonical source of truth;
- distinguish user preferences from project/client facts;
- search before creating duplicate assets or project roots;
- resolve project/client scope before persistent writes;
- recommend the smallest appropriate workflow;
- load only task-relevant assets;
- preserve authoritative originals and version history;
- apply tool authorization boundaries;
- produce a concise verification/change report;
- route a reusable correction through the learning loop;
- fail safely when a connector, dependency, or destination is unavailable.

Use `09_TESTS_EVALS/Prompt_Tests/PRODUCTION_ACCEPTANCE_MATRIX_v0.7.0.md` for the guided-onboarding production evidence.

## Optional Graphify setup

Graphify is not required for core HiveForge operation. For sufficiently complex repositories only:

```bash
python3 -m pip install graphifyy==0.9.48
graphify install --project --platform codex
graphify .
graphify cluster-only .
```

Graphify remains a Candidate capability even when HiveForge v0.7.0 is Production. Its promotion gate is independent.
