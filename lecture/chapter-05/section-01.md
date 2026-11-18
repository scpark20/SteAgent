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

# Execute a request before involving the model

<div class="split ">
<div>

<div class="code-meta">code/chapter-05/agent.py · execute_tool</div>

<!-- code: @code/chapter-05/agent.py#execute_tool -->



```python
REGISTRY = {"add": add}
```

</div>
<div>

```json
{
  "function": {
    "name": "add",
    "arguments": {"a": 2, "b": 3}
  }
}
```



<div class="small">

Look up the callable by name, unpack the argument dictionary, execute Python, then serialize the result as a tool message.

</div>

</div>
</div><div class="terminal">



```bash
uv run code/chapter-05/agent.py --tool-demo
```



</div>
<div class="output">{&quot;result&quot;: 5}</div>
