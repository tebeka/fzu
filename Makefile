venv = /tmp/fzu-install-test

all:
	$(error please pick a target)


.PHONY: test
test:
	find . -name '*.pyc' -exec rm {} \;
	flake8 fzu tests
	python -m pytest -v tests

.PHONY: sdist
sdist:
	rm -rf dist
	rm -rf build
	rm -rf fzu.egg-info
	python setup.py sdist

.PHONY: pypi
pypi: sdist
	twine upload dist/fzu-*.tar.gz

.PHONY: circleci
circleci:
	docker build -f Dockerfile.test .

.PHONY: test-install
test-install: sdist
	rm -rf /tmp/fzu-$(USER)
	rm -fr $(venv)
	virtualenv $(venv)
	$(venv)/bin/python -m pip install dist/fzu-*.tar.gz
	$(venv)/bin/fzu

.PHONY: app
app:
	rm -rf build/app
	mkdir -p build/app
	cp -r fzu build/app
	cp $(shell which fzf) build/app/fzu/fzf
	mkdir -p dist
	python -m zipapp build/app/fzu -p '/usr/bin/env python3' -o dist/fzu
	rm -rf build/app
