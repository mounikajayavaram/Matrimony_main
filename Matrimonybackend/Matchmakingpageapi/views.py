# views.py

from rest_framework import generics
from profileapi.models import  Profile
from .models import *
from profileapi.serializers import  ProfileSerializer
from .serializers import *

class MatchMakingList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Matchmaking.objects.all()
        name = self.request.query_params.get('name', None)
        gender = self.request.query_params.get('gender', None)
        religion = self.request.query_params.get('religion', None)
        caste = self.request.query_params.get('caste', None)
        height_min = self.request.query_params.get('height_min', None)
        height_max = self.request.query_params.get('height_max', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        if gender is not None:
            queryset = queryset.filter(gender=gender)
        if religion is not None:
            queryset = queryset.filter(religion=religion)
        if caste is not None:
            queryset = queryset.filter(caste=caste)
        if height_min is not None and height_max is not None:
            queryset = queryset.filter(height__range=(height_min, height_max))
        return queryset
