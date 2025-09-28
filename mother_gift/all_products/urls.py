from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from django.conf import settings
from mother_gift.all_products import views

urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('product-details/<int:pk>/', views.product_details, name='product-details'),
    path('add-product/', views.create_products, name='add-product')
]