from rest_framework import serializers
from .models import partnerprefarence

class partnerprefarenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = partnerprefarence
        fields = '__all__'
  
