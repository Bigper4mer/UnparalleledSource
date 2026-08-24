#!/usr/bin/env sh
set -eu

REPOSITORY="Bigper4mer/UnparalleledSource"
REF="${HIVEFORGE_REF:-main}"
INSTALL_ROOT="${HIVEFORGE_HOME:-${XDG_DATA_HOME:-${HOME}/.local/share}/unps-hiveforge}"
BIN_ROOT="${HIVEFORGE_BIN_DIR:-${HOME}/.local/bin}"
FORCE=0

usage() {
  cat <<'EOF'
Install UNPS HiveForge.

Usage:
  install.sh [--target DIRECTORY] [--bin-dir DIRECTORY] [--ref BRANCH_OR_TAG] [--force]

Options:
  --target   Installation directory.
  --bin-dir  Directory for the hiveforge launcher.
  --ref      Git branch or tag to install. Default: main.
  --force    Preserve the existing installation as a timestamped backup, then install.
  --help     Show this help.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      [ "$#" -ge 2 ] || { echo "Missing value for --target" >&2; exit 2; }
      INSTALL_ROOT=$2
      shift 2
      ;;
    --bin-dir)
      [ "$#" -ge 2 ] || { echo "Missing value for --bin-dir" >&2; exit 2; }
      BIN_ROOT=$2
      shift 2
      ;;
    --ref)
      [ "$#" -ge 2 ] || { echo "Missing value for --ref" >&2; exit 2; }
      REF=$2
      shift 2
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

for required_command in tar mkdir cp mv chmod; do
  command -v "$required_command" >/dev/null 2>&1 || {
    echo "HiveForge installer requires: $required_command" >&2
    exit 1
  }
done

temporary_root=$(mktemp -d 2>/dev/null || mktemp -d -t hiveforge)
staging_root="${INSTALL_ROOT}.staging.$$"

cleanup() {
  [ ! -d "$temporary_root" ] || rm -rf "$temporary_root"
  [ ! -d "$staging_root" ] || rm -rf "$staging_root"
}
trap cleanup EXIT HUP INT TERM

if [ -n "${HIVEFORGE_SOURCE_DIR:-}" ]; then
  source_root=$HIVEFORGE_SOURCE_DIR
else
  command -v curl >/dev/null 2>&1 || {
    echo "HiveForge installer requires curl for remote installation." >&2
    exit 1
  }

  archive="$temporary_root/hiveforge.tar.gz"
  extract_root="$temporary_root/source"
  mkdir -p "$extract_root"

  case "$REF" in
    *[!A-Za-z0-9._/-]*)
      echo "Invalid ref: $REF" >&2
      exit 2
      ;;
  esac

  curl --proto '=https' --tlsv1.2 -fsSL \
    "https://github.com/${REPOSITORY}/archive/refs/heads/${REF}.tar.gz" \
    -o "$archive"
  tar -xzf "$archive" -C "$extract_root"
  set -- "$extract_root"/*
  source_root=$1
fi

for required_path in \
  "10_CUSTOM_AGENTS/UNPS_HiveForge/BRAIN.md" \
  "10_CUSTOM_AGENTS/UNPS_HiveForge/AGENT.md" \
  "10_CUSTOM_AGENTS/UNPS_HiveForge/SYSTEM_INSTRUCTIONS.md" \
  "10_CUSTOM_AGENTS/UNPS_HiveForge/PACKAGE_MANIFEST.md" \
  "bin/hiveforge"; do
  [ -f "$source_root/$required_path" ] || {
    echo "Invalid HiveForge source: missing $required_path" >&2
    exit 1
  }
done

if [ -e "$INSTALL_ROOT" ]; then
  if [ "$FORCE" -ne 1 ]; then
    echo "HiveForge is already installed at $INSTALL_ROOT" >&2
    echo "Re-run with --force to preserve it as a backup and install this version." >&2
    exit 1
  fi
  backup_root="${INSTALL_ROOT}.backup.$(date +%Y%m%d%H%M%S)"
  mv "$INSTALL_ROOT" "$backup_root"
  echo "Previous installation preserved at $backup_root"
fi

mkdir -p "$(dirname "$INSTALL_ROOT")" "$staging_root"

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
  bin \
  README.md \
  SECURITY.md \
  DRIVE_SYNC_MANIFEST.md; do
  [ ! -e "$source_root/$item" ] || cp -R "$source_root/$item" "$staging_root/"
done

chmod +x "$staging_root/bin/hiveforge"
mv "$staging_root" "$INSTALL_ROOT"

mkdir -p "$BIN_ROOT"
launcher="$BIN_ROOT/hiveforge"
if [ -e "$launcher" ] && [ ! -L "$launcher" ]; then
  echo "Existing launcher was not replaced: $launcher" >&2
  echo "Run HiveForge directly: $INSTALL_ROOT/bin/hiveforge" >&2
else
  ln -sfn "$INSTALL_ROOT/bin/hiveforge" "$launcher"
fi

"$INSTALL_ROOT/bin/hiveforge" doctor

cat <<EOF

UNPS HiveForge installed successfully.

Install:  $INSTALL_ROOT
Launcher: $launcher

Next:
  hiveforge bootstrap

If the launcher directory is not on PATH:
  $INSTALL_ROOT/bin/hiveforge bootstrap
EOF

