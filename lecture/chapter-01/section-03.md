---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Generate new tokens

<!-- code: @code/chapter-01/agent.py#call_model -->

---

# What this code does

The chat template marks message roles. generate() appends tokens autoregressively. Decode only the new suffix, excluding the input prompt.
