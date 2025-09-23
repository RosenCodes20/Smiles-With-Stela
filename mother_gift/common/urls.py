from django.urls import path

from mother_gift.common import views

urlpatterns = [
    path("", views.index, name="index"),
    path('subscribe-for-news', views.subscribe_for_news, name='subscribe-for-news')
]
