---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Execute a request

<!-- code: @code/chapter-05/agent.py#execute_tool -->

---

# What this code does

The registry maps a name to a callable. Arguments are passed by name. A tool message carries the result. Run the example with --tool-demo to execute add(2, 3).
