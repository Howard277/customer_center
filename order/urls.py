from django.urls import path
from . import views

urlpatterns = [
    path('save', views.save),
    path('page_by_condition', views.page_by_condition),
    path('get_order_by_customerid', views.get_order_by_customerid)
]
