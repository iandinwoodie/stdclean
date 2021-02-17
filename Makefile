.PHONY: default
default: tests

.PHONY: tests
tests:
	flake8 stdclean tests --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 stdclean tests --count --max-complexity=10 --max-line-length=80 --statistics
	pytest

.PHONY: clean
clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
