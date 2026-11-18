---
marp: true
theme: steslide
size: 16:9
paginate: false
---

# Run the complete agent

```bash
uv run agent.py "Use add to calculate 12 + 30." --trace
```

1. The model requests `add(a=12, b=30)`.
2. Python executes the function and appends its result.
3. The model receives the result and answers **42**.

---

# Check the boundaries

```bash
uv run python -m unittest discover -s tests -v
```

Verify direct answers, tool execution, repeated calls, invalid arguments,
unknown tools, and the step limit. Scripted model replies make failure
checks deterministic.
