venv = /tmp/fzu-install-test

all:
	$(error please pick a target)

sdist:
	rm -rf dist
	rm -rf build
	rm -rf fzu.egg-info
	python setup.py sdist

pypi: sdist
	twine upload dist/fzu-*.tar.gz


test-install: sdist
	rm -fr $(venv)
	virtualenv $(venv)
	$(venv)/bin/python -m pip install dist/fzu-*.tar.gz
	test -d $(venv)/lib/python3.7/site-packages/fzu/symbols
