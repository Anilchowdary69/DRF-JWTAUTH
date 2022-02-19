from django.contrib import admin
from django.urls import path
from. import views
from .api import RegisterApi


urlpatterns =[
path('api/register', RegisterApi.as_view()),
]