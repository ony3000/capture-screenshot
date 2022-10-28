# capture-screenshot
python, selenium을 이용한 페이지 캡처 프로그램<br>
(단, 스크롤 위치에 따라 동적으로 변하는 페이지의 경우, 캡처 결과가 예상과 다를 수 있다)

## Environment
- Python 3.9
- [Poetry](https://python-poetry.org/)
- [Selenium](https://www.selenium.dev/)
- [Black](https://black.readthedocs.io/en/stable/)
- [mypy](http://www.mypy-lang.org/)
- 이 프로그램을 실행하려는 기기에 설치된 크롬 브라우저

### How to run a script
1. `src/example_list.csv`를 복사해서 `src/capture_list.csv`를 만든다.
2. `src/capture_list.csv`를 적당히 수정하여, 화면을 캡처하려는 사이트의 이름과 URL 목록을 작성한다.
3. 아래 명령어를 실행한다.
   - virtualenv 활성화 상태에서: `(.venv) $ python src/main.py [--width=375]`<br>
   또는
   - poetry 사용하기: `$ poetry run python src/main.py [--width=375]`
