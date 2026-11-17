# 작업 규칙

- 강의 원본은 `lectures/`에 둡니다. 사용자가 지시한 내용만 넣고 예시 강의나 목차를 임의로 채우지 않습니다.
- 슬라이드 공통 도구는 `tools/steslide` Git 서브모듈입니다. 생성기·공통 테마·설치 도구는 그 안에서 수정하고 SteSlide 저장소에 반영합니다. SteAgent에 별도 구현을 만들지 않습니다.
- 슬라이드 원본은 `intro.md`, `section-*.md`입니다. `lecture.md`, `chapter.md`, `.build/`는 자동 생성 파일입니다.
- 공통 도구 업데이트를 반영할 때 SteSlide 변경을 먼저 커밋·푸시한 뒤 SteAgent의 서브모듈 버전을 커밋합니다. 관련 없는 미커밋 변경은 보존합니다.
- 실행 방법과 업데이트 절차는 `lectures/README.md`, `tools/steslide/README.md`를 참고합니다.
