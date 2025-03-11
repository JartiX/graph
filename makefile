OS := $(shell uname 2>/dev/null || echo Windows)

help:
	@echo "Make project with following instructions"
	@cat Makefile

dev:
	pipenv install --dev

test: dev
	pipenv run pytest --doctest-modules --junitxml=junit/test-results.xml

build: clean
	pipenv install wheel
	pipenv run python setup.py sdist bdist_wheel

clean:
ifeq ($(OS), Windows)
	@if exist .pytest_cache rd /s /q .pytest_cache
	@if exist .mypy_cache rd /s /q .mypy_cache
	@if exist junit rd /s /q junit
	@if exist build rd /s /q build
	@if exist dist rd /s /q dist
	@for /d %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
	@for /d %%d in (*.egg-info) do @if exist "%%d" rd /s /q "%%d"
else
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete
endif
