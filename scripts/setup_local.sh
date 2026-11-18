#!/usr/bin/env bash
# Prepare a local checkout; install uv and Ollama before running this script.
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

if [[ "$(uname -s)" == "Darwin" ]]; then
  mac_version="$(sw_vers -productVersion)"
  if [[ "${mac_version%%.*}" -lt 14 ]]; then
    echo "Ollama requires macOS 14 or newer." >&2
    exit 1
  fi
  export PATH="$PATH:/Applications/Ollama.app/Contents/Resources:$HOME/Applications/Ollama.app/Contents/Resources"
fi

for required in git uv ollama; do
  if ! command -v "$required" >/dev/null 2>&1; then
    echo "Missing $required. See docs/mac-local-setup.md for installation." >&2
    exit 1
  fi
done

git submodule update --init --recursive
# Preserve optional direct-inference dependencies if they are already installed.
uv sync --locked --inexact

export OLLAMA_HOST="${OLLAMA_BASE_URL:-http://localhost:11434}"
model="${OLLAMA_MODEL:-qwen3:4b-instruct}"
if ! ollama list >/dev/null 2>&1; then
  if [[ "$(uname -s)" == "Darwin" && "$OLLAMA_HOST" == "http://localhost:11434" ]]; then
    if [[ -d /Applications/Ollama.app ]]; then
      open -a /Applications/Ollama.app
    elif [[ -d "$HOME/Applications/Ollama.app" ]]; then
      open -a "$HOME/Applications/Ollama.app"
    elif command -v brew >/dev/null 2>&1 && brew list --formula ollama >/dev/null 2>&1; then
      brew services start ollama
    fi
  fi
  ready=false
  for attempt in {1..30}; do
    if ollama list >/dev/null 2>&1; then
      ready=true
      break
    fi
    sleep 1
  done
  if [[ "$ready" != true ]]; then
    echo "Ollama is unavailable at $OLLAMA_HOST. Start the Ollama app or run 'ollama serve', then retry." >&2
    exit 1
  fi
fi

if ! ollama show "$model" >/dev/null 2>&1; then
  ollama pull "$model"
fi

if [[ -z "${STESLIDE_MARP:-}" && ! -x tools/steslide/.tools/marp/marp ]] && ! command -v marp >/dev/null 2>&1; then
  uv run --locked python tools/steslide/scripts/setup_marp.py
fi
uv run --locked python - <<'PY'
import runpy
import subprocess
tool = runpy.run_path("tools/steslide/steslide.py")
subprocess.run([tool["marp_executable"](), "--version"], check=True)
PY
uv run --locked python tools/steslide/steslide.py build
uv run --locked python -m unittest discover -s tests -v

echo "Local setup complete."
echo 'Run:     uv run agent.py --trace'
echo 'Slides:  uv run python tools/steslide/steslide.py preview'
