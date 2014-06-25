.PHONY: clean venv install analysis test test-install cover

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt; pip install -e .

test-install:
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 tests
	. venv/bin/activate; flake8 tradewave

test: analysis
	. venv/bin/activate; nosetests

cover:
	. venv/bin/activate; nosetests --with-coverage --cover-package=tradewave

clean:
	rm -rf venv