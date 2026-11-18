---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: compact -->
<!-- footer: "STEAGENT · 02 / Ollama" -->

<div class="eyebrow">02 / Ollama</div>

# Move inference behind an HTTP API

<div class="split ">
<div>

The caller still sends messages and receives an assistant message. Ollama now loads the weights, prepares tensors, and runs inference.

<div class="terminal">



```bash
uv run code/chapter-02/agent.py \
  "What is 2 + 3? Reply with only the number."
```



</div>
<div class="output">5</div>

<div class="small">

Use `OLLAMA_MODEL` and `OLLAMA_BASE_URL` to select the server and model.

</div>

</div>
<div>

<div class="figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 260" role="img"><g font-family="Inter,Arial,sans-serif"><rect x="2" y="35" width="210" height="155" rx="12" fill="#fff" stroke="#cbd9e5"/><rect x="310" y="35" width="226" height="155" rx="12" fill="#e7f4f1" stroke="#b0d8cc"/><text x="107" y="70" font-size="19" fill="#19354e" text-anchor="middle" font-weight="600">Your Python process</text><text x="107" y="110" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">call_model(messages)</text><text x="107" y="145" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">JSON client</text><text x="423" y="70" font-size="20" fill="#19354e" text-anchor="middle" font-weight="600">Ollama server</text><text x="423" y="110" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">model + tokenizer</text><text x="423" y="145" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">GPU inference</text><path d="M217 89 L303 89" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="295,84 303,89 295,94" fill="none" stroke="#00868b" stroke-width="2"/><path d="M303 152 L217 152" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="225,147 217,152 225,157" fill="none" stroke="#00868b" stroke-width="2"/><text x="260" y="76" font-size="14" fill="#19354e" text-anchor="middle" font-weight="400">request</text><text x="260" y="176" font-size="14" fill="#19354e" text-anchor="middle" font-weight="400">message</text><text x="270" y="231" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">POST /api/chat · localhost:11434</text></g></svg></div>

| Remove from client | Keep |
|---|---|
| Model and tokenizer loading | Message list |
| Tensor/device management | `call_model(messages)` |
| `generate()` | The same CLI and return shape |

</div>
</div>
