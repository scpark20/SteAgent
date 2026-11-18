---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: compact -->
<!-- footer: "STEAGENT · 08 / Minimal Agent" -->

<div class="eyebrow">08 / Minimal Agent</div>

# Run and verify the finished agent

<div class="split ">
<div>

<div class="terminal">



```bash
uv run agent.py "Use add for 12 + 30." --trace
uv run python -m unittest discover -s tests -v
```



</div>
<div class="output">[tool:add] {&quot;result&quot;: 42}</div>

<div class="small">

Use `--chat` to retain history. `--trace` prints actual tool observations. The final model wording can vary.

</div>

</div>
<div>

| Check | Evidence |
|---|---|
| Greeting | No tool execution |
| Addition | Result is fed back to the model |
| Repeated calls | Observations stay in history |
| Bad tool or arguments | Error observation |
| Budget exhausted | No next action is dispatched |



<div class="small">

The runnable checkpoints are in `code/`; explanations are in `lecture/`. Compare adjacent checkpoints with their `changes.diff`.

</div>

</div>
</div><div class="micro" style="margin-top:16px">Teaching structure informed by <a href="https://academy.langchain.com/courses/intro-to-langgraph">LangChain Academy</a> and the <a href="https://huggingface.co/learn/llm-course/chapter2/2">Hugging Face LLM Course</a>. The diagrams and explanations are authored for this implementation.</div>
