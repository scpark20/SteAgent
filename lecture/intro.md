---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: cover -->
<!-- footer: "STEAGENT · COURSE MAP" -->

<div class="eyebrow">COURSE MAP</div>

# Build a minimal agent

<p style="font-size:28px">Start with model inference. Add one capability at a time.</p>

<div class="terminal">

```bash
uv run agent.py "Use add to calculate 12 + 30." --trace
```

</div>

<div style="font-family:monospace;font-size:24px;color:#8ae5d4;margin:20px 0 32px">[tool:add] {"result": 42}<br>12 + 30 = 42.</div>

<p style="font-size:23px">The destination: a model chooses an action, Python executes it,<br>and the model answers using the observed result.</p>

<p style="font-size:18px;margin-top:24px">LLM → Ollama → LangGraph → State → Tools → Tool calling → Loop → Limits</p>
