from django.urls import path
from .views import AddCustomerView

urlpatterns = [
    path('add-customer/', AddCustomerView.as_view(), name='add_customer'),
]
