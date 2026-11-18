"""Chapter 03: wrap the existing model call in a single graph node."""

import argparse
import json
import os
import urllib.request
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


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


class State(TypedDict):
    messages: list[dict]


def build_graph():
    def assistant(state):
        reply = call_model(state["messages"])
        return {"messages": state["messages"] + [reply]}

    builder = StateGraph(State)
    builder.add_node("assistant", assistant)
    builder.add_edge(START, "assistant")
    builder.add_edge("assistant", END)
    return builder.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", default="Say exactly: Hello World!!!")
    args = parser.parse_args()
    messages = [{"role": "user", "content": args.prompt}]
    graph = build_graph()
    state = graph.invoke({"messages": messages})
    print(state["messages"][-1]["content"])


if __name__ == "__main__":
    main()
