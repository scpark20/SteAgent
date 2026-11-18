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

# Stop before another action exceeds the budget

<div class="split ">
<div>

<div class="code-meta">code/chapter-08/agent.py · route</div>

<!-- code: @code/chapter-08/agent.py#route -->



<div class="code-meta">code/chapter-08/agent.py · assistant</div>

<!-- code: @code/chapter-08/agent.py#assistant -->

</div>
<div>

| At the route decision | Result |
|---|---|
| Final answer | END, including at the limit |
| Tool request below limit | Execute tools |
| Tool request at limit | Raise explicit stop |



<div class="small">

`--max-steps` counts **model calls per user turn**. It does not count individual functions: one response can request multiple tools.

The CLI starts a turn with `calls=0`, sets a graph recursion limit, and reports model I/O failures as errors.

</div>



<div class="note">Use a positive call budget. A limit should stop a loop explicitly, rather than silently return an unfinished tool request.</div>

</div>
</div>
