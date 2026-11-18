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

# Put the existing function inside a graph

<div class="split ">
<div>

<div class="code-meta">code/chapter-03/agent.py · build_graph</div>

<!-- code: @code/chapter-03/agent.py#build_graph -->

</div>
<div>

<div class="figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 270" role="img"><g font-family="Inter,Arial,sans-serif"><rect x="4" y="60" width="91" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="49" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">START</text><rect x="176" y="48" width="180" height="76" rx="12" fill="#e0f3ec" stroke="#a8d8c8"/><text x="266" y="80" font-size="21" fill="#19354e" text-anchor="middle" font-weight="600">assistant</text><text x="266" y="105" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">call_model()</text><rect x="440" y="60" width="94" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="487" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">END</text><path d="M98 85 L170 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="162,80 170,85 162,90" fill="none" stroke="#00868b" stroke-width="2"/><path d="M361 85 L434 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="426,80 434,85 426,90" fill="none" stroke="#00868b" stroke-width="2"/><text x="266" y="185" font-size="18" fill="#19354e" text-anchor="middle" font-weight="400">State travels through the graph.</text></g></svg></div>



<div class="small">

**Node:** a Python function that reads state and returns an update.

**Edges:** the order in which nodes run.

`compile()` produces the object that can be invoked. The model adapter remains unchanged.

</div>

</div>
</div>
