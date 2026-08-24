# UNPS Workspace Hygiene & File Routing Workflow

Status: Candidate  
Version: 0.1.0

## Trigger
Use after meaningful file creation/import, during project hydration/synchronization, when a workspace becomes cluttered, when duplicate or stale artifacts appear, or when the correct client/project destination is uncertain.

## Workflow
1. **Resolve scope** — client, project/opportunity, internal initiative, and authoritative workspace.
2. **Inspect before creating** — find existing folders/files and avoid duplicate trees.
3. **Classify artifacts** — source, research, data, working, correspondence, decision, deliverable, admin, archive.
4. **Route** — move/create in the semantically correct location using the project's established structure.
5. **Normalize** — when repeated AI use is expected, create verified Markdown/text derivatives while preserving rich/original files.
6. **Name clearly** — human-readable title, meaningful identifier/date/status when needed.
7. **Dedupe** — identify competing copies; keep one canonical active version and archive superseded material.
8. **Refresh orientation** — update README/index/status when the change materially affects where humans should look.
9. **Refresh references** — update critical links/manifests when moves or replacements would otherwise break navigation.
10. **Capture learning** — if the cleanup exposed a recurring routing mistake, update the project/client learning record or routing rule.
11. **Human QA** — confirm a new team member can find the current source, working state, decisions, and final deliverables without this chat.

## No-Guess Rule
When destination confidence is low, stage the file in the project's existing intake area or `_NEEDS_ROUTING`; do not silently place it in a plausible but unverified client/project.

## Archive Rule
Archive for history; do not use archive as a dumping ground. Archived artifacts should retain enough naming/context to explain what they were and why they are no longer active.

## Completion Gate
A workspace pass is complete when:
- active files are in the correct project/client;
- no material duplicate competes with the source of truth;
- current/final status is recognizable;
- key links still work or are updated;
- heavy AI sources have efficient normalized forms when useful;
- humans can navigate the workspace without agent memory.
