from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Customer
import json
from django.views.decorators.http import require_POST, require_GET
from django.core import serializers


# Create your views here.
def health(require):
    return HttpResponse(json.dumps({'status': 'UP'}),
                        content_type='application/json')


# 保存客户，必须是POST请求
@require_POST
def save(require):
    customer = Customer()
    # application/json 参数接收
    paras = json.loads(require.body.decode())
    if 'name' in paras:
        customer.name = paras['name']
    if 'sex' in paras:
        customer.sex = paras['sex']
    customer.save()
    return HttpResponse(customer.id)


# 获取所有客户信息
@require_GET
def all(require):
    return HttpResponse(serializers.serialize("json", Customer.objects.all()),
                        content_type="application/json")


# 通过查询条件搜索客户信息
@require_GET
def search_by_condition(require):
    customers = Customer.objects.all()
    params = require.GET
    if 'name' in params:
        customers = customers.filter(name=params['name'])
    if 'id_card_no' in params:
        customers = customers.filter(id_card_no=params['id_card_no'])
    return HttpResponse(serializers.serialize("json", customers), content_type="application/json")
