#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
BRAIN="$ROOT/10_CUSTOM_AGENTS/UNPS_HiveForge/BRAIN.md"
DEPS="$ROOT/10_CUSTOM_AGENTS/UNPS_HiveForge/DEPENDENCIES.md"

# Core package must validate without Graphify installed.
TMP=$(mktemp -d 2>/dev/null || mktemp -d -t hiveforge-fallback)
trap 'rm -rf "$TMP"' EXIT HUP INT TERM
HIVEFORGE_SOURCE_DIR="$ROOT" sh "$ROOT/install.sh" --target "$TMP/install" --bin-dir "$TMP/bin"
"$TMP/bin/hiveforge" doctor

# The policy must explicitly preserve a capability-equivalent fallback while
# keeping Graphify an optional Candidate dependency.
grep -q "If Graphify is unavailable" "$BRAIN"
grep -q "graphifyy==0.9.48" "$DEPS"
grep -q "CANDIDATE" "$DEPS"

printf '%s\n' "HiveForge fallback without Graphify: PASS"
