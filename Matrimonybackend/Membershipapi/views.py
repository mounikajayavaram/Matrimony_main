from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profileapi.models import Profile
from profileapi.serializers import ProfileSerializer 
from account.models import User
from .models import *
from .serializers import *
# Create your views here.
class PlanView(APIView):
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)



class SilverPlanView(APIView):
    def get(self, request):
        # check if user has a valid Silver plan
        user = request.user
        silver_plan = SilverPlan.objects.filter(user=user).first()

        if not silver_plan:
            return Response({'message': 'You do not have a valid Silver plan'}, status=status.HTTP_400_BAD_REQUEST)

        # get the profile details of another user
        # you can use any criteria to choose the other user, for example, you can choose a random user
        other_user = User.objects.exclude(id=user.id).first()
        profile = Profile.objects.filter(user=other_user).first()

        # return the profile details
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        # check if user already has a Silver plan
        if SilverPlan.objects.filter(user=user).exists():
            return Response({'message': 'You already have a Silver plan'}, status=status.HTTP_400_BAD_REQUEST)

        # create a new Silver plan for the user
        plan = Plan.objects.filter(name='Silver').first()
        silver_plan = SilverPlan(user=user, plan=plan)
        silver_plan.save()

        return Response({'message': 'Silver plan purchased successfully'}, status=status.HTTP_201_CREATED)

    def post(self, request):
        user = request.user
        silver_plan = SilverPlan.objects.filter(user=user).first()

        if not silver_plan:
            return Response({'message': 'You do not have a valid Silver plan'}, status=status.HTTP_400_BAD_REQUEST)

        # get the user ID from the request data
        user_id = request.data.get('user_id')

        if not user_id:
            return Response({'message': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        # get the profile details of the specified user
        user = User.objects.filter(id=user_id).first()

        if not user:
            return Response({'message': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.filter(user=user).first()

        if not profile:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        # return the profile details
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class GoldPlanView(APIView):
    def get(self, request):
        # check if user has a valid Gold plan
        user = request.user
        gold_plan = GoldPlan.objects.filter(user=user).first()

        if not gold_plan:
            return Response({'message': 'You do not have a valid Gold plan'}, status=status.HTTP_400_BAD_REQUEST)

        # get the profiles of other users
        profiles = Profile.objects.exclude(user=user).order_by('?')[:40]

        # return the profiles
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        # check if user already has a Gold plan
        if GoldPlan.objects.filter(user=user).exists():
            return Response({'message': 'You already have a Gold plan'}, status=status.HTTP_400_BAD_REQUEST)

        # create a new Gold plan for the user
        plan = Plan.objects.filter(name='Gold').first()
        gold_plan = GoldPlan(user=user, plan=plan, validity_months=3)
        gold_plan.save()

        return Response({'message': 'Gold plan purchased successfully'}, status=status.HTTP_201_CREATED)

class PremiumPlanView(APIView):
    def get(self, request):
        # check if user has a valid Premium plan
        user = request.user
        premium_plan = PremiumPlan.objects.filter(user=user).first()

        if not premium_plan:
            return Response({'message': 'You do not have a valid Premium plan'}, status=status.HTTP_400_BAD_REQUEST)

        # get the user's own profile
        profile = Profile.objects.filter(user=user).first()

        # return the user's own profile as a Premium profile
        serializer = PremiumPlanSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        # check if user already has a Premium plan
        if PremiumPlan.objects.filter(user=user).exists():
            return Response({'message': 'You already have a Premium plan'}, status=status.HTTP_400_BAD_REQUEST)

        # create a new Premium plan for the user
        plan = Plan.objects.filter(name='Premium').first()
        premium_plan = PremiumPlan(user=user, plan=plan, validity_months=3)
        premium_plan.save()

        return Response({'message': 'Premium plan purchased successfully'}, status=status.HTTP_201_CREATED)

class DedicatedRMPlanView(APIView):
    def get(self, request):
        # check if user has a valid Dedicated RM plan
        user = request.user
        dedicated_rm_plan = DedicatedRMPlan.objects.filter(user=user).first()

        if not dedicated_rm_plan:
            return Response({'message': 'You do not have a valid Dedicated RM plan'}, status=status.HTTP_400_BAD_REQUEST)

        # get the user's own profile
        profile = Profile.objects.filter(user=user).first()

        # return the user's own profile as a Dedicated RM profile
        serializer = DedicatedRMPlanSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        # check if user already has a Dedicated RM plan
        if DedicatedRMPlan.objects.filter(user=user).exists():
            return Response({'message': 'You already have a Dedicated RM plan'}, status=status.HTTP_400_BAD_REQUEST)

        # create a new Dedicated RM plan for the user
        plan = Plan.objects.filter(name='Dedicated RM').first()
        dedicated_rm_plan = DedicatedRMPlan(user=user, plan=plan)
        dedicated_rm_plan.save()

        return Response({'message': 'Dedicated RM plan purchased successfully'}, status=status.HTTP_201_CREATED)
