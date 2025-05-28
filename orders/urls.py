from django.urls import path
from .views import create_order

urlpatterns = [
    path('create/<int:service_id>/', create_order, name='create_order'),
]