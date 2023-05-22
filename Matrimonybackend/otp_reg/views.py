from django.shortcuts import render
import os
import random
import math
# *********************** FOR OTP SEND TO MOBILE NUMBER **********************************
#******************* START  *****************************

# ***************** END SEND OTP ***************************

# * Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

# * Twilio Imports
# from twilio.rest import Client


# * models Import
from .models import OTPVerifiaction,PhoneUser
# from .models import CustomUser

#* Errors
# from django.db import IntegrityError


# * Generating OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# *Checks OTP with the otp recevied from the GET Request

def generatingOTP(number):
    OTP = generateOTP()

    return OTP


# * Checking the OTP
import requests

url = "https://www.fast2sms.com/dev/bulkV2"
@api_view(['GET', 'POST'])
def otpGeneration(request):
    number = request.data['number']
    print(number)
    generatedOTP = generatingOTP(number)
    print(generatedOTP)
    s=OTPVerifiaction.objects.filter(phone_number=number).delete()
    print("end")
    querystring = {"authorization":"Ohn3rzDyQepLYgH8dVl1G6XCUcjtfm5MsNTbBxPISko7v0FAwaVbcwGO0hmTsXJotrdRM3QCSu2Y46L8","variables_values":generatedOTP,"route":"otp","numbers":number}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("start")
    print(response.text)
    if generatedOTP:
        data = OTPVerifiaction(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"OTPSent": True})
    else:
        return Response({"OTPSent": False})


@api_view(['PUT'])
def checkOTP(request):
    number = request.data['number']
    otp = request.data['otp']
    print("checking time",number,otp)
    generatedOTP = OTPVerifiaction.objects.filter(
        phone_number=number).values_list('otp')
    print(generatedOTP)
    if generatedOTP[0][0] == otp:
        data = OTPVerifiaction.objects.get(phone_number=number)
        data.is_verfied = True
        data.save()
        return Response({"status": True})

    else:
        return Response({"status": False})
    



@api_view(['GET', 'POST'])
def verifyUserPhone(request):
    phoneNumber=request.data['number']
    s=PhoneUser.objects.filter(phone_number=phoneNumber)
    print(s)
    if s:
        return Response({"status": "exist useer"})
    else:
        return Response({"status":"not Exist"})
@api_view(['GET', 'POST'])
def sendMessage(request):
    sender=request.data['sender']
    title=request.data['title']
    message=request.data['message']
    phoneNumber=request.data['phoneNumber']
    textValue="Mtrimony-"+title+"-"+phoneNumber +" -"+message
    print(textValue)
    querystring = {"authorization":"Ohn3rzDyQepLYgH8dVl1G6XCUcjtfm5MsNTbBxPISko7v0FAwaVbcwGO0hmTsXJotrdRM3QCSu2Y46L8","variables_values":textValue,"route":"otp","numbers":sender}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return Response({"status": "success"})