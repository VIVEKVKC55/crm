# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.calendar_view, name='calendar'),
    path('service/<str:selected_date>/', views.date_view, name='date_view'),
]
