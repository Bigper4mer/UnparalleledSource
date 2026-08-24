# LangGraph Staging Profile

Status: STAGED  
Owner: Unparalleled Source  
Validated against upstream: 2026-08-24

## Role

Optional durable orchestration layer for long-running, stateful, resumable agent workflows that need checkpoints, human-in-the-loop interrupts, explicit state transitions, or recovery across process/session failures.

## Routing policy

Use LangGraph when at least one of these is material:

- workflow duration requires durable state;
- restart/resume after failure is a business requirement;
- explicit approval/interrupt points are required;
- branching/parallel stateful workflows need inspectable transitions;
- a workflow must be replayed/audited from checkpoints;
- agent state cannot safely live only in one model conversation.

Do not use LangGraph for bounded one-shot tasks, simple scripts, or workflows already handled reliably by deterministic automation.

## Install

```bash
pip install -U langgraph
```

Use a project-local environment and pin the exact tested version at CORE promotion.

## UNPS state boundary

LangGraph runtime state is operational state, not the sole canonical business record. Durable project meaning remains human-readable in files such as `STATUS.md`, `TASKS.md`, `DECISIONS.md`, `LEARNINGS.md`, ADRs, and authoritative databases/Drive sources.

## Initial pilot

Pilot one low-risk workflow with four explicit nodes:

`intake → retrieve → human approval → finalize`

Required test conditions:

1. run to approval interrupt;
2. persist checkpoint/state;
3. terminate the process/session;
4. resume without redoing completed work;
5. approve or modify state through the human gate;
6. finish and write a human-readable completion artifact;
7. simulate a tool failure and verify bounded retry/fallback;
8. verify hidden state is not required to reconstruct the business outcome.

## Security / reliability gate

Before CORE promotion verify state serialization, checkpoint access controls, bounded/idempotent retries, approval for destructive actions, state-schema migration, timeout/cancellation paths, and protection of canonical client/project records.

## BRAIN integration

Classification: STAGED. BRAIN may select LangGraph only when durable state materially improves reliability. Capability-equivalent orchestration may substitute.
