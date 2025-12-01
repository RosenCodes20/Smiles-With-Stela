from django.urls import path

from mother_gift.accounts import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login-by-me'),
    path('register/', views.Register.as_view(), name='register-by-me'),
    path('logout/', views.Logout.as_view(), name='logout-by-me'),

    path('profile/<int:pk>/', views.ProfileDetails.as_view(), name='profile-details'),

    path('edit-profile/<int:pk>/', views.EditProfile.as_view(), name='edit-profile')
]