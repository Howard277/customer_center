from .models import Relationship
from django.http import HttpResponse
from django.core import serializers
import json


# 获取所有联系人
def all(request):
    return HttpResponse(serializers.serialize("json", Relationship.objects.all()),
                        content_type='application/json')


# 保存联系人
def save(request):
    paras = json.loads(request.body.decode())
    relationship = Relationship()
    # 通过判断id的长度是否大于0，判断是新增还是修改
    if 'id' in paras and paras['id'] > 0:
        # 如果修改，那么首先需要从数据库中拿到原始对象
        id = paras['id']
        relationship = Relationship.objects.get(id=id)
    # 遍历所有参数与对象属性进行匹配，如果能匹配就进行赋值
    for p_key in paras:
        for c_key in relationship.__dict__:
            if p_key == c_key:
                relationship.__dict__[c_key] = paras[p_key]
    relationship.save()
    return HttpResponse(relationship.id)


# 通过客户id查询联系人
def get_by_customerid(request):
    customer_id = -1
    if 'customer_id' in request.GET:
        customer_id = request.GET['customer_id']
    return HttpResponse(serializers.serialize("json", Relationship.objects.all().filter(customer_id=customer_id)),
                        content_type='application/json')
