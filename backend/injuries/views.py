from rest_framework import viewsets
from .models import Injury, Symptom, Place, Cause
from .serializers import InjurySerializer, SymptomSerializer, PlaceSerializer, CauseSerializer

class InjuryViewSet(viewsets.ModelViewSet):
	queryset = Injury.objects.all()
	serializer_class = InjurySerializer

class SymptomViewSet(viewsets.ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer

class PlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

class CauseViewSet(viewsets.ModelViewSet):
	queryset = Cause.objects.all()
	serializer_class = CauseSerializer