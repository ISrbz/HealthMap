from rest_framework import serializers
from .models import Injury, Symptom, Place, Cause

class InjurySerializer(serializers.ModelSerializer):
	class Meta:
		model = Injury
		fields = ['name']

class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = ['name', 'place', 'cause']

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ['name']

class CauseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cause
		fields = ['name']

	