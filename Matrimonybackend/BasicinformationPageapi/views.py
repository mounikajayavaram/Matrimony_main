from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BasicInformationList(APIView):
    def get(self, request, format=None):
        Basic = BasicInformation.objects.all()
        serializer = BasicinformationSerializer(Basic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BasicinformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasicInformationDetail(APIView):
    def get_object(self, pk):
        try:
            return BasicInformation.objects.get(pk=pk)
        except BasicInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        serializer = BasicinformationSerializer(BasicInformation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        serializer = BasicinformationSerializer(BasicInformation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        BasicInformation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)