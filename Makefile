.PHONY: default
default: tests

.PHONY: tests
tests:
	python -m pytest


.PHONY: clean
clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
