install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build: poetry build 

publish: # отладка публикации
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	poetry check

check: selfcheck test lint