from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from request.serializers import RequestDetailSerializer, RequestsListSerializer
from request.models import Request


class RequestCreateView(generics.CreateAPIView):
    serializer_class = RequestDetailSerializer


class RequestListView(generics.ListAPIView):
    serializer_class = RequestsListSerializer
    queryset = Request.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


# class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CarDetailSerializer
#     queryset = Car.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, )
