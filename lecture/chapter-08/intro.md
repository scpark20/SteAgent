---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 08 / Minimal Agent" -->

<div class="eyebrow">08 / Minimal Agent</div>

# Validate what the model actually sends

<div class="split ">
<div>

<div class="code-meta">code/chapter-08/agent.py · add</div>

<!-- code: @code/chapter-08/agent.py#add -->

</div>
<div>

| Input | Outcome |
|---|---|
| `12, 30` | Return 42 |
| `"12", 30` | Reject string |
| `True, 30` | Reject boolean |
| `NaN` or infinity | Reject non-finite input |
| Non-finite sum | Reject the result |



<div class="small">

Python booleans are integer-like, so the explicit boolean check matters. Checking the result also catches floating-point overflow.

The model’s schema guides generation; the function protects the actual execution boundary.

</div>

</div>
</div>
