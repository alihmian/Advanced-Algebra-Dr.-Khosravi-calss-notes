.DEFAULT_GOAL := slides
LATEXMK ?= latexmk
PYTHON ?= python3
export WILDCAT_REPO

.PHONY: slides lecture questions sources check-sources source-page doctor theme clean
slides: theme
	$(LATEXMK) -jobname=advanced-algebra-slides main.tex

lecture: theme
	$(PYTHON) scripts/lectures.py build "$(LECTURE)" --latexmk "$(LATEXMK)"

questions:
	$(PYTHON) scripts/build-questions.py "$(LECTURE)" --latexmk "$(LATEXMK)"

sources:
	$(PYTHON) scripts/lectures.py list

check-sources:
	$(PYTHON) scripts/lectures.py check

source-page:
	$(PYTHON) scripts/lectures.py render "$(LECTURE)" --page "$(PAGE)" $(if $(VARIANT),--variant "$(VARIANT)")

doctor: theme
	@bash scripts/doctor.sh
	$(PYTHON) scripts/lectures.py check

theme:
	@bash scripts/link-wildcat.sh

clean:
	$(LATEXMK) -C -jobname=advanced-algebra-slides main.tex
