.PHONY: default
default: tests

.PHONY: test
test: ## Run all tests.
	flake8 stdclean tests --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 stdclean tests --count --max-complexity=10 --max-line-length=80 --statistics
	pytest

.PHONY: clean
clean: ## Remove all file artifacts.
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
