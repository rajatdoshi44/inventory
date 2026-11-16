.PHONY: inventory create-tables

inventory:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run uvicorn services.inventory.main:app --reload --port 8001

company:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run uvicorn services.company.main:app --reload --port 8002

run-all:
	$(MAKE) inventory &
	$(MAKE) company &

create-tables:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run python -m shared.db.main

drop-tables:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run python -m shared.db.main drop


