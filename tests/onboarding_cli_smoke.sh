#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TMP=$(mktemp -d 2>/dev/null || mktemp -d -t hiveforge-onboarding)
trap 'rm -rf "$TMP"' EXIT HUP INT TERM

INSTALL="$TMP/install"
BIN="$TMP/bin"
PROFILE="$TMP/user/USER_PROFILE.md"
PROJECT="$TMP/project/HIVEFORGE_PROJECT.md"
mkdir -p "$TMP/project"

HIVEFORGE_SOURCE_DIR="$ROOT" sh "$ROOT/install.sh" --target "$INSTALL" --bin-dir "$BIN"

HF="$BIN/hiveforge"
"$HF" doctor
[ "$("$HF" version)" = "0.7.0" ]

"$HF" bootstrap | grep -q "hiveforge onboard"
"$HF" onboard > "$TMP/onboard.txt"
grep -q "COPY / PASTE INTO YOUR AGENT" "$TMP/onboard.txt"
grep -qi "startup intake" "$TMP/onboard.txt"

"$HF" docs > "$TMP/docs.txt"
grep -q "GETTING_STARTED.md" "$TMP/docs.txt"
grep -q "WORKFLOW_GUIDE.md" "$TMP/docs.txt"

"$HF" profile-init "$PROFILE"
test -s "$PROFILE"
if "$HF" profile-init "$PROFILE" >/dev/null 2>&1; then
  echo "profile-init unexpectedly overwrote an existing profile" >&2
  exit 1
fi

grep -qi "working" "$PROFILE"
grep -qi "password" "$PROFILE"

"$HF" project-init "$PROJECT"
test -s "$PROJECT"
if "$HF" project-init "$PROJECT" >/dev/null 2>&1; then
  echo "project-init unexpectedly overwrote an existing project intake" >&2
  exit 1
fi

grep -qi "source of truth" "$PROJECT"

"$HF" tooljet status > "$TMP/tooljet.txt"
grep -qi "STAGED" "$TMP/tooljet.txt"
[ "$("$HF" tooljet url)" = "http://localhost:8080" ]

printf '%s\n' "HiveForge guided onboarding CLI: PASS"
