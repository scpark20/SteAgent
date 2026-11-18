# Usage guide

[← SteAgent](../README.md) · [Course outline](curriculum.md) · [Slides](slides.md)

## Setup

For a Mac-local checkout, use the [setup guide](mac-local-setup.md) or its [PDF](mac-local-setup.pdf). After installing uv and Ollama, `bash scripts/setup_local.sh` prepares dependencies, the model, the slide tool, and the tests.

```bash
git clone --recurse-submodules https://github.com/scpark20/SteAgent.git
cd SteAgent
uv sync --locked
```

Requires Python 3.11+ and uv. Chapters 02–08 need a running Ollama service and the model:

```bash
ollama pull qwen3:4b-instruct
```

If Ollama is not already running as an application or service, run `ollama serve` in another terminal.

## Chapter 01: direct weights

```bash
uv sync --locked --extra llm
uv run --extra llm code/chapter-01/agent.py
```

Set `LLM_MODEL` to a Hugging Face model ID or local directory:

```bash
LLM_MODEL=/path/to/qwen-checkpoint uv run --extra llm code/chapter-01/agent.py
```

The default is `Qwen/Qwen3-4B-Instruct-2507`. PyTorch, Transformers, and Accelerate are optional dependencies. The first run may download the selected model. On Apple Silicon, an available MPS backend is selected with FP16; other hosts keep automatic device placement. Set `LLM_DEVICE=cpu` to force CPU execution. The locked PyTorch macOS wheels require Apple Silicon; Intel Macs can run the Ollama chapters.

Allow memory for the weights and runtime buffers. FP8 checkpoints are dequantized on load. The local Qwen3-8B-FP8 checkpoint has been verified on an RTX 5090; Apple GPU inference has not yet been verified on a real Mac.

## Chapter checkpoints

```bash
uv run code/chapter-02/agent.py
uv run code/chapter-03/agent.py
uv run code/chapter-04/agent.py --chat
uv run code/chapter-05/agent.py --tool-demo
uv run code/chapter-06/agent.py "Use add to calculate 12 + 30."
uv run code/chapter-07/agent.py "Use add to calculate 12 + 30."
uv run code/chapter-08/agent.py "Use add to calculate 12 + 30." --trace
```

All scripts accept a positional prompt. Chapter 01 defaults to Hello World!!!; Chapters 02, 03, and 05 ask a short arithmetic question; Chapter 04 introduces the name Ada; Chapters 06–08 request the addition tool. Chapters 04–08 accept `--chat`. In Chapter 04, ask “What is my name?” at the next prompt. Chapter 05 demonstrates direct dispatch with `--tool-demo`; Chapter 06 ends at the tool result; Chapter 07 returns that result to the model.

Use `OLLAMA_MODEL` and `OLLAMA_BASE_URL` to configure Chapters 02–08. Defaults are `qwen3:4b-instruct` and `http://localhost:11434`.

## Final agent

```bash
uv run agent.py
uv run agent.py "Use add to calculate 12 + 30." --trace
uv run agent.py --chat
uv run agent.py --max-steps 4 --model qwen3:4b-instruct
```

`--base-url` selects the Ollama server. `--trace` prints actual tool observations to stderr. `--max-steps` limits model calls per user turn. Exhausting the budget produces an explicit error and a nonzero exit status. Tool failures are returned as observations so the model can respond or correct its request.

Conversation history stays in memory until the process exits. It is not a database or long-term memory.

## Verification

```bash
uv run python -m unittest discover -s tests -v
```

Tests cover greeting-only responses, tool results reaching the model, multiple tool rounds, bad arguments, unknown tools, runtime failures, and execution limits. They also check the behavioral change from Chapter 06 to Chapter 07.

If Python cannot import a dependency, run through `uv run` instead of an unrelated system interpreter. If `tools/steslide` is empty, run `git submodule update --init --recursive`.

References: [Qwen weights](https://huggingface.co/Qwen/Qwen3-8B-FP8), [Ollama tool calling](https://docs.ollama.com/capabilities/tool-calling), [Transformers FP8](https://huggingface.co/docs/transformers/quantization/finegrained_fp8).
