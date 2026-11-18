"""Chapter 06: let the model request one tool execution."""

import argparse
import json
import os
import urllib.request
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


def call_model(messages, tools=None):
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "qwen3:4b-instruct"),
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {"temperature": 0, "num_ctx": 4096, "num_predict": 256},
    }
    if tools:
        payload["tools"] = tools
    url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/") + "/api/chat"
    request = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)["message"]


class State(TypedDict):
    messages: list[dict]


def add(a: float, b: float) -> float:
    return a + b


TOOLS = [{
    "type": "function",
    "function": {
        "name": "add",
        "description": "Add two numbers. Use this tool for addition.",
        "parameters": {
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"],
            "additionalProperties": False,
        },
    },
}]
REGISTRY = {"add": add}


def execute_tool(call):
    function = call["function"]
    name = function["name"]
    result = REGISTRY[name](**function["arguments"])
    return {"role": "tool", "tool_name": name, "content": json.dumps({"result": result})}


def build_graph():
    def assistant(state):
        reply = call_model(state["messages"], TOOLS)
        return {"messages": state["messages"] + [reply]}

    def tool_node(state):
        results = [execute_tool(call) for call in state["messages"][-1].get("tool_calls", [])]
        return {"messages": state["messages"] + results}

    def route(state):
        return "tools" if state["messages"][-1].get("tool_calls") else END

    builder = StateGraph(State)
    builder.add_node("assistant", assistant)
    builder.add_node("tools", tool_node)
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", route, {"tools": "tools", END: END})
    builder.add_edge("tools", END)
    return builder.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", default="Use add to calculate 12 + 30.")
    parser.add_argument("--chat", action="store_true", help="Keep messages between turns")
    parser.add_argument("--tool-demo", action="store_true", help="Execute add(2, 3) directly")
    args = parser.parse_args()
    if args.tool_demo:
        call = {"function": {"name": "add", "arguments": {"a": 2, "b": 3}}}
        print(execute_tool(call)["content"])
        return
    graph = build_graph()
    messages = []
    prompt = args.prompt
    while True:
        messages.append({"role": "user", "content": prompt})
        state = graph.invoke({"messages": messages})
        messages = state["messages"]
        print(messages[-1]["content"])
        if not args.chat:
            break
        try:
            prompt = input("You (empty to exit): ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not prompt:
            break


if __name__ == "__main__":
    main()
