from django.urls import path

from mother_gift.accounts import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('profile/<int:pk>/', views.profile_details, name='profile-details')
]