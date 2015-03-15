SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " make install	to install package."
	@echo " make release    to release to the PyPI."
	@echo " make test       to run test suite."
	@echo " make coverage   to run test suite with coverage."

install:
	python setup.py install

release:
	python setup.py sdist upload

test:
	tox -e test

coverage:
	tox -e coverage