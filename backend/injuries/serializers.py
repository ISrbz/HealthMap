#For seeing all objects from a given model

from rest_framework import serializers
from .models import Injury, Symptom, Place, Cause

class InjurySerializer(serializers.ModelSerializer):
	class Meta:
		model = Injury
		fields = ['name']

class SymptomSerializer(serializers.ModelSerializer):
	name = serializers.StringRelatedField()
	place = serializers.StringRelatedField()
	cause = serializers.StringRelatedField()

	class Meta:
		model = Symptom
		fields = ['name', 'place', 'cause']
	def __str__(self):
		return f"{self.name}"

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ['name']

class CauseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cause
		fields = ['name']