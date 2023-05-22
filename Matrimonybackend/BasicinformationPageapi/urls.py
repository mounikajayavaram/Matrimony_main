from django.urls import path
from .views import *

urlpatterns = [
    path('BasicInformationList/', BasicInformationList.as_view()),
    path('BasicInformationList/<int:pk>/', BasicInformationDetail.as_view()),
]