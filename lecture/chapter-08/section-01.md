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

# Return failures as observations

<div class="split code-layout">
<div>

<div class="code-meta">code/chapter-08/agent.py · execute_tool</div>

<!-- code: @code/chapter-08/agent.py#execute_tool -->

</div>
<div>

```json
{
  "role": "tool",
  "tool_name": "add",
  "content": "{\"error\": \"Arguments must be finite numbers\"}"
}
```



<div class="small">

Unknown tools, missing arguments, and ordinary execution exceptions become error content.

The next model call sees the failure and can revise its request or explain the problem. It is not treated as a successful result.

</div>



<div class="note">Only functions in <code>REGISTRY</code> can be dispatched. The host does not evaluate generated Python.</div>

</div>
</div>
