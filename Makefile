.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "BB Consent API"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

bootstrap: resources/ssl/development ## Boostraps development environment
	make -C resources/ssl/development bootstrap

up: bootstrap ## Run nginx server with swagger ui
	docker-compose up -d

down: ## Stop the nginx server
	docker-compose down
