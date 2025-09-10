from django.urls import path

from mother_gift.about_us import views

urlpatterns = [
    path("", views.about_us, name='about-us')
]