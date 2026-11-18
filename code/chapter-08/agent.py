"""Chapter 08: a bounded tool-using agent with validated inputs."""

import argparse
import json
import math
import sys
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
    calls: int


def add(a: float, b: float) -> float:
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Arguments must be finite numbers")
    result = a + b
    if not math.isfinite(result):
        raise ValueError("The result must be finite")
    return result


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
    name = "unknown"
    try:
        function = call["function"]
        name = function["name"]
        if name not in REGISTRY:
            raise ValueError(f"Unknown tool: {name}")
        arguments = function["arguments"]
        if not isinstance(arguments, dict):
            raise ValueError("Tool arguments must be an object")
        content = {"result": REGISTRY[name](**arguments)}
    except Exception as error:
        content = {"error": str(error)}
    return {"role": "tool", "tool_name": str(name), "content": json.dumps(content, allow_nan=False)}


def build_graph(max_steps=8):
    if max_steps < 1:
        raise ValueError("max_steps must be positive")

    def assistant(state):
        reply = call_model(state["messages"], TOOLS)
        return {"messages": state["messages"] + [reply], "calls": state.get("calls", 0) + 1}

    def tool_node(state):
        results = [execute_tool(call) for call in state["messages"][-1].get("tool_calls", [])]
        return {"messages": state["messages"] + results}

    def route(state):
        if not state["messages"][-1].get("tool_calls"):
            return END
        if state["calls"] >= max_steps:
            raise RuntimeError("Step limit reached before a final answer")
        return "tools"

    builder = StateGraph(State)
    builder.add_node("assistant", assistant)
    builder.add_node("tools", tool_node)
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", route, {"tools": "tools", END: END})
    builder.add_edge("tools", "assistant")
    return builder.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", default="Say exactly: Hello World!!!")
    parser.add_argument("--chat", action="store_true", help="Keep messages between turns")
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "qwen3:4b-instruct"))
    parser.add_argument("--base-url", default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    parser.add_argument("--max-steps", type=int, default=8)
    parser.add_argument("--trace", action="store_true", help="Print tool results to stderr")
    args = parser.parse_args()
    if args.max_steps < 1 or not args.prompt.strip():
        parser.error("Use a non-empty prompt and a positive max-steps value")
    os.environ["OLLAMA_MODEL"] = args.model
    os.environ["OLLAMA_BASE_URL"] = args.base_url
    graph = build_graph(args.max_steps)
    messages = [{"role": "system", "content": "Reply briefly. Use add for addition. Never invent tool results."}]
    prompt = args.prompt
    while True:
        messages.append({"role": "user", "content": prompt})
        before = len(messages)
        try:
            state = graph.invoke({"messages": messages, "calls": 0},
                                 {"recursion_limit": 2 * args.max_steps + 4})
        except (RuntimeError, OSError, ValueError) as error:
            parser.exit(1, f"Agent stopped: {error}\n")
        messages = state["messages"]
        if args.trace:
            for message in messages[before:]:
                if message["role"] == "tool":
                    print(f"[tool:{message['tool_name']}] {message['content']}", file=sys.stderr)
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
