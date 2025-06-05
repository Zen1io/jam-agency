# urls.py
from django.urls import path
from .views import billboard_preview

urlpatterns = [
    path('billboard-preview/', billboard_preview, name='billboard_preview'),
]
