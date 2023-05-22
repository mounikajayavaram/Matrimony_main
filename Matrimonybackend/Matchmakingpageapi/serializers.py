from rest_framework import serializers
from .models import *

class MatchmakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchmaking
        fields = '__all__'
