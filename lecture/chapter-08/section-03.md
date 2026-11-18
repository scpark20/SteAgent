---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Return errors as observations

<!-- code: @code/chapter-08/agent.py#execute_tool -->

---

# What this code does

Unknown tools and invalid arguments become tool error messages. The model can observe the failure instead of assuming execution succeeded.
