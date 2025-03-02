.PHONY: test lint build

test:
	uv run pytest --cov=src/betelgeuse --cov-report=xml --cov-report=term -v

lint:
	ruff check --config ruff.toml --fix
	ruff format

build:
	uv build
