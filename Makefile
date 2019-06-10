venv = /tmp/fzu-install-test

all:
	$(error please pick a target)

.PHONY: sdist
sdist:
	rm -rf dist
	rm -rf build
	rm -rf fzu.egg-info
	python setup.py sdist

.PHONY: pypi
pypi: sdist
	twine upload dist/fzu-*.tar.gz

.PHONY: test-install
test-install: sdist
	rm -fr $(venv)
	virtualenv $(venv)
	$(venv)/bin/python -m pip install dist/fzu-*.tar.gz

.PHONY: app
app:
	mkdir -p dist
	python -m zipapp fzu -p '/usr/bin/env python3' -o dist/fzu
