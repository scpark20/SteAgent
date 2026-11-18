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

# Load weights and get the first reply

<div class="split code-layout">
<div>

<div class="code-meta">code/chapter-01/agent.py · load_model</div>

<!-- code: @code/chapter-01/agent.py#load_model -->

</div>
<div>

<div class="small">

### What is loaded?

- **Config:** architecture and quantization.
- **Tokenizer:** vocabulary and formatting.
- **Model:** pretrained parameters on available devices.

Apple Silicon uses MPS with FP16. Other devices follow checkpoint precision. FP8 checkpoints are dequantized.

`eval()` selects inference behavior.

</div>

<div class="terminal">



```bash
uv run --extra llm code/chapter-01/agent.py
```



</div>
<div class="output">Hello World!!!</div>

</div>
</div>
