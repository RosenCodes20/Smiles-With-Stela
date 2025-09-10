from django.urls import path

from mother_gift.all_products import views

urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('product-details/<int:pk>/', views.product_details, name='product-details')
]