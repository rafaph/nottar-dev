.PHONY: up down ps

SHELL=/bin/sh

define down
	$(MAKE) down || $(MAKE) down
endef

define compose
	docker compose $(1)
endef

down:
	$(call compose,down --remove-orphans)

up:
	$(call compose,up -d)

ps:
	$(call compose,ps)
