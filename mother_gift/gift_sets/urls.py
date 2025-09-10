from django.urls import path

from mother_gift.gift_sets import views

urlpatterns = [
    path('', views.gift_sets, name='gift-sets')
]