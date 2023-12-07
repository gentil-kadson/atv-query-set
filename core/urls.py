from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.respostas_exercicio, name='respostas_exercicio')
]