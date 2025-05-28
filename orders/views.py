from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order, Service
from accounts.models import UserProfile  # если используется расширенный профиль

@login_required
def create_order(request, service_id):
    user = request.user
    service = get_object_or_404(Service, id=service_id)
    profile = UserProfile.objects.filter(user=user).first()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.client = user
            order.client_name = f"{user.first_name} {user.last_name}".strip() or "Без имени"
            order.phone = profile.phone_number if profile and profile.phone_number else "Без телефона"
            order.save()
            return redirect('profile')  # или куда нужно
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form, 'service': service})