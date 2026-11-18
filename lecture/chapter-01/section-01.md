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

# Generate tokens, then decode the new suffix

<div class="split code-layout">
<div>

<div class="code-meta">code/chapter-01/agent.py · call_model</div>

<!-- code: @code/chapter-01/agent.py#call_model -->

</div>
<div>

<div class="small">

1. Reuse the cached model and tokenizer.
2. Apply role markers with the chat template.
3. Convert text to tensors on the model device.
4. Generate without gradient bookkeeping.
5. Decode only tokens after the input prefix.

</div>

<div class="formula">

$$p_\theta(y\mid x)=\prod_t p_\theta(y_t\mid x,y_{<t})$$

</div>



<div class="small">

`do_sample=False` chooses the highest-scoring token at each step. `max_new_tokens=128` is a cap, not a required length. An end token can stop generation earlier.

</div>

</div>
</div>
