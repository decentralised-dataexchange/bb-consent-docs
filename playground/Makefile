.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "BB Consent Playground"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Run the playground
	docker-compose up -d

down: ## Stop the playground
	docker-compose down

clean: ## Stop and destroy volumes
	docker-compose down -v