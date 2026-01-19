.PHONY: help install install-dev test test-verbose test-cov lint format type-check clean build all

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
	pip install -e .

install-dev:
	pip install -r dev-requirements.txt
	pip install -e .

test:
	pytest

test-verbose:
	pytest -v

test-cov:
	pytest --cov=triangle --cov=circle --cov-report=term-missing --cov-report=html

lint:
	ruff check triangle/ circle/

format:
	black triangle/ circle/

format-check:
	black --check triangle/ circle/

type-check:
	mypy triangle/triangle.py circle/circle.py

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
	python -m build

all: format lint type-check test
	@echo "✓ All checks passed!"
