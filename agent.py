"""Hello-world LangGraph agent: START -> assistant -> END."""

import argparse
import os

from langchain_ollama import ChatOllama
from langgraph.graph import END, START, MessagesState, StateGraph


def build_graph(model: str, base_url: str):
    llm = ChatOllama(
        model=model,
        base_url=base_url,
        temperature=0,
        reasoning=False,
        num_ctx=4096,
        num_predict=256,
        client_kwargs={"timeout": 120.0},
        validate_model_on_init=True,
    )

    def assistant(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}

    builder = StateGraph(MessagesState)
    builder.add_node("assistant", assistant)
    builder.add_edge(START, "assistant")
    builder.add_edge("assistant", END)
    return builder.compile()


def main():
    parser = argparse.ArgumentParser(description="LangGraph hello world using a local Ollama model")
    parser.add_argument(
        "prompt", nargs="?", default="Say Hello, world! and introduce yourself in one sentence."
    )
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "qwen3:4b-instruct"))
    parser.add_argument(
        "--base-url", default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    )
    args = parser.parse_args()
    if not args.prompt.strip():
        parser.error("Please enter a non-empty prompt.")

    graph = build_graph(args.model, args.base_url)
    result = graph.invoke(
        {
            "messages": [
                ("system", "You are SteAgent, an AI assistant. Reply briefly and clearly in the user's language."),
                ("user", args.prompt),
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
