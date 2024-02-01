from typing import NamedTuple

import requests

from config import CURRENCY_2

from .schemas import APIExchangeRate


class CurrentRate(NamedTuple):
    current_rate: float
    time: str


def get_data_from_api_exchange(url: str) -> CurrentRate:
    """ Получает данные о курсе валюты и времени """
    data: APIExchangeRate = APIExchangeRate.parse_obj(
        requests.get(url).json())
    return CurrentRate(current_rate=data.rates[CURRENCY_2],
                       time=data.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
