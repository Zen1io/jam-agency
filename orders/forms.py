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
        exclude = ['service', 'client', 'estimated_price']

    def __init__(self, *args, service=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = service
        self.user = user

        self.fields['client_name'].disabled = True
        self.fields['phone'].disabled = True

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # Ограничение по материалам
        if self.service and self.service.code in MATERIAL_MAP:
            allowed_materials = MATERIAL_MAP[self.service.code]
            self.fields['material'].choices = [
                (key, label) for key, label in self.fields['material'].choices if key in allowed_materials
            ]

        # 🔄 Автозаполнение client_name и phone из user
        if self.user and hasattr(self.user, 'first_name'):
            self.fields['client_name'].initial = self.user.first_name
        if self.user and hasattr(self.user, 'userprofile'):
            profile = self.user.userprofile
            self.fields['phone'].initial = getattr(profile, 'phone_number', '')# если есть userprofile.phone

        if self.user and hasattr(self.user, 'userprofile'):
            discount = self.user.userprofile.discount
            self.fields['discount_info'] = forms.CharField(
                initial=f"{discount}%",
                disabled=True,
                required=False,
                label="Ваша скидка",
                widget=forms.TextInput(attrs={'class': 'form-control'})
            )