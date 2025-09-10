from django.urls import path

from mother_gift.cart import views

urlpatterns = [
    path('', views.cart, name='cart')
]