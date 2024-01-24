from rest_framework import generics

from .serializers import UsdRubSerializer
from .models import UsdRub


class UsdRubView(generics.ListAPIView):
    """
    Outputs a list of the last 10 exchange rate values starting from the most current one
    """
    queryset = UsdRub.objects.order_by('-pk')[:10]
    serializer_class = UsdRubSerializer
