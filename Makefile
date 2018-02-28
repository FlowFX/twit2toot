init:
    pip install pipenv
    pipenv install --dev
    # Use empty secrets file. Its contents are not used by the test suite.
    cp .travis/secrets.json.sample secrets.json
test:
    pipenv run pytest --cov