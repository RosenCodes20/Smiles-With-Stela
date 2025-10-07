from django.urls import path

from mother_gift.cart import views

urlpatterns = [
    path('<int:pk>/', views.cart, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-product/<int:pk>/', views.remove_product_from_cart, name='remove-cart-product'),
    path('finish_cart/', views.create_deliver_cart, name='finish-cart'),
    path('thanks-for-choosing-this-page/', views.thanks_for_choosing, name='thanks-for-choosing')
]