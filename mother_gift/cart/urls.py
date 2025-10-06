from django.urls import path

from mother_gift.cart import views

urlpatterns = [
    path('<int:pk>/', views.cart, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-product/<int:pk>/', views.remove_product_from_cart, name='remove-cart-product')
]