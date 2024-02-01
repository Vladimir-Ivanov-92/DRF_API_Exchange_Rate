from os import environ

from dotenv import load_dotenv

load_dotenv()

# Django
DEBUG = environ.get("DEBUG")
SECRET_KEY = environ.get("SECRET_KEY")

# Количество отображаемых запросов
NUM_QUERY = int(environ.get("NUM_QUERY"))

# openexchangerates.org
APP_ID = environ.get("APP_ID")
CURRENCY_1 = environ.get("CURRENCY_1")
CURRENCY_2 = environ.get("CURRENCY_2")

# Redis
REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")
