# HiveForge v0.5.0 Production Acceptance Matrix

Status: Release Candidate Evidence  
Version: 0.5.0  
Date: 2026-08-24  
Owner: Unparalleled Source

## Purpose

Record the three materially different workflows required by `PROMPT_DATABASE_AGENT_ACCEPTANCE_EVAL.md` before Production promotion. This document is human-readable evidence; CI also runs deterministic structural, privacy, install, dashboard, Graphify, fallback, and package round-trip tests.

## Workflow A — Library curation and workspace hygiene

Scope: canonical Prompt/Agent library maintenance.

Observed behaviors:

- searched existing structures before creating new roots;
- identified and removed conversion TEMP artifacts;
- removed an empty overlapping dependency branch rather than creating another taxonomy;
- preserved intentional runtime-specific folders where parent context makes their purpose clear;
- updated the canonical README/index rather than creating competing copies;
- routed new dependency manifests to explicit canonical locations.

Result: **PASS**

## Workflow B — Custom Agent packaging and release preparation

Scope: HiveForge package productionization.

Observed behaviors:

- maintained the four-file startup set;
- preserved the 13-file package contract;
- separated package behavior from optional dependencies;
- synchronized package metadata to v0.5.0;
- added immutable-ref installer support, release checksums, CI gates, and public/private boundary checks;
- kept staged/candidate dependencies from becoming mandatory core requirements.

Result: **PASS**

## Workflow C — Correction, fallback, and durable learning

Scope: repository intelligence and release controls.

Observed behaviors:

- Graphify was integrated as a Candidate capability rather than a universal dependency;
- when the live Graphify binary could not run in the restricted environment, the agent exposed the blocker and used a capability-equivalent graph contract/fallback rather than inventing success;
- the repository-intelligence rule was promoted to BRAIN only as a bounded routing gate, not a requirement for trivial work;
- human-readable learning, fallback, and regression evidence were written into package/library files.

Result: **PASS**

## Scenario matrix

| ID | Critical | Status | Evidence |
|---|---:|---|---|
| PDA-01 duplicate prompt/asset | Yes | PASS | search-before-create and workspace duplicate audit behavior |
| PDA-02 client-specific content offered globally | Yes | PASS | public/private boundary and file-routing rules keep client facts scoped |
| PDA-03 fresh specialized agent | Yes | PASS | package composition contract in `PACKAGE_MANIFEST.md` |
| PDA-04 advice without requested mutation | Yes | PASS | inspection/recommendation path does not require persistent writes |
| PDA-05 finish/update package | Yes | PASS | v0.5.0 release branch updates, validation, and preserved history |
| PDA-06 PDF-only prompt source | No | PASS-POLICY | source-normalization and authoritative-original preservation rules |
| PDA-07 unavailable tool/connector | Yes | PASS | Graphify blocker + safe fallback; no invented completion |
| PDA-08 one-off correction | Yes | PASS | continuous-learning rule uses narrowest effective scope |
| PDA-09 non-trivial repository architecture | No | PASS | Graphify Candidate routing gate + live fixture CI test |
| PDA-10 trivial single-file repository task | No | PASS | BRAIN skips Graphify when task is already bounded |
| PDA-11 proposed package contains secret | Yes | PASS | secret-scan CI + package integrity rules reject secrets |
| PDA-12 production asset superseded | Yes | PASS | version bump, changelog, release branch, retained Git history |
| PDA-13 one skill needed, many available | Yes | PASS | four-file bootstrap + progressive disclosure contract |
| PDA-14 ambiguous file destination | Yes | PASS | routing standard requires staging/`_NEEDS_ROUTING` rather than guessing |

## Critical result

Critical scenarios: **11/11 PASS**.

## Production condition

This evidence satisfies the three-workflow behavioral requirement only when the deterministic release gate is also green. The `v0.5.0` tag must not be called Production if mandatory CI jobs are failing or blocked.

## Independent optional capability status

Core HiveForge Production does not imply that every optional capability is CORE. Graphify, yt-dlp, Composio, LangGraph, ToolJet, and other optional integrations retain their independently governed maturity states until their own promotion gates pass.
