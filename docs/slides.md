# Slide guide

[← SteAgent](../README.md) · [Usage guide](usage.md) · [Architecture](architecture.md)

Shared tooling comes from the [SteSlide](https://github.com/scpark20/SteSlide) submodule at `tools/steslide`. Lecture sources belong to this project. Add only the content requested by the author, and write repository content in English.

## Preview

After cloning, run from the SteAgent root:

```bash
git submodule update --init --recursive
python3 tools/steslide/scripts/setup_marp.py
bash lecture/preview.sh
```

Open <http://localhost:8766/lecture.md>. Saved source changes update the preview automatically. With Remote SSH, forward port `8766` in VS Code.

## Sources

There is one lecture: `lecture/` itself.

```text
code/
├── chapter-01/agent.py
└── chapter-02/ ... chapter-08/
lecture/
├── intro.md
├── chapter-01/section-01.md
├── chapter-02/ ... chapter-08/
├── lecture.md                 # Generated parent preview
└── preview.sh
```

Edit Markdown in `lecture/` and Python in `code/`. A directive such as `<!-- code: @code/chapter-02/agent.py#call_model -->` includes the real function in the generated slide. Saving Python also refreshes the preview. Chapter 02 onward includes `changes.diff` for source comparison.

## Build and export

```bash
python3 tools/steslide/steslide.py build
python3 tools/steslide/steslide.py export --format pdf
```

If Firefox is installed through Snap and automatic detection fails, specify its executable:

```bash
python3 tools/steslide/steslide.py export --format pdf \
  --browser firefox --browser-path /snap/firefox/current/usr/lib/firefox/firefox
```

## Update the shared tool

```bash
git submodule update --init --remote --merge tools/steslide
git add tools/steslide
git commit -m "Update SteSlide version"
git push
```

Edit shared generators and themes inside `tools/steslide`, commit and push to **SteSlide first**, then record the updated submodule commit in SteAgent. See the [SteSlide usage guide](https://github.com/scpark20/SteSlide/blob/main/docs/usage.md) and [maintenance guide](https://github.com/scpark20/SteSlide/blob/main/docs/maintenance.md). Restart the preview after Python tooling updates.
