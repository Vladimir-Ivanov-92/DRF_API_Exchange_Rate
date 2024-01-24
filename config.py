from os import environ

DEBUG = environ.get("DEBUG")

SECRET_KEY = environ.get("SECRET_KEY")

APP_ID = environ.get("APP_ID")

REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")
