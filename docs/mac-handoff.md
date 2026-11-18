# Handoff: set up SteAgent on a Mac

The user wants the project to run on their Mac, including a live slide preview they can edit through chat. The previous session ran on Linux and could not access the Mac filesystem. Do not claim the Mac is already configured.

Repository: https://github.com/scpark20/SteAgent
Preferred destination: `~/projects/steagent`
Guide: [Mac local setup](mac-local-setup.md) · [PDF](mac-local-setup.pdf)

## Complete the setup

1. Confirm this session is local to macOS with `uname -s`, `uname -m`, and `sw_vers`. Check available memory with `sysctl -n hw.memsize` before loading direct weights.
2. Inspect any existing destination and its Git status. Preserve edits. Clone with `--recurse-submodules` when absent; otherwise inspect the remote and update with a fast-forward only when appropriate. Read the checkout's `AGENTS.md`.
3. Ensure Git, uv, and Ollama are installed. Prefer an existing Ollama app or service. With an existing Homebrew installation, `brew install uv ollama` and `brew services start ollama` provide the CLI route. If Homebrew is absent or unsupported on this Mac, use the official uv installer and Ollama Mac application. Complete any OS dialogs with the user.
4. Run `bash scripts/setup_local.sh` from the project. It preserves already-installed optional Python dependencies, initializes the pinned submodule, prepares `qwen3:4b-instruct`, builds the slides, and runs the tests. It does not install OS prerequisites or silently replace a checkout.
5. Run `uv run agent.py "Use add to calculate 12 + 30." --trace`. Confirm an actual `[tool:add] {"result": 42}` observation and a final answer. A unit-test pass alone does not prove local inference works.
6. Start `uv run python tools/steslide/steslide.py preview` in a persistent terminal. Open `http://localhost:8766/lecture.md` on the Mac. Use another port if occupied; do not stop unrelated processes. Verify edits to source Markdown or included Python refresh the preview, then undo any temporary probe.
7. Report the local folder, chip/OS, test results, observed tool result, and preview URL. Separate verified results from any remaining limitations.

## Optional direct inference

Chapter 01 uses `uv run --extra llm code/chapter-01/agent.py`. Its loader selects MPS and FP16 when available; `LLM_DEVICE=cpu` overrides this. The default model is `Qwen/Qwen3-4B-Instruct-2507`; the first run downloads separate Transformers weights. Allow memory beyond the approximately 8 GB of FP16 weights. Do not download or run this optional path without sufficient memory and the user's intended scope.

The pinned PyTorch macOS wheels support Apple Silicon. Do not promise Chapter 01 works on an Intel Mac with this lockfile. Ollama-based Chapters 02–08 remain the Intel CPU route.

## Editing and publication

- Keep executable checkpoints in `code/` and lecture sources in `lecture/`.
- Keep repository text in English.
- Read `docs/slides.md` before editing preview configuration. Generated `.build/`, `lecture.md`, and `chapter.md` are not source files.
- Publish shared tooling changes to SteSlide first, then update the SteAgent submodule pointer.
- Do not copy `/home/scpark/...`, `/snap/firefox/...`, the Linux `.venv`, or installed Linux binaries to the Mac.
- The model adapters use `OLLAMA_MODEL` and `OLLAMA_BASE_URL`; local defaults need no environment file.

## Refresh this PDF

After editing `docs/mac-local-setup.md`, regenerate its committed PDF with the installed Marp CLI. A local Chrome or Firefox installation is required:

```bash
tools/steslide/.tools/marp/marp --no-config-file docs/mac-local-setup.md \
  --html --theme-set tools/steslide/theme.css --pdf \
  --output docs/mac-local-setup.pdf
```

The Linux authoring session may supply an explicit Linux browser path. Do not carry that override into the Mac commands.
