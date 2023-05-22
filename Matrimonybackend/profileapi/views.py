from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import generics
from .models import *
from .serializers import *

class Profile_register(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class Profile_registerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
