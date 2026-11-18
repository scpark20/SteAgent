---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 01 / LLM" -->

<div class="eyebrow">01 / LLM</div>

# Keep one interface for the next step

<div class="split ">
<div>

<div class="code-meta">code/chapter-01/agent.py · main</div>

<!-- code: @code/chapter-01/agent.py#main -->



<div class="note"><code>call_model(messages)</code> is the boundary we will preserve when inference moves into Ollama.</div>

</div>
<div>

<div class="figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 185" role="img"><g font-family="Inter,Arial,sans-serif"><rect x="5" y="35" width="98" height="56" rx="12" fill="#e7edf5" stroke="#cbd9e5"/><text x="54" y="69" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">input</text><rect x="112" y="35" width="98" height="56" rx="12" fill="#e7edf5" stroke="#cbd9e5"/><text x="161" y="69" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">prefix</text><rect x="219" y="35" width="98" height="56" rx="12" fill="#dff3ea" stroke="#cbd9e5"/><text x="268" y="69" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">Hello</text><rect x="326" y="35" width="98" height="56" rx="12" fill="#dff3ea" stroke="#cbd9e5"/><text x="375" y="69" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">World</text><rect x="433" y="35" width="98" height="56" rx="12" fill="#dff3ea" stroke="#cbd9e5"/><text x="482" y="69" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">!!!</text><text x="108" y="121" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">n input tokens</text><text x="379" y="121" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">generated suffix</text><text x="270" y="162" font-size="17" fill="#19354e" text-anchor="middle" font-weight="400">output[0, n:] → decode only new tokens</text></g></svg></div>

| Value | Meaning |
|---|---|
| `messages` | User/system/assistant records |
| `reply` | One assistant message dictionary |
| `reply["content"]` | Text printed by the caller |

<div class="caption">Token blocks are schematic; actual tokenizer boundaries vary.</div>

</div>
</div>
