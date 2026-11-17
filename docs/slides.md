# Slide guide

[← SteAgent](../README.md) · [Usage guide](usage.md) · [Architecture](architecture.md)

Shared tooling comes from the [SteSlide](https://github.com/scpark20/SteSlide) submodule at `tools/steslide`. Lecture sources belong to this project. Add only the content requested by the author, and write repository content in English.

## Preview

After cloning, run from the SteAgent root:

```bash
git submodule update --init --recursive
python3 tools/steslide/scripts/setup_marp.py
bash lectures/preview.sh
```

Open <http://localhost:8766/lecture.md>. Saved source changes update the preview automatically. With Remote SSH, forward port `8766` in VS Code.

## Sources

- `lecture-01/intro.md`: Lecture introduction
- `lecture-01/chapter-01/intro.md`: LLM
- `lecture-01/chapter-02/intro.md`: Ollama
- `lecture-01/chapter-03/intro.md`: LangGraph
- Each chapter's `section-01.md`: Hello World!!!
- `lecture.md`, `chapter.md`: Generated decks that include child content

Paths above are relative to `lectures/`. The [course outline](curriculum.md) is a planning document; detailed lesson content has not been populated.

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
