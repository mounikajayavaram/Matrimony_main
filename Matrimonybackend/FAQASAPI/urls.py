from django.urls import path
from .views import FAQList, FAQDetail

urlpatterns = [
    path('faq/', FAQList.as_view()),
    path('faq/<int:pk>/', FAQDetail.as_view()),
]