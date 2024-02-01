from datetime import datetime

import requests
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response

from config import NUM_QUERY, CURRENCY_2

from .models import UsdRub
from .serializers import UsdRubSerializer


class UsdRubView(generics.ListAPIView):
    """
        Предоставляет данные о текущем курсе USD/RUB и 10 последних полученных значений
    курса в JSON:

    {
        "current_rate": 89.766607,
        "time": "2024-01-01 15:46:54",
        "last_10_rates": [
                {
                    "index": 1,
                    "time": "2024-01-01 15:25:30",
                    "value": 89.786533
                },
                ...
                {
                    "index": 10,
                    "time": "2024-01-01 15:23:54",
                    "value": 89.766234
                }
            ]
    }
    """
    queryset = UsdRub.objects.order_by('-pk')[:NUM_QUERY]
    serializer_class = UsdRubSerializer

    def get(self, request, *args, **kwargs) -> Response:
        result = {}
        # получение данных о курсе через API openexchangerates.org
        data = requests.get(settings.API_EXCHANGE_RATE).json()
        result['current_rate'] = data['rates'][CURRENCY_2]
        result['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # get data from serializer
        serializer = self.get_serializer(self.get_queryset(), many=True)
        serialized_data = [{"index": index + 1, **item} for index, item in
                           enumerate(serializer.data)]
        result['last_10_rates'] = serialized_data

        return Response(result)
