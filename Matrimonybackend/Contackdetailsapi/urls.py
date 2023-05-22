from django.urls import path
from .views import *

urlpatterns = [
    path('Contact_register/', Contact_register.as_view()),
    path('Contact_register/<int:pk>/', Contact_registerView.as_view()),
]