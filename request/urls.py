from django.contrib import admin
from django.urls import path, include
from request.views import *

app_name = 'request'
urlpatterns = [
    path('create/', RequestCreateView.as_view()),
    path('all/', RequestListView.as_view()),
    # path('car/detail/<int:pk>/', CarDetailView.as_view())
]
