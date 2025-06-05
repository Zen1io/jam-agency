from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile
from .forms import ProfileForm
from orders.models import Order  # ✅ Импорт модели заказов

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            profile.phone_number = form.cleaned_data['phone_number']
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user, initial={'phone_number': profile.phone_number})

    # ✅ Получаем заказы, связанные с текущим пользователем
    orders = Order.objects.filter(client=user).order_by('-created_at')

    return render(request, 'accounts/profile.html', {'form': form, 'orders': orders})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Убедись, что 'login' есть в urls
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
