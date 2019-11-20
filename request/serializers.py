from rest_framework import serializers
from request.models import Request


# class RequestsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Request
#         fields = ('id', 'vin', 'user')

class RequestsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'creation_date', 'message', 'user', 'request_status')


class RequestDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'phone',
                  'creation_date', 'address', 'message', 'user', 'request_status')
