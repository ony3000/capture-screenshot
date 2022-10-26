# capture-screenshot
python, selenium을 이용한 페이지 캡처 프로그램

## Environment
- Python 3.9
- [Poetry](https://python-poetry.org/)
- [Selenium](https://www.selenium.dev/)
- [Black](https://black.readthedocs.io/en/stable/)
- [mypy](http://www.mypy-lang.org/)

### How to run a script
1. Copy `src/example_list.csv` to make `src/capture_list.csv`.
2. Modify `src/capture_list.csv` appropriately to list the names and URLs of the sites you want to capture the screen from.
3. Run command below.
   - After virtualenv is activated: `(.venv) $ python src/main.py`<br>
   or
   - Using poetry: `$ poetry run python src/main.py`
