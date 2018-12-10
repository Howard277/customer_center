from django.urls import path
from .views import health, save, all, delete_by_id, page_by_condition, upload_customer_image

urlpatterns = [
    path('health', health),
    path('save', save),
    path('all', all),
    path('delete_by_id', delete_by_id),
    path('page_by_condition', page_by_condition),
    path('upload_customer_image', upload_customer_image)
]
