DRF_API_Exchange_Rate 

Django API, который по переходу на страницу /get-current-usd/ 
отображает в json формате актуальный курс доллара к рублю 
и показывает 10 последних запросов. 

Данные по курсу обновляются в фоновом режиме каждые 10 секунд. Для обработки задачи
в фоновом режиме используется Celery. Задача запускается при старте работы приложения.

В данном проекте использовались следующие инструменты:

python v3.11
django v5.0.1
djangorestframework v3.14
celery v5.3.6
redis v5.0.1
requests v2.31

Настройка и запуск:

Перейдите в директорию, в которую будете клонировать репозиторий. 
Необходимо наличие установленного и запущенного Docker.
Для скачивания репозитория и разворачивания проекта локально в docker контейнере 
(создание БД, запуск приложения):
git clone https://github.com/Vladimir-Ivanov-92/DRF_API_Exchange_Rate.git

Необходимо создать в текущей директории .env файл 
и заполнить данными по образцу .env.example

Для автоматизации сборки проекта в репозитории лежит Makefile. Для запуска приложения
выполните: 
make up  - создаст два Docker контейнера app и redis
make start_app - выполнит миграции БД, запустит Celery и добавит фоновую задачу по 
отправке запросов и получению значений обменного курса.

