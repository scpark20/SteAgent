---
marp: true
theme: steslide
size: 16:9
paginate: true
math: katex
---

<!-- _class: lesson -->
<!-- footer: "STEAGENT · 07 / Agent Loop" -->

<div class="eyebrow">07 / Agent Loop</div>

# Change one edge to create feedback

<div class="split ">
<div>

```diff
- builder.add_edge("tools", END)
+ builder.add_edge("tools", "assistant")
```



<div class="small">

The next assistant invocation receives the entire history, including the action request and the tool’s result.

It can answer using the observation or request another action. The adapter, registry, and executor are unchanged.

</div>

</div>
<div>

<div class="figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 270" role="img"><g font-family="Inter,Arial,sans-serif"><rect x="4" y="60" width="91" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="49" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">START</text><rect x="176" y="48" width="180" height="76" rx="12" fill="#e0f3ec" stroke="#a8d8c8"/><text x="266" y="80" font-size="21" fill="#19354e" text-anchor="middle" font-weight="600">assistant</text><text x="266" y="105" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">call_model()</text><rect x="440" y="60" width="94" height="51" rx="24" fill="#eaf0f6" stroke="#cbd9e5"/><text x="487" y="92" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">END</text><path d="M98 85 L170 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="162,80 170,85 162,90" fill="none" stroke="#00868b" stroke-width="2"/><path d="M361 85 L434 85" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="426,80 434,85 426,90" fill="none" stroke="#00868b" stroke-width="2"/><text x="400" y="65" font-size="14" fill="#19354e" text-anchor="middle" font-weight="400">answer</text><rect x="191" y="188" width="150" height="56" rx="12" fill="#fff4dd" stroke="#ead6a3"/><text x="266" y="222" font-size="20" fill="#19354e" text-anchor="middle" font-weight="600">tools</text><path d="M292 130 L292 181" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="287,173 292,181 297,173" fill="none" stroke="#00868b" stroke-width="2"/><text x="308" y="160" font-size="15" fill="#19354e" text-anchor="start" font-weight="400">tool_calls</text><path d="M190 216 H136 V86 H169" fill="none" stroke="#00868b" stroke-width="3"/><path d="M158 86 L171 86" fill="none" stroke="#00868b" stroke-width="2"/><polyline points="163,81 171,86 163,91" fill="none" stroke="#00868b" stroke-width="2"/><text x="78" y="177" font-size="16" fill="#19354e" text-anchor="middle" font-weight="400">result</text></g></svg></div>

</div>
</div>

<div class="note">This is the behavioral change from one-shot tool execution to a tool-using agent loop.</div>
