.PHONY: test lint build

test:
	uv run python -m pytest -v

lint:
	ruff check src/betelgeuse
	ruff check tests

build:
	uv build
	cd docs && npm install && npm run build
