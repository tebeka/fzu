venv = /tmp/fzu-install-test

all:
	$(error please pick a target)

sdist:
	rm -f dist/fzu-*.tar.gz
	python setup.py sdist

pypi: sdist
	twine upload dist/fzu-*.tar.gz


test-install: sdist
	virtualenv $(venv)
	$(venv)/bin/python -m pip install dist/fzu-*.tar.gz
	test -d $(venv)/lib/python3.7/site-packages/fzu/symbols
