from django.urls import path, include
from . import views, views_relationship

urlpatterns = [
    path('health', views.health),
    # 配置“客户”模块接口地址
    path('save', views.save),
    path('all', views.all),
    path('delete_by_id', views.delete_by_id),
    path('page_by_condition', views.page_by_condition),
    path('upload_customer_image', views.upload_customer_image),
    # 配置“联系人”模块接口地址
    path('relationship/', include(
        [path('all', views_relationship.all)
            , path('get_by_customerid', views_relationship.get_by_customerid)
            , path('save', views_relationship.save)]))
]
