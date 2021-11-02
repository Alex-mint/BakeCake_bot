from BakeCake.models import Profile, Order


def get_adress(chat_id):
    profile = Profile.objects.get(external_id=chat_id)
    orders = Order.objects.filter(profile=profile).order_by('-created_at')[0]
    return orders.address