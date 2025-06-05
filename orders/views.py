from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order, Service
from accounts.models import UserProfile
from accounts.utils import update_user_discount


# 💰 базовые цены за 1 м²
BASE_PRICES = {
    'banner_fabric': 500,
    'mesh': 450,
    'lightbox_film': 700,
    'pvc': 300,
    'plastic': 350,
    'composite': 600,
    'vinyl': 400,
    'perforated_vinyl': 450,
    'uv_acrylic': 800,
    'vinyl_gloss': 700,
    'vinyl_matte': 750,
    'vinyl_special': 900,
    'reinforced_banner': 600,
    'blockout': 650,
    'acrylic': 900,
    'metal': 1100,
    'composite_led': 1200,
}

@login_required
def create_order(request, service_id):
    user = request.user
    service = get_object_or_404(Service, id=service_id)
    profile = UserProfile.objects.filter(user=user).first()

    if request.method == 'POST':
        form = OrderForm(request.POST, service=service, user=user)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.client = user
            order.client_name = f"{user.first_name} {user.last_name}".strip() or "Без имени"
            order.phone = profile.phone_number if profile and profile.phone_number else "Без телефона"

            # 📏 расчёт стоимости без скидки
            base_price = BASE_PRICES.get(order.material, 500)
            area = order.width * order.height
            price = area * base_price

            # 🔁 обновляем скидку пользователя перед применением
            update_user_discount(user)

            # ⚠️ тянем обновлённую скидку заново
            profile.refresh_from_db()
            discount = profile.discount if profile else 0

            # 💰 итоговая стоимость
            order.estimated_price = round(price * (1 - discount / 100), 2)

            order.save()
            return redirect('profile')
    else:
        form = OrderForm(service=service, user=user)

    return render(request, 'orders/create_order.html', {'form': form, 'service': service})
