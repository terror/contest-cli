ci: lint test fmt

lint:
  pylint contest_cli

test:
  pytest .

fmt:
  black . --exclude tests

build:
  python3 setup.py sdist
  python3 setup.py build

clean:
  rm -rf dist build contest_cli.egg-info

publish:
  twine upload dist/*

install *pkg:
  pipenv install {{pkg}} --skip-lock

lock:
  pipenv lock --pre
