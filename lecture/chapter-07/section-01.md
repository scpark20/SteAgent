---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: compact -->
<!-- footer: "STEAGENT · 07 / Agent Loop" -->

<div class="eyebrow">07 / Agent Loop</div>

# Inspect a complete agent turn

<div class="split ">
<div>

| Step | Who runs? | Message appended |
|---|---|---|
| 1 | User | Request 12 + 30 |
| 2 | Model | `add(a=12, b=30)` |
| 3 | Python | Tool result: 42 |
| 4 | Model | Final answer using 42 |



<div class="small">

The first model call selects the action. The second model call receives the actual observation. A response without tool calls reaches END.

</div>

</div>
<div>

<div class="terminal">



```bash
uv run code/chapter-07/agent.py \
  "Use add to calculate 12 + 30."
```



</div>
<div class="output">The result is 42.</div>| Chapter 06 | Chapter 07 |
|---|---|
| tools → END | tools → assistant |
| Stops at observation | Model reads observation |
| One execution pass | Repeated decisions possible |

</div>
</div>
