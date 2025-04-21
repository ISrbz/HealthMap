from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets
from .models import Injury, Symptom, Place, Cause
from .serializers import InjurySerializer, SymptomSerializer, PlaceSerializer, CauseSerializer

class AllInjuryViewSet(viewsets.ModelViewSet):
	queryset = Injury.objects.all()
	serializer_class = InjurySerializer

class AllSymptomViewSet(viewsets.ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer

class AllPlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

class AllCauseViewSet(viewsets.ModelViewSet):
	queryset = Cause.objects.all()
	serializer_class = CauseSerializer

##################################################

def SymptomByPlace(request, flag):
	body = json.loads(request.body)
	# Use request.POST for form data or request.body for JSON data
	place_name = body['place']
	place = Place.objects.filter(name = place_name).values_list('pk', flat=True).first()
	symptoms = Symptom.objects.filter(place = place)
	json_symptoms = []
	for i in list(symptoms):
		json_symptoms.append(i.name)
	for i in json_symptoms: print(i)
	if flag:
		return place_name, symptoms
	else:
		return place_name, json_symptoms

def CauseBySymptom(symptoms):
	causes = [str(symptoms[0].cause)]
	for symptom in symptoms:
		#cause = Cause.objects.filter(name = symptom.cause).values_list('name', flat=True).first()
		if str(symptom.cause) != causes[-1]:
			causes.append(str(symptom.cause))
	for i in causes: print(i)
	return causes


@csrf_exempt
def ShowSymptomByPlace(request):
	if request.method == 'POST':
		print(request.POST)
		place_name, json_symptoms = SymptomByPlace(request, 0)
		return JsonResponse({
			'place': place_name,
			'symptoms': json_symptoms
		})

@csrf_exempt
def ShowCauseByPlace(request):
	if request.method == 'POST':
		print(request.POST)
		place_name, symptoms = SymptomByPlace(request, 1)
		json_causes = CauseBySymptom(symptoms)
		return JsonResponse({
			'place': place_name,
			'causes': json_causes
		})