from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from profileapi.models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView

class SearchAPIView(APIView):
    def get(self, request):
        # Get search parameters from request
        search_params = request.GET
        # Build query based on search parameters
        query = Q()
        for key, value in search_params.items():
            if key == 'age':
                age_range = value.split('-')
                query &= Q(age__range=(age_range[0], age_range[1]))
            elif key == 'gender':
                query &= Q(gender=value)
            elif key == 'religion':
                query &= Q(religion=value)
            elif key == 'bride_or_groom':
                query &= Q(bride_or_groom=value)
            # Add more filters here

        # Execute query and return results
        results = Profile.objects.filter(query)
        return Response(results)
