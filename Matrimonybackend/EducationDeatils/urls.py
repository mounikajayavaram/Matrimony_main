from django.urls import path
from .views import *

urlpatterns = [
    path('EducationDetailList/', EducationDetailList.as_view()),
    path('EducationDetailList/<int:pk>/', EducationDetailview.as_view()),
]