from rest_framework import serializers
from .models import *

class HoroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horoscope
        fields = '__all__'