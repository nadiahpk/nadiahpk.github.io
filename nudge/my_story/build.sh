#!/usr/bin/env bash
set -euo pipefail

# Path to the tweego installation
TWEEGO_BIN="$HOME/work/teaching/twine_experiments/code/tweego/tweego"
export TWEEGO_PATH="$HOME/work/teaching/twine_experiments/code/tweego/storyformats"

# Project directories (relative to this script)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$SCRIPT_DIR/src"
DIST_DIR="$SCRIPT_DIR/dist"

mkdir -p "$DIST_DIR"

echo "Compiling story..."
"$TWEEGO_BIN" -o "$DIST_DIR/story.html" "$SRC_DIR"
echo "Done -> $DIST_DIR/story.html"
