from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('calculator/', views.calculator_view, name='calculator'),
]
