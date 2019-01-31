from .models import OrderItem, Order

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


class OrderModelTests(TestCase):
    def setUp(self):
        for i in range(0, 10):
            Order.objects.create(order_id=str(i), customer_id="1", shipping=0,
                                 created_at=timezone.now())
        for i in range(10, 15):
            Order.objects.create(order_id=str(i), customer_id="2", shipping=80,
                                 created_at=timezone.now())
        for i in range(0, 7):
            OrderItem.objects.create(order_id=str(i), product_name="product_1", qty=1)
        for i in range(7, 12):
            OrderItem.objects.create(order_id=str(i), product_name="product_2", qty=2)
        for i in range(12, 15):
            OrderItem.objects.create(order_id=str(i), product_name="product_3", qty=3)

    def test_shipping_view(self):
        response = self.client.get(reverse('shipping'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_free'], 10)
        self.assertEqual(response.context['total_not_free'], 5)

    def test_top_view(self):
        response = self.client.get(reverse('top'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['goods'][0], ('product_2', 10))
        self.assertEqual(response.context['goods'][1], ('product_3', 9))
        self.assertEqual(response.context['goods'][2], ('product_1', 7))