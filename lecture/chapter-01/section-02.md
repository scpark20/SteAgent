---
marp: true
theme: steslide
size: 16:9
paginate: false
---

<!-- _class: code -->
# Load weights once

<!-- code: @code/chapter-01/agent.py#load_model -->

---

# What this code does

The tokenizer maps text to token IDs. The model holds pretrained weights. Reuse the loaded pair between calls. FP8 checkpoints are dequantized during loading.
