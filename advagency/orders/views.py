from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from pricing.utils import calculate_price

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.price = calculate_price(order.service_type)
            order.save()
            return redirect('order_history')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})