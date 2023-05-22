from rest_framework import serializers
from .models import SuccessStory

class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = '__all__'
