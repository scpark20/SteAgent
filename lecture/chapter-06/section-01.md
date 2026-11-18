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

# Route the response, then execute once

<div class="split ">
<div>

<div class="code-meta">code/chapter-06/agent.py · route</div>

<!-- code: @code/chapter-06/agent.py#route -->



<div class="code-meta">code/chapter-06/agent.py · tool_node</div>

<!-- code: @code/chapter-06/agent.py#tool_node -->

| Response | Branch |
|---|---|
| No tool calls | END |
| Non-empty `tool_calls` | tools |

</div>
<div>

<div class="figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 270" role="img"><g font-family="Inter,Arial,sans-serif"><rect x="4" y="60" width="91" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="49" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">START</text><rect x="176" y="48" width="180" height="76" rx="12" fill="#e0f3ec" stroke="#a8d8c8"/><text x="266" y="80" font-size="21" fill="#19354e" text-anchor="middle" font-weight="600">assistant</text><text x="266" y="105" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">call_model()</text><rect x="440" y="60" width="94" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="487" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">END</text><path d="M98 85 L170 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="162,80 170,85 162,90" fill="none" stroke="#00868b" stroke-width="2"/><path d="M361 85 L434 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="426,80 434,85 426,90" fill="none" stroke="#00868b" stroke-width="2"/><text x="400" y="65" font-size="14" fill="#19354e" text-anchor="middle" font-weight="400">answer</text><rect x="191" y="188" width="150" height="56" rx="12" fill="#fff4dd" stroke="#ead6a3"/><text x="266" y="222" font-size="20" fill="#19354e" text-anchor="middle" font-weight="600">tools</text><path d="M292 130 L292 181" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="287,173 292,181 297,173" fill="none" stroke="#00868b" stroke-width="2"/><text x="308" y="160" font-size="15" fill="#19354e" text-anchor="start" font-weight="400">tool_calls</text><path d="M342 216 H487 V118" fill="none" stroke="#00868b" stroke-width="2"/><path d="M487 130 L487 115" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="482,123 487,115 492,123" fill="none" stroke="#00868b" stroke-width="2"/></g></svg></div>



<div class="small">

The tool node appends observations to the message list. Multiple calls in one response execute sequentially here.

This checkpoint stops after execution. A tool-request prompt can therefore end with `{"result": 42}` rather than a final model answer.

</div>

</div>
</div>
