.PHONY: clean venv install analysis test test-install cover

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt; pip install -e .

test-install:
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 tests --max-complexity 10
	. venv/bin/activate; flake8 tradewave --max-complexity 10

test: analysis
	. venv/bin/activate; nosetests

cover:
	. venv/bin/activate; nosetests --with-coverage --cover-package=tradewave

clean:
	rm -rf venv