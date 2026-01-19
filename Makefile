.PHONY: help install install-dev test test-verbose test-cov lint format type-check clean build all

PYTHON := .venv/bin/python
PIP := .venv/bin/pip

help:
	@echo "Shapes Package - Available Make Commands"
	@echo "=========================================="
	@echo "help           - Show this help message"
	@echo "install        - Install the package"
	@echo "install-dev    - Install package with development dependencies"
	@echo "test           - Run all tests"
	@echo "test-verbose   - Run tests with verbose output"
	@echo "test-cov       - Run tests with coverage report"
	@echo "lint           - Run ruff linter"
	@echo "format         - Format code with black"
	@echo "format-check   - Check code formatting without modifying"
	@echo "type-check     - Run mypy type checker"
	@echo "clean          - Remove build artifacts and cache files"
	@echo "build          - Build the package"
	@echo "all            - Run format, lint, type-check, and test"

install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -r dev-requirements.txt
	$(PIP) install -e .

test:
	$(PYTHON) -m pytest

test-verbose:
	$(PYTHON) -m pytest -v

test-cov:
	$(PYTHON) -m pytest --cov=shapes/triangle --cov=shapes/circle --cov=shapes/rectangles --cov-report=term-missing --cov-report=html

lint:
	$(PYTHON) -m ruff check shapes/triangle/ shapes/circle/ shapes/rectangles/

format:
	$(PYTHON) -m black shapes/triangle/ shapes/circle/ shapes/rectangles/

format-check:
	$(PYTHON) -m black --check shapes/triangle/ shapes/circle/ shapes/rectangles/

type-check:
	$(PYTHON) -m mypy shapes/triangle/triangle.py shapes/circle/circle.py shapes/rectangles/rectangle.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	$(PYTHON) -m build

all: format lint type-check test
	@echo "✓ All checks passed!"
