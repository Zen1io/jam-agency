from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    SERVICE_CHOICES = [
        ('design', 'Дизайн'),
        ('ads', 'Реклама'),
        ('seo', 'SEO продвижение'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.service_type} - {self.date_created.date()}"