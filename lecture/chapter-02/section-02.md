---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# The same call boundary

<!-- code: @code/chapter-02/agent.py#call_model -->

---

# What this code does

Ollama owns model loading and inference. Python sends the same messages as JSON. stream=False returns one complete response. The caller still reads reply["content"].
