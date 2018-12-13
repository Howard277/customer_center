from django.db import models
from .common import ORDER_STATUS


# Create your models here.

# 订单
class Order(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # 订单编号，主键
    card_no = models.CharField(max_length=50, db_index=True)  # 客户身份证号
    customer_name = models.CharField(max_length=50, null=True, db_index=True)  # 客户姓名
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='init', db_index=True)  # 订单状态
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=50)
