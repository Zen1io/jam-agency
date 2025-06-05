from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'client_name', 'phone', 'material', 'width', 'height', 'comment','estimated_price', 'created_at')
    list_filter = ('service', 'material', 'created_at')
    search_fields = ('client_name', 'phone', 'comment')
    ordering = ('-created_at',)
