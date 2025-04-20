from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import jsonpickle

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


#note: json is kinda weird, mby different solution?
@csrf_exempt
def SymptomByPlace(request):
	if request.method == 'POST':
		print(request.POST)
		body = json.loads(request.body)
		# Use request.POST for form data or request.body for JSON data
		place_name = body['place']
		place = Place.objects.filter(name = place_name).values_list('pk', flat=True).first()
		symptoms = Symptom.objects.filter(place = place)
		json_symptoms = []
		for i in list(symptoms):
			#json_symptoms.append(jsonpickle.encode(i))
			json_symptoms.append(i.name)
		for i in json_symptoms: print(i)
		return JsonResponse({
			'place': place_name,
			'symptoms': json_symptoms
		})