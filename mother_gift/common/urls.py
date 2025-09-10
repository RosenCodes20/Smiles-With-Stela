from django.urls import path

from mother_gift.common import views

urlpatterns = [
    path("", views.index, name="index")
]