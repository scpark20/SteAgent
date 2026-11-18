---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Keep the returned messages

<!-- code: @code/chapter-04/agent.py#main -->

---

# The next turn contains the previous one

The messages list is created before the loop. Each iteration appends the user
message, invokes the same graph, then retains its returned history.

The model has no memory outside its input. Keeping the list in Python is what
makes the next question include earlier turns.
