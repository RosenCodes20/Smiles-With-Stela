from django.urls import path

from mother_gift.soaps import views

urlpatterns = [
    path('', views.soaps, name='soaps')
]