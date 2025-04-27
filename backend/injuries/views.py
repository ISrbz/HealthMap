#Connections to the injury db

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Injury, Symptom, Place, Cause
from .serializers import InjurySerializer, SymptomSerializer, PlaceSerializer, CauseSerializer

##################################################

#For seeing all objects from a given model

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

#Functions for searching for specific objects from a given model by a given value

def SymptomByPlace(request, obj):
	body = json.loads(request.body)
	# Use request.POST for form data or request.body for JSON data
	id = body['id']
	print(id)
	place = Place.objects.filter(pk = id).values_list('pk', flat=True).first()
	symptoms = Symptom.objects.filter(place = place)
	json_symptoms = []
	for i in list(symptoms):
		json_symptoms.append(i.name)
	for i in json_symptoms: print(i)
	if obj: # if True return the symptoms as a list of objects
		return id, symptoms
	else: #if False return a list of strings
		return id, json_symptoms

def SymptomByCause(request):
	body = json.loads(request.body)
	# Use request.POST for form data or request.body for JSON data
	cause_name = body['cause']
	cause = Cause.objects.filter(name = cause_name).values_list('pk', flat=True).first()
	symptoms = Symptom.objects.filter(cause = cause)
	json_symptoms = []
	for i in list(symptoms):
		json_symptoms.append(i.name)
	for i in json_symptoms: print(i)
	return cause_name, json_symptoms

def CauseBySymptom(symptoms):
	causes = [str(symptoms[0].cause)]
	for symptom in symptoms:
		if str(symptom.cause) != causes[-1]:
			causes.append(str(symptom.cause))
	for i in causes: print(i)
	return causes

##################################################

#Functions for giving the search results to the frontend in json format 

def ShowCauseAndSymptom(request):
	if request.method == 'GET':
		print(request.GET)
		causes = []
		json_str = "{"
		symptoms = Symptom.objects.all().values_list("name", flat=True)
		for s in symptoms:
			cause = str(Symptom.objects.filter(name = s).values_list('cause', flat=True).first())
			causes.append(cause)
			if cause != causes[-1]:
				json_str += "},\n{\n\"cause\": \"" + cause +  "\",\n\"symptoms\": "
			json_str += "\"" + s + "\","
		return JsonResponse(json_str, safe=False)

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
	
@csrf_exempt
def ShowSymptomByCause(request):
	if request.method == 'POST':
		print(request.POST)
		cause_name, json_symptoms = SymptomByCause(request)
		return JsonResponse({
			'cause': cause_name,
			'symptoms': json_symptoms
		})
	
#####################################################

class ReactView(viewsets.ModelViewSet):
  
    serializer_class = SymptomSerializer

    def get(self, request):
        detail = [ {"place": str(detail.place),"detail": detail.name} 
        for detail in Symptom.objects.all()]
        return Response(detail)

    def post(self, request):

        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
		
