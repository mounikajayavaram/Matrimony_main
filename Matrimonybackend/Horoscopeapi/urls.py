from django.urls import path
from .views import *

urlpatterns = [
    path('HoroscopeList/', HoroscopeList.as_view()),
    path('HoroscopeList/<int:pk>/', Horoscopeview.as_view()),
]