#Testing purposes only

from django.urls import path, include
from . import views
from .views import ShowSymptomByPlace, ShowCauseByPlace, ShowSymptomByCause, ShowCauseAndSymptom
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'injuries', views.AllInjuryViewSet)
router.register(r'symptoms', views.AllSymptomViewSet)
router.register(r'place', views.AllPlaceViewSet)
router.register(r'cause', views.AllCauseViewSet)
#router.register(r'sbp', views.ReactView)



urlpatterns = [
    path('', include(router.urls)),
    path('symptombyplace/', ShowSymptomByPlace),
    path('symptombycause/', ShowSymptomByCause),
    path('symptomandcause/', ShowCauseAndSymptom),
    path('causebyplace/', ShowCauseByPlace)

]
