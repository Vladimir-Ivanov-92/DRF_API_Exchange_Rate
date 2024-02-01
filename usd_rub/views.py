from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response

from config import NUM_QUERY

from .models import UsdRub
from .serializers import UsdRubSerializer
from .services import CurrentRate, get_data_from_api_exchange


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
        # получение данных о курсе через API openexchangerates.org
        current_rate_data: CurrentRate = get_data_from_api_exchange(
            settings.API_EXCHANGE_RATE)

        # получение данных из serializer
        serializer_data = (self.get_serializer(self.get_queryset(), many=True)).data

        # добавление индекса к каждому прошлому значению курса
        previous_values = [{"index": index + 1, **item} for index, item in
                           enumerate(serializer_data)]

        result = dict(
            current_rate=current_rate_data.current_rate,
            time=current_rate_data.time,
            last_rates=previous_values
        )

        return Response(result)
