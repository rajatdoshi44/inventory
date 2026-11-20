.PHONY: inventory users create-tables

inventory:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run uvicorn services.inventory.main:app --reload --port 8001

users:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run uvicorn services.users.main:app --reload --port 8003

company:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run uvicorn services.company.main:app --reload --port 8002

run-all:
	$(MAKE) inventory &
	$(MAKE) company &
	$(MAKE) users &
	
stop-all:
	@pids=$$(pgrep -f 'services[.](inventory|company|users)[.]main:app' || true); \
	if [ -n "$$pids" ]; then \
		echo "Stopping project services: $$pids"; \
		kill $$pids; \
	else \
		echo "No project services are running."; \
	fi

create-tables:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run python -m shared.db.main

drop-tables:
	cd "$(dir $(abspath $(lastword $(MAKEFILE_LIST))))" && uv run python -m shared.db.main drop


