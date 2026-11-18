---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: annotated -->
<!-- footer: "STEAGENT · 06 / Tool Calling" -->

<div class="eyebrow">06 / Tool Calling</div>

# Let the model propose the action

<div class="split ">
<div>

<div class="code-meta">code/chapter-06/agent.py · assistant</div>

<!-- code: @code/chapter-06/agent.py#assistant -->



<div class="code-meta">code/chapter-06/agent.py · call_model[9:10]</div>

<!-- code: @code/chapter-06/agent.py#call_model[9:10] -->



<div class="small">

The schema is attached to the request. The assistant returns its proposed action as structured data. Execution still belongs to the host.

</div>

</div>
<div>

```json
{
  "role": "assistant",
  "tool_calls": [{
    "function": {
      "name": "add",
      "arguments": {"a": 12, "b": 30}
    }
  }]
}
```



<div class="note">This is a request to call <code>add</code>. The value 42 does not exist as a tool result until Python runs.</div>

</div>
</div>
