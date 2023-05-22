from django.shortcuts import render

# Create your views here.
from .models import *
import ast
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .renderes import UserRenderer
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import routers, serializers, viewsets

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)     


class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)     

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)    


class verifyEmail(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      s=User.objects.filter(email=email)
      if s:
        return HttpResponse("already exist",content_type='application/json')
      else:
        return HttpResponse("not exist",content_type='application/json')     

class verifyPhone(APIView):
    def post(self,request,format=None):
      phoneNumber=request.data.get("phoneNumber")
      print(phoneNumber)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(phoneNumber=phoneNumber)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['phone Number not exist']}}, status=status.HTTP_404_NOT_FOUND)        

class verifyEmailLogin(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      print(email)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(email=email)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['Email not exist']}}, status=status.HTTP_404_NOT_FOUND)       


import requests
from django.views.generic.edit import CreateView
class verify_aadhaar(CreateView):
  def post(request):
      aadhaar_number = request.POST.get('aadhaar_number')

      # Make API call to UIDAI Aadhaar verification API
      response = requests.post(
          'https://<UIDAI API endpoint>',
          data={'aadhaar_number': aadhaar_number},
          headers={'Authorization': '<UIDAI API access token>'}
      )

      if response.status_code == 200:
          # Aadhaar card is verified
          return JsonResponse({'status': 'success'})
      else:
          # Aadhaar card verification failed
          return JsonResponse({'status': 'error'})        