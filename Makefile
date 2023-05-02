install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

tests:
	poetry run pytest