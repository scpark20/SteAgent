# Course: a minimal agent through small changes

[← SteAgent](../README.md) · [Run the examples](usage.md) · [Slides](slides.md)

Each chapter has executable code in `code/chapter-*/agent.py` and separate slides in `lecture/chapter-*/section-*.md`. Every chapter starts with Hello World!!! and explains the actual source. Chapter 02 onward also has a `changes.diff` against the previous implementation. The slide generator reads code excerpts from the actual source files.

| Chapter | Opening | Subsequent sections | Change from the previous code |
| --- | --- | --- | --- |
| [01 · LLM](../code/chapter-01/) | Hello World!!! | Loading weights; templates; token generation | Establish `call_model(messages)` and a small CLI. |
| [02 · Ollama](../code/chapter-02/) | Hello World!!! | HTTP model call; unchanged caller | Replace direct inference with `/api/chat`. |
| [03 · LangGraph](../code/chapter-03/) | Hello World!!! | State; assistant node; graph edges | Wrap the same adapter in START → assistant → END. |
| [04 · State & Memory](../code/chapter-04/) | Hello World!!! | Message history; interactive turns | Keep graph code; retain messages between invocations. |
| [05 · Tools](../code/chapter-05/) | Hello World!!! | Function; schema; registry; dispatch | Add one explicit Python action without changing inference. |
| [06 · Tool Calling](../code/chapter-06/) | Hello World!!! | Model action requests; routing; execution | Send the tool schema and execute a requested call once. |
| [07 · Agent Loop](../code/chapter-07/) | Hello World!!! | Result feedback; repeated decisions | Change the tools edge from END to assistant. |
| [08 · Minimal Agent](../code/chapter-08/) | Hello World!!! | Input validation; tool errors; limits; demonstration | Preserve the loop and add predictable failure behavior. |

## How to teach each checkpoint

1. Run the Hello World!!! example.
2. Compare the source with the previous chapter.
3. Explain the changed function and its state/input/output.
4. Run the new behavior, then verify that the old greeting still works.

Compare adjacent checkpoints directly:

```bash
git diff --no-index code/chapter-06/agent.py code/chapter-07/agent.py
```

The final demonstration answers a greeting, chooses the addition tool when needed, observes the real result, and stops predictably on errors or limits. This course builds agent control flow from pretrained model weights; it does not train a language model from scratch.
