# Working on SteAgent

- Store lecture sources in `lectures/`. Add only content requested by the user; do not invent lesson material.
- Write all published documentation, comments, CLI help, prompts, and other repository text in English.
- The course follows LLM → Ollama → LangGraph. Each chapter starts with Hello World!!! and evolves the previous implementation through small, explicit changes. The current design lives in `docs/curriculum.md`.
- Shared slide tooling lives in the `tools/steslide` Git submodule. Make generator, shared theme, and installer changes there and publish them to SteSlide. Do not create a separate implementation in SteAgent.
- Edit `intro.md` and `section-*.md`. Treat `lecture.md`, `chapter.md`, and `.build/` as generated output.
- Publish shared tool changes to SteSlide first, then commit the updated submodule version in SteAgent. Preserve unrelated uncommitted changes.
- See `docs/slides.md` and `tools/steslide/docs/maintenance.md` for preview and update procedures.
