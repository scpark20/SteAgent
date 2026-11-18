"""Chapter 02: replace direct inference with an Ollama HTTP request."""

import argparse
import json
import os
import urllib.request


def call_model(messages):
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "qwen3:4b-instruct"),
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {"temperature": 0, "num_ctx": 4096, "num_predict": 256},
    }
    url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/") + "/api/chat"
    request = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)["message"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", default="What is 2 + 3? Reply with only the number.")
    args = parser.parse_args()
    messages = [{"role": "user", "content": args.prompt}]
    reply = call_model(messages)
    print(reply["content"])


if __name__ == "__main__":
    main()
