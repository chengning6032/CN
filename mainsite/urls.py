# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('<str:slug>', views.showpost, name="ShowPost")
]
