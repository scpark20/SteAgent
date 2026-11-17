# Usage guide

[← SteAgent](../README.md) · [Architecture](architecture.md) · [Slides](slides.md)

## Install and run

Install Python 3.11+, [uv](https://docs.astral.sh/uv/getting-started/installation/), and [Ollama](https://ollama.com/download).

```bash
git clone --recurse-submodules https://github.com/scpark20/SteAgent.git
cd SteAgent
uv sync --locked
```

Start the Ollama application or service. If no service is running, run `ollama serve` in a separate terminal. Then download the model and run the agent:

```bash
ollama pull qwen3:4b-instruct
uv run agent.py
uv run agent.py "What is 2 + 3?"
```

Dependencies are pinned in `uv.lock`. `uv sync --locked` installs them into the project's `.venv`, and `uv run` selects that environment.

## Choose a model or server

```bash
ollama list
uv run agent.py --model qwen3:4b-instruct "Introduce yourself in one sentence."
uv run agent.py --base-url http://localhost:11434 "Hello!"
```

Use a model name installed in Ollama. The default model's official page is [Qwen3 4B Instruct](https://ollama.com/library/qwen3:4b-instruct).

| Setting | CLI option | Environment variable | Default |
| --- | --- | --- | --- |
| Model | `--model` | `OLLAMA_MODEL` | `qwen3:4b-instruct` |
| Ollama URL | `--base-url` | `OLLAMA_BASE_URL` | `http://localhost:11434` |

CLI options take precedence over environment variables. Omitting the prompt uses the default greeting request.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `No module named 'langchain_ollama'` | Run `uv sync --locked`, then use `uv run agent.py`. |
| Ollama connection failure | Check that the application/service is running and `--base-url` is correct. |
| Model not found | Check `ollama list` and download the model with `ollama pull`. |
| Empty `tools/steslide` directory | Run `git submodule update --init --recursive`. |

To run with plain `python`, activate `.venv` first or use `.venv/bin/python agent.py` on macOS/Linux. A standalone Safetensors checkpoint cannot be passed directly as an Ollama model name; it needs a supported import/conversion workflow or a separate inference integration.
