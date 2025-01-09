install:
	uv sync

brain-games:
	uv run brain-games

brain-calc:
	uv run brain-calc

brain-even:
	uv run brain-even

brain-gcd:
	uv run brain-gcd

brain-prime:
	uv run brain-prime

brain-progression:
	uv run brain-progression

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	rm -r -f dist/
	uv tool uninstall hexlet-code

lint:
	uv run ruff check brain_games

lint with fix:
	uv run ruff check --fix brain_games