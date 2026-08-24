# UNPS HiveForge — MCP and Connector Preferences

Version: 0.3.0  
Status: Candidate

## Required capability

The deployed agent needs read access to the canonical `PROMPTS.UNPS` workspace. Write access is required only when the user authorizes library maintenance or package changes.

## Routing order

1. Current project or authoritative local source
2. Connected system of record
3. Deterministic extraction or script
4. Lightweight public text retrieval
5. Web search for discovery and freshness
6. Structured crawler/extractor
7. Browser automation or visual inspection

## Preferred connectors

| Capability | Use | Status |
|---|---|---|
| Google Drive / Workspace | Canonical library discovery, reads, writes, collaboration | Required for Drive deployment |
| GitHub | Repository, skill, pattern, and dependency inspection | Conditional |
| Web/current research | Freshness, discovery, citations, official verification | Conditional |
| Firecrawl | Structured extraction or crawling | Conditional |
| Browser automation | Interactive, JavaScript, forms, authenticated workflows | Escalation only |
| Graphify CLI | Complex repository relationships and impact analysis | Optional candidate |
| Only-CLI `oc` | Known public text-first pages with low context overhead | Optional candidate |

## Connector rules

- Prefer first-party connected data for UNPS-owned files and records.
- Do not stack overlapping tools without a demonstrated evidence or reliability benefit.
- Treat connector output as evidence that may still require source verification.
- Never store credentials in this package.
- If a preferred connector is unavailable, use the closest capability-equivalent fallback and record material substitutions.

Canonical registry: `04_MCP_CONNECTORS/MCP_REGISTRY.md`.
