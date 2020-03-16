BUILD   ?= build
DIST    ?= dist
PYTHON  ?= python3
PACKAGE ?= $(shell basename $(shell pwd))
PYTEST  ?= $(PYTHON) -m pytest

help:
	@echo "===================================================================="
	@echo " Makefile: github.com/butuzov/easydecks - rountine tasks automation     "
	@echo "===================================================================="
	@echo ""
	@cat $(MAKEFILE_LIST) | \
		grep -E '^# ~~~ .*? [~]+$$|^[a-zA-Z0-9_-]+:.*?## .*$$' | \
		awk '{if ( $$1=="#" ) {\
			match($$0, /^# ~~~ (.+?) [~]+$$/, a);\
			{print "\n", a[1], "\n"}\
		} else { \
			match($$0, /^([a-zA-Z-]+):.*?## (.*)$$/, a); \
			{printf "  - \033[32m%-20s\033[0m %s\n",   a[1], a[2]} \
		};}'
	@echo ""

venv:
	@if [ -z "${VIRTUAL_ENV}" ]; then\
		echo ">>>>> You need to run this test in virtual environment. Abort!";\
		exit 1;\
	fi

install: venv ## Dev Installs Reqired Packages
	python3 -m pip install setuptools twine -q
	python3 -m pip install yapf pylint pytest -q
	python3 -m pip install -e .


clean: ## Cleanup Build artifacts
	@rm -rf ${DIST}
	@rm -rf ${BUILD}

.PHONY: tests
tests:  ## Tests
	$(PYTEST)

build: venv clean ## Build disto (source) - Production
	@ $(PYTHON) setup.py sdist  > /dev/null 2>&1

deploy-test:  build  ## PyPi Deploy (test.pypi.org)
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*;\
	$(MAKE) clean

deploy-prod: build  ## PyPi Deploy (pypi.org)
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*;\
	$(MAKE) clean
