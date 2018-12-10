from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Customer
import json
from django.views.decorators.http import require_POST, require_GET
from django.core import serializers
from django.db.models import Q
from PIL import Image
import uuid


# Create your views here.
def health(require):
    return HttpResponse(json.dumps({'status': 'UP'}),
                        content_type='application/json')


# 保存客户，必须是POST请求
@require_POST
def save(require):
    # application/json 参数接收
    paras = json.loads(require.body.decode())
    customer = Customer()
    # 通过判断id的长度是否大于0，判断是新增还是修改
    if 'id' in paras and paras['id'] > 0:
        # 如果修改，那么首先需要从数据库中拿到原始对象
        id = paras['id']
        customer = Customer.objects.get(id=id)
    # 遍历所有参数与对象属性进行匹配，如果能匹配就进行赋值
    for p_key in paras:
        for c_key in customer.__dict__:
            if p_key == c_key:
                customer.__dict__[c_key] = paras[p_key]
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


# 通过id删除客户信息
@require_POST
def delete_by_id(require):
    result = {'flag': True, 'msg': '删除失败！'}
    paras = json.loads(require.body.decode())
    if 'id' in paras:
        id = paras['id']
        Customer.objects.filter(id=id).delete()
        result = {'flag': True, 'msg': '删除成功！'}
    else:
        result['msg'] = '没有设置id参数'
    return HttpResponse(json.dumps(result), content_type='application/json')


# 通过条件查询分页数据
@require_POST
def page_by_condition(require):
    params = json.loads(require.body.decode())
    page = params['page']
    condition = params['condition']
    customer_list = Customer.objects.all()
    if condition != None and len(condition) > 0:
        customer_list = customer_list.filter(Q(name__icontains=condition)
                                             | Q(id_card_no__icontains=condition)
                                             | Q(phone_no__icontains=condition)
                                             | Q(phone_no_2__icontains=condition)
                                             | Q(passport_no__icontains=condition)
                                             | Q(home_address__icontains=condition))
    pagesize = page['pagesize']
    currentpage = page['currentpage']
    beginindex = (currentpage - 1) * pagesize
    endindex = currentpage * pagesize
    total = customer_list.count()
    customer_list_json = serializers.serialize("json", customer_list[beginindex:endindex])
    page['total'] = total
    return HttpResponse(json.dumps({'data': customer_list_json, 'page': page}),
                        content_type="application/json")


# @require_POST
def upload_customer_image(request):
    if request.method == 'POST':
        photo = request.FILES['file']

        if photo:
            photoname = str(uuid.uuid1()) + '.' + str(photo).split('.')[-1]  # 使用uuid作为图片的存储名称
            photofullname = '/Users/wuketao/Public/study/github/customer_center_static/src/assets/' + photoname
            img = Image.open(photo)
            img.save(photofullname)
            if 'pk' in request.POST:
                pk = request.POST['pk']
                current_customer = Customer.objects.get(id=pk)  # type:Customer
                current_customer.photo_url = photoname
                current_customer.save()
                # 设置一个session，然后跳转到对应的页面，此处简易写写
                return HttpResponse('上传成功')
            else:
                return HttpResponse('上传失败')

        return HttpResponse('图片为空')
