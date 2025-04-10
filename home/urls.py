from django.urls import path
from .views import HomeView, CustomLoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
     path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
