from datetime import datetime

import requests
from rest_framework import generics
from rest_framework.response import Response

from config import APP_ID

from .models import UsdRub
from .serializers import UsdRubSerializer


class UsdRubView(generics.ListAPIView):
    """
    Outputs a list of the last 10 exchange rate values starting from the most current one
    """
    queryset = UsdRub.objects.order_by('-pk')[:10]
    serializer_class = UsdRubSerializer

    def get(self, request, *args, **kwargs) -> Response:
        result = {}
        # get data from API
        data = requests.get(
            f'https://openexchangerates.org/api/latest.json?app_id={APP_ID}&base=USD&symbols=RUB').json()
        result['current_rate'] = data['rates']['RUB']
        result['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # get data from serializer
        serializer = self.get_serializer(self.get_queryset(), many=True)
        serialized_data = [{"index": index + 1, **item} for index, item in
                           enumerate(serializer.data)]
        result['last_10_rates'] = serialized_data

        return Response(result)
