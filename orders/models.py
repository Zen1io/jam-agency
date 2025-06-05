from django.db import models
from pricing.models import Service
from django.contrib.auth.models import User


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента", default="")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="")
    comment = models.TextField(blank=True, verbose_name="Комментарий", default="")
    width = models.FloatField(verbose_name="Ширина (м)", default=1.0)
    height = models.FloatField(verbose_name="Высота (м)", default=1.0)
    estimated_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Примерная стоимость",
        default=0
    )

    MATERIAL_CHOICES = [
        ('banner_fabric', 'Баннерная ткань'),
        ('mesh', 'Сетка'),
        ('lightbox_film', 'Лайтбокс-плёнка'),
        ('pvc', 'ПВХ'),
        ('plastic', 'Пластик'),
        ('composite', 'Композит'),
        ('vinyl', 'Винил'),
        ('perforated_vinyl', 'Перфорированная плёнка'),
        ('uv_acrylic', 'УФ печать на акриле'),
        ('vinyl_gloss', 'Винил глянец'),
        ('vinyl_matte', 'Винил матовый'),
        ('vinyl_special', 'Винил спецэффект'),
        ('reinforced_banner', 'Прочный баннер'),
        ('blockout', 'Блок-аут'),
        ('acrylic', 'Акрил'),
        ('metal', 'Металл'),
        ('composite_led', 'Композит с подсветкой'),
    ]

    material = models.CharField(
        max_length=30,
        choices=MATERIAL_CHOICES,
        verbose_name="Материал",
        default='banner_fabric'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.title} - {self.client_name or 'Гость'} ({self.created_at.strftime('%d.%m.%Y')})"
