---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 03 / LangGraph" -->

<div class="eyebrow">03 / LangGraph</div>

# Trace the state through one invocation

<div class="split ">
<div>

<div class="code-meta">code/chapter-03/agent.py · State</div>

<!-- code: @code/chapter-03/agent.py#State -->



<div class="code-meta">code/chapter-03/agent.py · assistant</div>

<!-- code: @code/chapter-03/agent.py#assistant -->



```python
state = graph.invoke({"messages": messages})
```

</div>
<div>

| Moment | Message list |
|---|---|
| Input | `[user]` |
| Node reads | `[user]` |
| Node returns | `[user, assistant]` |
| Caller receives | Updated state dictionary |



<div class="note">The node returns the <b>whole new list</b>. No append reducer is configured; the state key uses replacement semantics.</div>



<div class="small">

`TypedDict` documents the shape for type checking. It does not validate the contents at runtime.

</div>

</div>
</div>
