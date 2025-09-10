from django.urls import path

from mother_gift.decorations import views

urlpatterns = [
    path('', views.decorations, name='decorations')
]