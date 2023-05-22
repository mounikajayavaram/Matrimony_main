from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('PlanView/', PlanView.as_view(), name='PlanView'),
    path('SilverPlanView/', SilverPlanView.as_view(), name='SilverPlanView'),
    path('GoldPlanView/', GoldPlanView.as_view(), name='GoldPlanView'),
    path('PremiumPlanView/', PremiumPlanView.as_view(), name='PremiumPlanView'),
    path('DedicatedRMPlanView/', DedicatedRMPlanView.as_view(), name='DedicatedRMPlanView'),
    

    
    
]