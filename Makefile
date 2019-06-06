all:
	$(error please pick a target)

sdist:
	rm -f dist/fzu-*.tar.gz
	python setup.py sdist

pypi: sdist
	twine upload dist/fzu-*.tar.gz
