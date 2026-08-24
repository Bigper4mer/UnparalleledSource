# Composio Staging Profile

Status: STAGED  
Owner: Unparalleled Source  
Validated against upstream: 2026-08-24

## Role

Optional action/tool layer for agents that need runtime discovery, authentication, and execution across external applications. Composio must not replace native connected tools that already satisfy the task with lower complexity or risk.

## Current upstream signals

The current Composio SDK repository exposes TypeScript and Python SDKs, a CLI, provider adapters, per-user sessions, runtime tool discovery, authentication, triggers, sandboxing, and optional hosted MCP session endpoints.

## Preferred integration

Use session-scoped discovery rather than injecting hundreds of tool schemas into every prompt.

### TypeScript

```bash
npm install @composio/core @composio/openai-agents @openai/agents
```

### Python

```bash
pip install composio composio-openai-agents openai-agents
```

Required secret placeholder: `COMPOSIO_API_KEY`. Never store the real key in Markdown, source control, prompts, ToolJet exports, or logs.

## Routing policy

Use Composio when:

- the needed external app is not available through a native/approved connector;
- dynamic tool discovery materially reduces context cost;
- a per-user authenticated session is required;
- a hosted MCP surface is useful across multiple harnesses.

Do not use Composio merely because it has a toolkit for an app already covered by a safer native connector.

## Initial pilot scope

Pilot one isolated non-destructive workflow with a test/least-privilege account:

1. create a user-scoped session;
2. restrict toolkits to minimum required apps;
3. discover tools at runtime;
4. execute read-only or draft-only actions first;
5. verify audit/logging behavior;
6. test auth expiry/reconnect and denied actions;
7. confirm no broad tool schema dump enters normal context.

## Security gate

Before CORE promotion verify account isolation, least-privilege toolkits, auth lifecycle, sensitive log handling, network behavior, prompt-injection boundaries, approval gates for consequential writes, and fallback behavior.

## BRAIN integration

Classification: STAGED. BRAIN may recommend Composio when a capability gap exists, but must not auto-promote or auto-connect accounts.
