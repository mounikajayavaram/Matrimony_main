from django.urls import path
from .views import  *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('MatchMakingList/', MatchMakingList.as_view(), name='MatchMakingList'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)