from django.shortcuts import render
from .models import Order
from django.http import HttpResponse
from django.core import serializers
import json
from common import utils
from django.views.decorators.http import require_POST
from django.db.models import Q


# Create your views here.

def save(request):
    params = json.loads(request.body.decode())
    order = Order()
    # 通过判断入参中是否包含订单号，判断是新增订单还是修改订单
    if 'id' in params and len(params[id]) > 0:
        # 包含id的属于修改订单
        order = Order.objects.get(id=id)
    else:
        # 不包含订单id的，属于新增订单
        order.id = 'order' + utils.get_time_str2()
    for okey in order.__dict__:
        for pkey in params:
            if okey == pkey:
                order.__dict__[okey] = params[pkey]
    order.save()
    return HttpResponse(order.id)


# 通过客户编号获取订单信息
def get_order_by_customerid(request):
    customer_id = request.GET['customerId']
    orders = Order.objects.all().filter(customer_id=customer_id)
    return HttpResponse(serializers.serialize(orders), content_type='application/json')


# 通过条件查询分页数据
@require_POST
def page_by_condition(request):
    params = json.loads(request.body.decode())
    page = params['page']
    condition = params['condition']
    order_list = Order.objects.all()
    if condition != None and len(condition) > 0:
        order_list = order_list.filter(Q(id__icontains=condition)
                                       | Q(card_no__icontains=condition)
                                       | Q(customer_name__icontains=condition)
                                       | Q(order_status__icontains=condition))
    pagesize = page['pagesize']
    current_page = page['currentpage']
    begin_index = (current_page - 1) * pagesize
    end_index = current_page * pagesize
    total = order_list.count()
    customer_list_json = serializers.serialize("json", order_list[begin_index:end_index])
    page['total'] = total
    return HttpResponse(json.dumps({'data': customer_list_json, 'page': page}),
                        content_type="application/json")
