init:
	pip install pipenv
	pipenv install --dev
	cp .travis/secrets.json.sample secrets.json
test:
	pipenv run pytest --cov -m "not api"
