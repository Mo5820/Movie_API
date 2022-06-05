from rest_framework import serializers 
from . models import Geust,Moive,Reserivation

class MoiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Moive
        fields='__all__'

class ReserviationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reserivation
        fields='__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Geust
        # fields=['pk','reservation','name','mobile']
        fields=['id','name','mobile']