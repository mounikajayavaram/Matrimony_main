from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('verifyEmail/',verifyEmail.as_view(),name='update-verifyEmail'),
    path('verifyPhone/',verifyPhone.as_view(),name='update-verifyPhone'),
    path('verifyEmailLogin/',verifyEmailLogin.as_view(),name='update-verifyEmailLogin'),
    path('verify-aadhaar/', verify_aadhaar.as_view(), name='verify-aadhaar'),
    
    



]  
