---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# History is state

<!-- code: @code/chapter-04/agent.py#State -->

---

# What this code does

The graph is unchanged. The CLI retains returned messages, then appends the next user message. This memory lives only while the process is running.
