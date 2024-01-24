from rest_framework import serializers
from .models import UsdRub


class UsdRubSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UsdRub
        fields = ('pk', 'time', 'value')
