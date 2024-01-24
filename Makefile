###### commands for build Docker container:
up:
	docker compose -f docker-compose.yml up -d --build

down:
	docker compose -f docker-compose.yml down

###### commands for app:
migrate:
	docker exec -d app python manage.py migrate && sleep 5

run_celery:
	docker exec -d app celery -A drf_api_exchange_rate worker -l INFO && sleep 5

run_task:
	docker exec -d app python manage.py shell -c "from usd_rub.tasks import start_task; start_task()"

stop_celery:
	docker exec -d app pkill -f "celery -A drf_api_exchange_rate worker"

start_app: migrate run_celery run_task
