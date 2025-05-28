from django import forms
from .models import Order

# соответствие code услуги → допустимые материалы
MATERIAL_MAP = {
    'billboard': ['banner_fabric', 'mesh', 'lightbox_film'],
    'stand': ['pvc', 'plastic', 'composite'],
    'showcase': ['vinyl', 'perforated_vinyl', 'uv_acrylic'],
    'car_wrap': ['vinyl_gloss', 'vinyl_matte', 'vinyl_special'],
    'facade_banner': ['reinforced_banner', 'mesh', 'blockout'],
    'letters': ['acrylic', 'plastic', 'metal', 'composite_led'],
}

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['service']  # service задается во view

    def __init__(self, *args, service=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = service
        self.user = user

        # ограничение по материалам
        if self.service and self.service.code in MATERIAL_MAP:
            allowed_materials = MATERIAL_MAP[self.service.code]
            self.fields['material'].choices = [
                (key, label) for key, label in self.fields['material'].choices if key in allowed_materials
            ]

        # автозаполнение имени и телефона
        if self.user:
            self.fields['client_name'].initial = f"{self.user.first_name} {self.user.last_name}".strip() or "Без имени"
            profile = getattr(self.user, 'userprofile', None)
            if profile:
                self.fields['phone'].initial = profile.phone_number
