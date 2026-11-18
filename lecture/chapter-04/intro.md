---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 04 / State & Memory" -->

<div class="eyebrow">04 / State & Memory</div>

# Remember a name across two turns

<div class="split ">
<div>

<div class="code-meta">code/chapter-04/agent.py · main[7:15]</div>

<!-- code: @code/chapter-04/agent.py#main[7:15] -->



<div class="small">

The list is created before the loop and replaced with the graph’s returned history after every turn.

</div>

</div>
<div>

<div class="terminal">



```bash
uv run code/chapter-04/agent.py \
  "My name is Ada." --chat
```



</div>
<div class="output">Next question: What is my name? → Ada</div>

<div class="small">

Append the next user message to the retained list. The model sees earlier turns because they are sent again—not because its weights changed.

Memory lasts only while this process is running.

</div>

<div class="formula">

$$N_{\mathrm{input}}+N_{\mathrm{generated}}\le C$$

</div>



<div class="small">

The configured context is 4096 tokens. This example has no explicit history-trimming policy.

</div>

</div>
</div>
