from django import views
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from recipes.views import home

urlpatterns = [
    path('', home)
]
