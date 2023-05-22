"""
URL configuration for Matrimonybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/otp_reg/', include('otp_reg.urls')),
    path('api/BasicinformationPageapi/', include('BasicinformationPageapi.urls')),
    path('api/EducationDetails/', include('EducationDeatils.urls')),
    path('api/Familydeatilsapi/', include('Familydeatilsapi.urls')),
    path('api/FAQASAPI/', include('FAQASAPI.urls')),
    path('api/Horoscopeapi/', include('Horoscopeapi.urls')),
    path('api/pagesapi/', include('pagesapi.urls')),
    path('api/partnerapi/', include('partnerapi.urls')),
    path('api/profileapi/', include('profileapi.urls')),
    path('api/Searchapi/', include('Searchapi.urls')),
    path('api/searchviewapi/', include('searchviewapi.urls')),
    path('api/Successtoriesapi/', include('Successtoriesapi.urls')),
    path('api/communicationapi/', include('communicationapi.urls')),
    path('api/Matchmakingpageapi/', include('Matchmakingpageapi.urls')),
    path('api/Membershipapi/', include('Membershipapi.urls')),
    path('api/Contackdetailsapi/', include('Contackdetailsapi.urls')),

    path('api/paymentapi/', include('paymentapi.urls')),















]  
