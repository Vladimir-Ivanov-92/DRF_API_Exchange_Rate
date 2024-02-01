import logging
import time

import requests
from celery import shared_task
from django.conf import settings

from .models import UsdRub

logger = logging.getLogger(__name__)


@shared_task
def get_current_usd_task() -> None:
    """
    Sends a request every 10 seconds to get the exchange rate value USD/RUB
    """
    while True:
        try:
            data = requests.get(settings.API_EXCHANGE_RATE).json()
            UsdRub.objects.create(value=data['rates']['RUB'])
            time.sleep(10)
        except Exception as e:
            logger.error(f"При отправке запроса возникла ошибка: {e}")


def start_task() -> None:
    """
        Start get_current_usd_task in Celery
    """
    get_current_usd_task.delay()
