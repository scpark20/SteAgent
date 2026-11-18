---
marp: true
theme: steslide
size: 16:9
paginate: false
---

# Change from Chapter 01

Replace local loading with HTTP. Preserve messages, call_model(), and the CLI.

```bash
git diff --no-index code/chapter-01/agent.py \
  code/chapter-02/agent.py
```

The complete diff is saved as `changes.diff`.
