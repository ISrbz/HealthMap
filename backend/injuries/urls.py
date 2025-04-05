from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'injuries', views.InjuryViewSet)
router.register(r'symptoms', views.SymptomViewSet)
router.register(r'place', views.PlaceViewSet)
router.register(r'cause', views.CauseViewSet)


urlpatterns = [
    path('', include(router.urls))
]
