
build: style types test

venv/bin:
	python3.11 -m venv venv

install: venv/bin
	pip3 install -r requirements.txt

style:
	flake8 serlib tests

types:
	mypy .

test:
	coverage run --source serlib -m unittest discover
	coverage html
	coverage report --fail-under=90

deploy:	build git-clean
	git push
	
git-clean:
	git diff-index --quiet HEAD
	test -z "$(git status --porcelain)"

run:
	./run.py

clean:
	rm -rf **/__pycache__
	rm -rf **/*.pyc
