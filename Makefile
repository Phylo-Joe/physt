.PHONY: help venv install clean lint test format

help:
	@echo "Available targets:"
	@echo "  make venv     - Create virtual environment"
	@echo "  make install  - Install project with dev dependencies"
	@echo "  make lint     - Run pre-commit on all files"
	@echo "  make test     - Run pytest"
	@echo "  make format   - Run black and isort"
	@echo "  make clean    - Remove virtual environment"

venv:
	python3 -m venv .venv

install:
	.venv/bin/pip install -e .[dev]

lint:
	.venv/bin/pre-commit run --all-files

test:
	.venv/bin/pytest

format:
	.venv/bin/isort src tests
	.venv/bin/black src tests

clean:
	rm -rf .venv
