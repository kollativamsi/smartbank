from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('kyc-upload/', views.kyc_upload, name='kyc_upload'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('kyc-status/', views.kyc_status, name='kyc_status'),
]
