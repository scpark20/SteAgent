# From inference to a minimal agent

[← SteAgent](../README.md) · [Run the examples](usage.md) · [Slides](slides.md)

One evolving Python program, eight executable checkpoints, and a 19-slide lecture. Code lives in `code/chapter-*/agent.py`; explanations live separately in `lecture/chapter-*/`. Slides include excerpts from the actual source. Chapters 02–08 include a `changes.diff` against the preceding checkpoint.

| Chapter | Demonstration | Change from the previous code | Slides |
| --- | --- | --- | ---: |
| [01 · LLM](../code/chapter-01/) | The first Hello World!!! | Load pretrained weights; tokenize, generate, and decode behind `call_model(messages)`. | 3 |
| [02 · Ollama](../code/chapter-02/) | Answer a question through HTTP | Replace local inference with `/api/chat`; keep the caller and return shape. | 2 |
| [03 · LangGraph](../code/chapter-03/) | Trace one state update through a graph | Add state, an assistant node, and START → assistant → END. | 2 |
| [04 · State & Memory](../code/chapter-04/) | Recall a name across turns | Retain the message list between invocations. | 1 |
| [05 · Tools](../code/chapter-05/) | Execute `add(2, 3)` explicitly | Add a function, schema, registry, and executor. | 2 |
| [06 · Tool Calling](../code/chapter-06/) | Let the model request `add(12, 30)` | Attach the schema, route a tool request, and execute once. | 2 |
| [07 · Agent Loop](../code/chapter-07/) | Answer using the observed result | Change one edge: tools → END becomes tools → assistant. | 2 |
| [08 · Minimal Agent](../code/chapter-08/) | Validate requests, handle failures, and stop | Add argument checks, error observations, and a model-call budget. | 4 |

The opening slide shows the destination; the 18 chapter slides explain how to build it. Chapter lengths follow the amount of new behavior, rather than repeating a fixed format.

## Teaching progression

Start from something the learner can execute, inspect the changed code, and trace its inputs, state changes, and outputs. Keep the explanation and relevant code together. Use a new demonstration when a chapter adds a capability; do not repeat a greeting as every chapter's introduction.

Compare adjacent checkpoints directly:

```bash
git diff --no-index code/chapter-06/agent.py code/chapter-07/agent.py
```

The final agent selects a tool, executes it in Python, feeds the observation back to the model, and stops explicitly at its call budget. This course builds agent control flow from pretrained weights; it does not train a language model from scratch.

See [teaching notes and reference courses](teaching-notes.md) for the design rationale and reviewed material.
