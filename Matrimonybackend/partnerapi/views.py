from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import generics
from .models import *
from .serializers import *

class partnerprefarencelist(generics.ListCreateAPIView):
    queryset = partnerprefarence.objects.all()
    serializer_class = partnerprefarenceSerializer

class partnerprefarenceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = partnerprefarence.objects.all()
    serializer_class = partnerprefarenceSerializer