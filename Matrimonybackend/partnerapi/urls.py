from django.urls import path
from .views import *

urlpatterns = [
    path('partnerprefarencelist/', partnerprefarencelist.as_view(), name='partnerprefarencelist'),
    path('partnerprefarencelist/<int:pk>/', partnerprefarenceView.as_view(), name='partnerprefarenceView'),
]
