from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Customer
import json
from django.views.decorators.http import require_POST,require_GET
from django.core import serializers


# Create your views here.
def test(require):
    return HttpResponse('ok')


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
