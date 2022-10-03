setup: requirements.txt
	pip3 install --user -r requirements.txt
	pip3 install --user .

test:
	python3 -m unittest discover -s tests

build_dist:
	rm -rf dist
	python3 -m build

upload_test: build_dist
	python3 -m twine upload --repository testpypi dist/*

upload: build_dist
	python3 -m twine upload dist/* -u __token__ -p $(PYPI_TOKEN)