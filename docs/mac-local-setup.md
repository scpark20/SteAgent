---
marp: true
theme: steslide
size: 16:9
paginate: true
footer: "STEAGENT · MAC LOCAL SETUP · 2026-11-18"
style: |
  section { --code-width: 1100px; font-size: 21px; font-variant-ligatures: none; }
  pre code { font-size: 19px; }
  h1 { font-size: 38px; }
  table { font-size: 18px; }
  th, td { padding: 8px 12px; }
---

# Run SteAgent on your Mac

**Goal:** run the agent and edit its live slides entirely on your Mac, without the Linux server.

| Component | Local requirement |
| --- | --- |
| Agent · Chapters 02–08 | macOS 14+, uv, and a running Ollama service |
| Hardware | Apple Silicon uses GPU acceleration; Intel uses CPU |
| Direct weights · Chapter 01 | Apple Silicon for the locked macOS PyTorch packages |
| Slides | Apple Silicon: bundled Marp; Intel: Node.js + npm Marp |

On Apple Silicon with a supported Homebrew installation, install the CLI tools:

```bash
brew install uv ollama
brew services start ollama
```

Alternatively, install [uv](https://docs.astral.sh/uv/getting-started/installation/) and the [Ollama Mac app](https://ollama.com/download/mac), then open Ollama. An existing Ollama app is sufficient; choose one installation route. If Git is missing, run `xcode-select --install` and finish Apple's dialog.

For Intel Mac slides, install Node.js 18+ and run `npm install -g @marp-team/marp-cli@4.5.1` before setup.

---

# Download the project and verify the agent

Run these commands in **macOS Terminal**, not a terminal connected to Linux over SSH.

```bash
mkdir -p ~/projects
cd ~/projects
git clone --recurse-submodules https://github.com/scpark20/SteAgent.git steagent
cd steagent
bash scripts/setup_local.sh
uv run agent.py "Use add to calculate 12 + 30." --trace
```

The setup script checks prerequisites, syncs Python packages, downloads the model if missing, installs Marp if missing, builds slides, and runs the unit tests. It can start an installed Ollama app or Homebrew service. Downloads need internet access; inference then runs locally.

```text
[tool:add] {"result": 42}
12 + 30 = 42.
```

The wording of the final answer can vary. If `~/projects/steagent` already exists, inspect its Git status and remote before updating it. Preserve local edits; do not overwrite the folder or copy the Linux `.venv`.

---

# Open the slides and keep editing

From `~/projects/steagent`, start the preview and leave this terminal running:

```bash
uv run python tools/steslide/steslide.py preview
```

Open **http://localhost:8766/lecture.md** in your Mac browser. Open the local `~/projects/steagent` folder in VS Code. This local workflow does not require SSH or port forwarding.

| Edit | Result |
| --- | --- |
| `code/chapter-*/agent.py` | Actual runnable source; included excerpts refresh in the slides |
| `lecture/chapter-*/intro.md` or `section-*.md` | Slide explanations and layout refresh |
| `tools/steslide/theme.css` | Shared visual styling; publish changes to SteSlide first |

Export the lecture PDF after installing Chrome or Firefox on the Mac:

```bash
uv run python tools/steslide/steslide.py export --format pdf
```

Output: `lecture/.build/lecture.pdf`. Browser preview does not need an export browser. Do not use the Linux `/snap/firefox/...` path on macOS.

---

# Optional: Chapter 01 without Ollama

This path loads a separate Hugging Face checkpoint through Transformers. It does not reuse Ollama's quantized model file. The default 4B model uses about 8 GB for FP16 weights alone, plus runtime memory.

```bash
uv sync --locked --extra llm
uv run --extra llm code/chapter-01/agent.py
```

The loader selects **MPS with FP16** when Apple's GPU backend is available. `LLM_DEVICE` overrides automatic selection; `LLM_MODEL` selects a model ID or a Mac-local checkpoint path.

```bash
LLM_DEVICE=cpu uv run --extra llm code/chapter-01/agent.py
```

| Situation | Next step |
| --- | --- |
| Not enough unified memory | Close other apps or choose a smaller compatible `LLM_MODEL` |
| MPS-specific failure | Try `LLM_DEVICE=cpu`; expect slower generation |
| Intel Mac | Use Chapters 02–08; the locked torch version has no Intel Mac wheel |

**Validation status:** Linux execution and device-selection tests pass. Actual Apple GPU inference must still be verified in the Mac session.

---

# Continue in a Mac Codex session

Open a Codex session with access to your **Mac's local filesystem**, then send:

> Set up scpark20/SteAgent locally in `~/projects/steagent`. Read `AGENTS.md` and `docs/mac-handoff.md` first. Preserve any existing checkout and edits. Install missing prerequisites, initialize the SteSlide submodule, and run `scripts/setup_local.sh`. Verify the final agent with `--trace`, open the local slide preview, and report the actual results. Check Apple GPU availability before trying the optional direct-weight chapter. Do not use the Linux server paths or its virtual environment.

| Symptom | Action |
| --- | --- |
| Ollama connection refused | Open Ollama or run `ollama serve`, then retry |
| Missing model | Run `ollama pull qwen3:4b-instruct` |
| Python import error | Use `uv run`; rerun `bash scripts/setup_local.sh` |
| Port 8766 in use | Use `preview --port 8767` and open that port |

Sources: [Ollama macOS requirements](https://docs.ollama.com/macos), [PyTorch MPS](https://docs.pytorch.org/docs/stable/notes/mps.html), [Homebrew uv](https://formulae.brew.sh/formula/uv), [Homebrew Ollama](https://formulae.brew.sh/formula/ollama).

Repository: [github.com/scpark20/SteAgent](https://github.com/scpark20/SteAgent). Download this [PDF from GitHub](https://github.com/scpark20/SteAgent/blob/main/docs/mac-local-setup.pdf).
