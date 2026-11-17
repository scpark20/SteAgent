# 슬라이드 가이드

[← SteAgent](../README.md) · [실행 가이드](usage.md) · [동작 구조](architecture.md)

공통 도구는 [SteSlide](https://github.com/scpark20/SteSlide) 서브모듈(`tools/steslide`)에서 받습니다. 이 폴더에는 SteAgent 강의 원본을 둡니다. 강의 내용은 사용자가 요청한 것만 추가합니다.

프로젝트를 처음 받은 후, SteAgent 루트에서 실행합니다.

```bash
git submodule update --init --recursive
python3 tools/steslide/scripts/setup_marp.py
bash lectures/preview.sh
```

미리보기: <http://localhost:8766/lecture.md>. 저장하면 자동 갱신됩니다. Remote SSH에서는 VS Code에서 `8766` 포트를 전달합니다.

- `lecture-01/intro.md`: Lecture 도입부
- `lecture-01/chapter-01/intro.md`: LLM
- `lecture-01/chapter-02/intro.md`: Ollama
- `lecture-01/chapter-03/intro.md`: LangGraph
- `lecture-01/chapter-01/section-01.md`: Section 내용
- `lecture.md`, `chapter.md`: 하위 내용까지 포함하는 자동 생성 파일

직접 생성하거나 PDF로 내보내려면:

```bash
python3 tools/steslide/steslide.py build
python3 tools/steslide/steslide.py export --format pdf
```

현재 서버의 Snap Firefox 실행 파일을 직접 지정할 때:

```bash
python3 tools/steslide/steslide.py export --format pdf \
  --browser firefox --browser-path /snap/firefox/current/usr/lib/firefox/firefox
```

최신 SteSlide 버전 받기:

```bash
git submodule update --init --remote --merge tools/steslide
git add tools/steslide
git commit -m "Update SteSlide version"
git push
```

공통 생성기나 테마는 `tools/steslide` 안에서 고쳐 **SteSlide에 먼저 커밋·푸시**하고, SteAgent에는 바뀐 서브모듈 버전을 커밋합니다. 자세한 명령은 [SteSlide 사용법](https://github.com/scpark20/SteSlide/blob/main/docs/usage.md)과 [유지보수](https://github.com/scpark20/SteSlide/blob/main/docs/maintenance.md)에 있습니다. Python 도구를 갱신한 뒤에는 미리보기를 다시 실행합니다.
