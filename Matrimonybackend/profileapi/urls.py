from django.urls import path
from .views import *

urlpatterns = [
    path('Profile_register/', Profile_register.as_view(), name='book-list'),
    path('Profile_register/<int:pk>/', Profile_registerView.as_view(), name='book-detail'),
]
