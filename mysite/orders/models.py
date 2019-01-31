from django.db import models
'''
order : 
    order_id: 訂單編號
    customer_id: 用戶id
    shipping: 運費，0為免運
    created_at: 訂單建立時間
order_item
    order_id: 訂單編號
    product_name: 商品名稱
    qty: 購買數量

'''


class Order(models.Model):

    order_id = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=10)
    shipping = models.IntegerField(default=0)
    created_at = models.DateTimeField()


class OrderItem(models.Model):

    order_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)

