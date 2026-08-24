# Security Policy

## Public repository boundary

This repository is a public architecture and example surface. Do not commit:

- credentials, API keys, tokens, private keys, or connection strings;
- client, partner, solicitation, pricing, or opportunity data not approved for publication;
- regulated, medical, legal, financial, HR, or personally identifiable information;
- private prompts, proprietary workflows, or internal system instructions;
- connector exports, logs, environment files, or hidden memory;
- unreviewed third-party prompt packs or executable integrations.

## Integration review

Before adding a model, package, repository, plugin, MCP server, connector, or external service, review:

1. Permissions and data access
2. Authentication and secret handling
3. External network behavior
4. Maintenance and release activity
5. Licensing
6. Prompt-injection and untrusted-content exposure
7. Context and operating cost
8. Overlap with safer built-in capabilities

## Reporting

Do not open a public issue containing a vulnerability, credential, private configuration, or sensitive evidence. Report sensitive findings through an approved private Unparalleled Source communication channel.

## Supported status

HiveForge is currently Candidate software. Security-sensitive deployment decisions require environment-specific review and least-privilege configuration.

## Command Center telemetry

The built-in dashboard binds to `127.0.0.1` and does not expose a public network
listener. Approval mutations require an in-memory session token and the dashboard
does not enable cross-origin access. Telemetry must contain short, sanitized
summaries only. Never record prompt bodies, command output, environment variables,
credentials, client evidence, regulated data, or private file contents.
