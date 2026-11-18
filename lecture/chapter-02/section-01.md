---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 02 / Ollama" -->

<div class="eyebrow">02 / Ollama</div>

# Read the request and the returned message

<div class="split code-layout">
<div>

<div class="code-meta">code/chapter-02/agent.py · call_model</div>

<!-- code: @code/chapter-02/agent.py#call_model -->

</div>
<div>

<div class="small">

| Payload field | Purpose |
|---|---|
| `messages` | Conversation input |
| `stream=False` | A complete JSON response |
| `think=False` | Request non-thinking behavior |
| `temperature=0` | Reduce randomness |
| Context / generation | 4096 / 256 tokens |

Encode the payload as JSON bytes. Extract `message` from the response.

The timeout is **120 seconds**. Generation remains autoregressive.

</div>

</div>
</div>
