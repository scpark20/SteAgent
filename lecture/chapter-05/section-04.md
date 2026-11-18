---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Describe the tool to the model

<!-- code: @code/chapter-05/agent.py#TOOLS -->

---

# A schema is an interface

- The name identifies a callable in the registry.
- The description tells the model when to request it.
- The parameters describe argument names and types.
- required lists the values the caller must supply.

Chapter 06 sends this schema to the model. Chapter 08 adds runtime validation.
