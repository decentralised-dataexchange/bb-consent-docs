.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "BB Consent API"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

check-swagger-cli:
	@which swagger-cli > /dev/null || (echo "\033[31mPlease install swagger-cli before proceeding.\033[0m" && exit 1)

bootstrap: resources/ssl/development ## Boostraps development environment
	make -C resources/ssl/development bootstrap

up: bootstrap ## Run nginx server with swagger ui
	docker-compose up -d

down: ## Stop the nginx server
	docker-compose down

bundle: check-swagger-cli ## Bundles swagger files
	swagger-cli bundle openapi.yaml -o bundled.yaml -t yaml