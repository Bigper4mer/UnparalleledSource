#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TMP=$(mktemp -d 2>/dev/null || mktemp -d -t hiveforge-test)
trap 'rm -rf "$TMP"' EXIT HUP INT TERM

install_one="$TMP/install-one"
bin_one="$TMP/bin-one"
HIVEFORGE_SOURCE_DIR="$ROOT" sh "$ROOT/install.sh" --target "$install_one" --bin-dir "$bin_one"
"$bin_one/hiveforge" doctor
[ "$("$bin_one/hiveforge" version)" = "0.5.0" ]

export_root="$TMP/export/unps-hiveforge-v0.5.0"
mkdir -p "$export_root"
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
  [ ! -e "$ROOT/$item" ] || cp -R "$ROOT/$item" "$export_root/"
done

archive="$TMP/unps-hiveforge-v0.5.0.tar.gz"
tar -czf "$archive" -C "$TMP/export" unps-hiveforge-v0.5.0
mkdir -p "$TMP/imported"
tar -xzf "$archive" -C "$TMP/imported"

import_root="$TMP/imported/unps-hiveforge-v0.5.0"
install_two="$TMP/install-two"
bin_two="$TMP/bin-two"
HIVEFORGE_SOURCE_DIR="$import_root" sh "$import_root/install.sh" --target "$install_two" --bin-dir "$bin_two"
"$bin_two/hiveforge" doctor
[ "$("$bin_two/hiveforge" version)" = "0.5.0" ]

printf '%s\n' "HiveForge package export/import: PASS"
