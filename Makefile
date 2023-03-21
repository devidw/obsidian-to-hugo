include .env

setup: requirements.txt
	pip3 install --user -r requirements.txt
	pip3 install --user .

install_locally:
	pip3 install --user .

test_unit: install_locally
	python3 -m unittest discover -s tests

test_e2e: install_locally
	python3 -m unittest discover -s tests -p "e2e_*.py"

test: test_unit test_e2e

update_calver: install_locally
	python3 ./scripts/update_calver.py

build_dist: update_calver
	rm -rf dist
	python3 -m build

upload_test: build_dist
	python3 -m twine upload \
		--repository testpypi \
		--username __token__ \
		--password $(PYPI_TEST_TOKEN) \
		dist/*

upload: build_dist
	python3 -m twine upload \
		--username __token__ \
		--password $(PYPI_TOKEN) \
		dist/*