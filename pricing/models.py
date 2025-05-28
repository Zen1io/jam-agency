from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")
    price_per_m2 = models.DecimalField(max_digits=10, decimal_places=2, default=500.00, verbose_name="Цена за м²", help_text="Базовая цена в рублях за квадратный метр")
    code = models.SlugField(max_length=30, verbose_name="Код услуги", default='default-code', unique=False)
    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', verbose_name="Фото проекта")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('billboard', 'Биллборд'),
        ('stand', 'Штендер'),
        ('showcase', 'Оформление витрин'),
        ('car_wrap', 'Оклейка автомобилей'),
        ('facade_banner', 'Баннер на фасаде'),
        ('letters', 'Объёмные буквы'),
    ]

    MATERIAL_CHOICES = [
        # Billboard
        ('banner_fabric', 'Баннерная ткань'),
        ('mesh', 'Сетка'),
        ('lightbox_film', 'Лайтбокс-плёнка'),

        # Stand
        ('pvc', 'ПВХ'),
        ('plastic', 'Пластик'),
        ('composite', 'Композит'),

        # Showcase
        ('vinyl', 'Виниловая плёнка'),
        ('perforated_vinyl', 'Перфорированная плёнка'),
        ('uv_acrylic', 'УФ печать на акриле'),

        # Car wrap
        ('vinyl_gloss', 'Винил глянец'),
        ('vinyl_matte', 'Винил матовый'),
        ('vinyl_special', 'Винил спецэффект'),

        # Facade banner
        ('reinforced_banner', 'Прочный баннер'),
        ('blockout', 'Блок-аут'),

        # Letters
        ('acrylic', 'Акрил'),
        ('metal', 'Металл'),
        ('composite_led', 'Композит с подсветкой'),
    ]  # ← ВОТ ЭТА СКОБКА БЫЛА ПРОПУЩЕНА

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    width = models.FloatField()
    height = models.FloatField()
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    client_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.client_name} — {self.service_type}"

