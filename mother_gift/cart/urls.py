from django.urls import path

from mother_gift.cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart')
]