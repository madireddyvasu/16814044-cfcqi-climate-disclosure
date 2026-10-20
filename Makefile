PYTHON ?= python3
.PHONY: setup test reproduce audit
setup:
	$(PYTHON) -m pip install -r requirements.txt
test:
	pytest -q
reproduce:
	bash run_all.sh
audit:
	$(PYTHON) scripts/07_final_audit.py
