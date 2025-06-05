from django.db.models import Sum
from orders.models import Order
from .models import UserProfile

def update_user_discount(user):
    total_sum = Order.objects.filter(client=user).aggregate(total=Sum('estimated_price'))['total'] or 0

    if total_sum >= 50000:
        discount = 15
    elif total_sum >= 30000:
        discount = 10
    elif total_sum >= 15000:
        discount = 5
    else:
        discount = 0

    profile, _ = UserProfile.objects.get_or_create(user=user)
    profile.discount = discount
    profile.save()
