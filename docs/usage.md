# 실행 가이드

[← SteAgent](../README.md) · [동작 구조](architecture.md) · [슬라이드](slides.md)

## 설치와 첫 실행

Python 3.11 이상, [uv](https://docs.astral.sh/uv/getting-started/installation/), [Ollama](https://ollama.com/download)를 설치합니다.

```bash
git clone --recurse-submodules https://github.com/scpark20/SteAgent.git
cd SteAgent
uv sync --locked
```

Ollama 앱이나 서비스를 실행합니다. 서비스가 없다면 별도 터미널에서 `ollama serve`를 실행합니다. 이후 모델을 내려받고 에이전트를 실행합니다.

```bash
ollama pull qwen3:4b-instruct
uv run agent.py
uv run agent.py "안녕! 2 + 3은 얼마야?"
```

의존성은 `uv.lock`에 고정하며 `uv sync --locked`가 프로젝트의 `.venv`에 설치합니다. `uv run`은 그 환경에서 실행하므로 시스템 Python 환경과 섞이지 않습니다.

## 모델과 서버 선택

```bash
ollama list
uv run agent.py --model qwen3:4b-instruct "한 문장으로 자기소개해 줘."
uv run agent.py --base-url http://localhost:11434 "Hello!"
```

`--model`에는 Ollama에 설치된 모델 이름을 사용합니다. 기본 모델의 공식 페이지는 [Qwen3 4B Instruct](https://ollama.com/library/qwen3:4b-instruct)입니다.

| 설정 | 명령줄 옵션 | 환경변수 | 기본값 |
| --- | --- | --- | --- |
| 모델 | `--model` | `OLLAMA_MODEL` | `qwen3:4b-instruct` |
| Ollama 주소 | `--base-url` | `OLLAMA_BASE_URL` | `http://localhost:11434` |

명령줄 옵션이 환경변수보다 우선합니다. 프롬프트를 생략하면 기본 인사말 요청을 사용합니다.

## 자주 만나는 오류

| 증상 | 확인할 것 |
| --- | --- |
| `No module named 'langchain_ollama'` | `uv sync --locked` 후 `uv run agent.py`로 실행합니다. |
| Ollama 연결 실패 | 앱·서비스가 실행 중인지, `--base-url`이 맞는지 확인합니다. |
| 모델을 찾을 수 없음 | `ollama list`로 이름을 확인하고 필요한 모델을 `ollama pull`로 받습니다. |
| `tools/steslide`가 비어 있음 | `git submodule update --init --recursive`를 실행합니다. |

일반 `python`으로 실행하려면 먼저 `.venv`를 활성화하거나 `.venv/bin/python agent.py`를 사용합니다. 로컬 Safetensors 파일만 보유한 경우에는 Ollama 모델 이름으로 곧바로 사용할 수 없으며 별도의 등록·변환 또는 다른 추론 서버 연동이 필요합니다.
