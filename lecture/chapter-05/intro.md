---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 05 / Tools" -->

<div class="eyebrow">05 / Tools</div>

# Define one action and its input contract

<div class="split ">
<div>

<div class="code-meta">code/chapter-05/agent.py · TOOLS</div>

<!-- code: @code/chapter-05/agent.py#TOOLS -->

</div>
<div>

<div class="code-meta">code/chapter-05/agent.py · add</div>

<!-- code: @code/chapter-05/agent.py#add -->

| Schema element | Connection to Python |
|---|---|
| `name: "add"` | Registry key |
| `properties` | Keyword argument names |
| `required` | Expected input fields |
| `type: number` | Declared value type |



<div class="note">A schema describes expectations. Type hints and schema text do not replace runtime validation in the host.</div>

</div>
</div>
