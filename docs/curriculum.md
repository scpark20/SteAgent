# Course outline: a minimal agent, step by step

[← SteAgent](../README.md) · [Current implementation](architecture.md) · [Slides](slides.md)

**Status: teaching plan.** The current executable is a single-call LangGraph hello world. The stages below describe the planned course, not already implemented examples.

## Design rules

- Follow three chapters: **LLM → Ollama → LangGraph**.
- Start every chapter with **Hello World!!!**.
- Evolve one codebase. Keep the existing prompt, message format, tools, and CLI whenever possible.
- Introduce one responsibility at a time. Show the small code diff and the resulting behavior in every section.
- Reuse pretrained model weights. Build the agent's control flow from scratch; model training is outside this course.
- Finish with a bounded loop that can select a tool, run it, observe its result, and return an answer.

## Chapter 01 — LLM

**Goal:** Call a local pretrained model directly, then establish the message and function interface reused later.

| Section | Title | Small change | Result |
| --- | --- | --- | --- |
| 01.01 | Hello World!!! | Load model weights and a tokenizer with PyTorch/Transformers; generate one reply. | Direct model inference, without Ollama or LangGraph. |
| 01.02 | Messages and Chat Templates | Express the prompt as role/content messages and apply the model's chat template. | A consistent input representation. |
| 01.03 | One Model Call Interface | Extract inference into `call_model(messages)` and return an assistant message. | A small boundary around the inference backend. |
| 01.04 | Conversation State | Append user and assistant messages to the same list. | Previous turns become model context. |

The model and tokenizer remain loaded between calls. The first example includes any model-specific formatting required to work; later sections explain and organize that code.

## Chapter 02 — Ollama

**Goal:** Replace the inference backend, then add tool use and a plain Python agent loop.

| Section | Title | Small change | Result |
| --- | --- | --- | --- |
| 02.01 | Hello World!!! | Replace the body of `call_model()` with an Ollama `/api/chat` request. Remove direct model-loading code. | The same greeting, messages, and caller through an API. |
| 02.02 | One Python Tool | Add an `add(a, b)` function, its input schema, and a tool registry. | One explicit action the program can perform. |
| 02.03 | Let the Model Request an Action | Pass tool definitions to the model and preserve returned tool calls. | Distinguish a final answer from an action request. |
| 02.04 | Execute and Return the Result | Dispatch the requested function and append its result to the messages. | The model can observe what the tool did. |
| 02.05 | The Agent Loop | Repeat model → tool → result until a final answer or a step limit. | A working minimal agent in plain Python. |

Keep the CLI and message history. Expand `call_model()` only as needed to pass tool definitions and return tool requests. Use a named function rather than evaluating arbitrary generated code.

## Chapter 03 — LangGraph

**Goal:** Express the same agent as a graph, retaining its model adapter and tool functions.

| Section | Title | Small change | Result |
| --- | --- | --- | --- |
| 03.01 | Hello World!!! | Wrap the existing agent function in a single graph node and run the same greeting. | A graph entry point with existing behavior preserved. |
| 03.02 | Separate State and Nodes | Extract the existing model step and tool step into nodes sharing message state. | Explicit state and node responsibilities. |
| 03.03 | Replace the Loop with Edges | Move the Python loop's decisions into conditional edges. | Tool requests return to the model; final answers reach END. |
| 03.04 | Stop and Recover | Keep bounded execution and handle invalid arguments, unknown tools, and tool failures. | Predictable termination and useful failure behavior. |
| 03.05 | Verify the Minimal Agent | Run greeting, tool-use, and failure/limit cases through the same entry point. | The complete minimal agent is demonstrated. |

Add message conversion only at the graph boundary where needed. Remove the old loop after its behavior is represented by edges. Do not replace the model adapter or tool implementation during this migration.

## What changes between chapters?

| Transition | Keep | Replace or add |
| --- | --- | --- |
| LLM → Ollama | Prompt, messages, callable interface, CLI | Replace direct inference with an HTTP model adapter; then add tools and a loop. |
| Ollama → LangGraph | Model adapter, tool definitions, tool functions, observable behavior | Replace orchestration with state, nodes, and conditional edges. |

The final demonstration is deliberately small: answer a greeting directly, choose the addition tool when needed, use its result in the final response, and stop predictably on failures or limits.
