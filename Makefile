.PHONY: build up test migrate

build:
	docker-compose build

up:
	docker-compose up --build -d

migrate:
	# run alembic upgrade head
	uv run alembic upgrade head

test:
	pytest -q