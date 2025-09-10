from django.urls import path

from mother_gift.contact import views

urlpatterns = [
    path('', views.contact, name='contact')
]