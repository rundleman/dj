from rest_framework import serializers
from cars.models import Car


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = ('vin', 'color', 'brand', 'car_type', 'user')
