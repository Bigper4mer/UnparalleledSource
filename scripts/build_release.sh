#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
VERSION=$(awk '/^version:/ { print $2; exit }' "$ROOT/10_CUSTOM_AGENTS/UNPS_HiveForge/AGENT.md")
[ -n "$VERSION" ] || { echo "Unable to resolve HiveForge version" >&2; exit 1; }

DIST="$ROOT/dist"
STAGE="$DIST/unps-hiveforge-v$VERSION"
ARCHIVE="$DIST/unps-hiveforge-v$VERSION.tar.gz"

rm -rf "$DIST"
mkdir -p "$STAGE"

for item in \
  00_README \
  03_SKILLS \
  04_MCP_CONNECTORS \
  05_WORKFLOWS \
  06_DEPENDENCIES \
  09_TESTS_EVALS \
  10_CUSTOM_AGENTS \
  schemas \
  examples \
  docs \
  dashboard \
  bin \
  README.md \
  LICENSE \
  SECURITY.md \
  DRIVE_SYNC_MANIFEST.md \
  install.sh; do
  [ ! -e "$ROOT/$item" ] || cp -R "$ROOT/$item" "$STAGE/"
done

find "$STAGE" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
find "$STAGE" -name '*.pyc' -type f -delete 2>/dev/null || true

tar -czf "$ARCHIVE" -C "$DIST" "unps-hiveforge-v$VERSION"

cd "$DIST"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$(basename "$ARCHIVE")" > SHA256SUMS
elif command -v shasum >/dev/null 2>&1; then
  shasum -a 256 "$(basename "$ARCHIVE")" > SHA256SUMS
else
  echo "No SHA-256 utility found" >&2
  exit 1
fi

printf '%s\n' "Built $ARCHIVE"
printf '%s\n' "Checksum: $DIST/SHA256SUMS"
