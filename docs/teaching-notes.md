# Teaching design and references

## Structure

The lecture contains 19 slides: one opening demonstration and 18 slides across eight chapters. Chapters have different lengths. Memory needs one focused page; direct inference and bounded execution need more space.

Only the first direct-model example uses Hello World!!!. Later demonstrations expose the new capability: an HTTP response, a graph state update, name recall, explicit tool dispatch, a model-selected action, result feedback, and bounded execution.

Code and explanation share the same screen. Tables explain contracts and state transitions; diagrams show execution boundaries and feedback. Equations describe autoregressive generation and the context budget. Diagrams and prose are tied to the actual implementation, including its limitations.

Executable code stays in `code/`; slide sources stay in `lecture/`. Named excerpts are extracted from the Python files. Focused excerpts select inclusive function-relative lines when showing the entire CLI would crowd the slide. Captions identify the file, symbol, and selected range.

## Public courses reviewed

| Source | Observed teaching structure | Applied here |
| --- | --- | --- |
| [LangChain Academy: Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) | Progresses from simple graphs through chains, routing, agents, and memory. | Introduce execution control through small code changes and visible state transitions. |
| [Official Academy notebooks](https://github.com/langchain-ai/langchain-academy/tree/main/module-1) | The simple-graph notebook introduces state, nodes, edges, construction, and invocation. | Place graph construction beside its execution diagram and trace the returned state. |
| [Hugging Face LLM Course: Behind the pipeline](https://huggingface.co/learn/llm-course/chapter2/2) | Begins with a working example, then decomposes preprocessing, model execution, and postprocessing. | Run a model, then explain chat templates, tensors, generation, and decoding. |

The review used public curricula, lesson text, and notebooks. All diagrams and explanations are authored for SteAgent; the slides do not reproduce another course's prose or artwork.

## Teaching boundaries

- The weights are pretrained. “From scratch” refers to assembling the agent's control flow.
- History is a list passed back to the model. It is neither training nor persistent storage.
- Chapter 05 executes an explicit request; Chapter 06 lets the model select an action but stops after execution.
- Chapter 07 feeds the observation back to the model. This changed edge creates the agent loop.
- Chapter 08 counts model calls per user turn. A single response can request multiple tools.
- Example model wording can vary. Tool results are produced by the actual Python function.
- Token blocks are schematic; they do not claim a particular tokenizer's exact boundaries.
