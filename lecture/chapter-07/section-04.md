---
marp: true
theme: steslide
size: 16:9
paginate: false
---

# Change from Chapter 06

Change one edge: tools → END becomes tools → assistant.

```bash
git diff --no-index code/chapter-06/agent.py \
  code/chapter-07/agent.py
```

The complete diff is saved as `changes.diff`.

```diff
- builder.add_edge("tools", END)
+ builder.add_edge("tools", "assistant")
```
