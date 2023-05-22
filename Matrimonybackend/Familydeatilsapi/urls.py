from django.urls import path
from .views import *

urlpatterns = [
    path('FamilydetailsList/', FamilydetailsList.as_view()),
    path('FamilydetailsList/<int:pk>/', Familydetailsview.as_view()),
]