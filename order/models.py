from django.db import models
from .common import ORDER_STATUS


# Create your models here.

# 订单
class Order(models.Model):
    card_no = models.CharField(max_length=50)  # 客户身份证号
    customer_name = models.CharField(max_length=50, null=True)  # 客户姓名
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='init')  # 订单状态
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=50)
