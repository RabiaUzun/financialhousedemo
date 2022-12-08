install:
	@export PIPENV_VENV_IN_PROJECT="enabled" && pipenv install --pre --dev
	@.venv/bin/pre-commit install

start:
	@pipenv run ./start-dev

test:
	@pipenv run pytest --cov-report=term-missing