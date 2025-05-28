from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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

    orders = user.order_set.all() if hasattr(user, 'order_set') else []

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