from django.contrib import admin
from .models import Service, PortfolioItem
from .models import QuoteRequest

admin.site.register(QuoteRequest)
admin.site.register(Service)
admin.site.register(PortfolioItem)