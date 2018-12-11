from django.db import models

# Create your models here.
SEX = (('man', '男'), ('woman', '女'))


# 客户模型
class Customer(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=5, choices=SEX, default='man')  # True为男，False为女
    id_card_no = models.CharField(max_length=20, null=True, db_index=True)  # 身份证号码
    phone_no = models.CharField(max_length=20, null=True, db_index=True)
    phone_no_2 = models.CharField(max_length=20, null=True, db_index=True)
    passport_no = models.CharField(max_length=20, null=True, db_index=True)  # 护照号码
    home_address = models.CharField(max_length=200, null=True)  # 家庭详细地址
    photo_url = models.CharField(max_length=200, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)


# 客户工作信息
class WordInfo(models.Model):
    customer_id = models.IntegerField(null=True, db_index=True)
    company_name = models.CharField(max_length=200, db_index=True)  # 单位名称
    company_org_no = models.CharField(max_length=200, null=True, db_index=True)  # 单位组织结构编码
    company_phone_no = models.CharField(max_length=20, null=True, db_index=True)  # 单位电话
    company_address = models.CharField(max_length=200, null=True)  # 单位详细地址
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)


# 客户关系人
class Relationship(models.Model):
    customer_id = models.IntegerField(null=False, db_index=True)
    name = models.CharField(max_length=20, db_index=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=5, default='man')  # man为男，woman为女
    relation_type = models.CharField(max_length=20)  # 关系类型
    id_card_no = models.CharField(max_length=20, null=True, db_index=True)  # 身份证号码
    phone_no = models.CharField(max_length=20, null=True, db_index=True)
    phone_no_2 = models.CharField(max_length=20, null=True, db_index=True)
    passport_no = models.CharField(max_length=20, null=True, db_index=True)  # 护照号码
    home_address = models.CharField(max_length=200, null=True)  # 家庭详细地址
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)


# 车产
class PropertyCar(models.Model):
    customer_id = models.IntegerField(null=True, db_index=True)
    brand = models.CharField(max_length=50)  # 品牌名称
    brand_chinese_name = models.CharField(max_length=50)  # 品牌中文名称
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)


# 房产
class PropertyHouse(models.Model):
    customer_id = models.IntegerField(null=True, db_index=True)
    house_no = models.CharField(max_length=50)  # 房产证号码
    house_address = models.CharField(max_length=200)  # 房产地址
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)
