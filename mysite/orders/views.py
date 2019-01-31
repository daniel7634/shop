from django.shortcuts import render
from django.http import HttpResponse

from .models import Order, OrderItem

def get_shipping_ratio(request):
    total_free = Order.objects.filter(shipping=0).count()
    total_not_free = Order.objects.all().count() - total_free
    print(total_not_free)
    context = {'total_free': total_free, 'total_not_free': total_not_free}
    return render(request, 'orders/shipping.html', context)

def get_top_good(request):
    query_set = OrderItem.objects.all()
    goods = {}
    for item in query_set:
        if item.product_name not in goods:
            goods[item.product_name] = item.qty
        else:
            goods[item.product_name] += item.qty
    goods = sorted(goods.items(), key=lambda t: t[1], reverse=True)
    context = {'goods': goods[:3]}
    return render(request, 'orders/top.html', context)

def get_cohort(request):
    query_set = Order.objects.all()
    daily_users = {}
    for order in query_set:
        day = order.created_at.strftime('%Y%m%d')
        if day not in daily_users:
            daily_users[day] = set()
        daily_users[day].add(order.customer_id)

    return render(request, 'orders/cohort.html')

