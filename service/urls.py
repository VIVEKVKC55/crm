# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.date_view, name='date_view'),
]
