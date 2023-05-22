from rest_framework import serializers
from .models import Plan, SilverPlan, GoldPlan, PremiumPlan, DedicatedRMPlan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SilverPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    class Meta:
        model = SilverPlan
        fields = '__all__'

class GoldPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    class Meta:
        model = GoldPlan
        fields = '__all__'

class PremiumPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    class Meta:
        model = PremiumPlan
        fields = '__all__'

class DedicatedRMPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    class Meta:
        model = DedicatedRMPlan
        fields = '__all__'
