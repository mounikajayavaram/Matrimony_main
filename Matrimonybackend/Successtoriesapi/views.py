from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SuccessStory
from .serializers import SuccessStorySerializer

class SuccessStoryViewSet(viewsets.ModelViewSet):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer
