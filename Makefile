migrate:
	export TEST_MODE=True \
	&& alembic stamp head  \
	&& alembic revision --autogenerate \
	&& alembic upgrade head 

test:
	rm ./test.sql \
	&& make migrate \
	&& pytest

build-image:
	docker-compose build

runapi:
	docker-compose up --force-recreate