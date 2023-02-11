from django.urls import path
from api.views import CepList, CepDetails, CreateCEPView, CepsLojaCorrList, CepsLojaCorrDetails, CreateCEPsLojaCorrView

urlpatterns = [
    path('cep/', CepList.as_view()),
    path('cep/<str:cep>', CepDetails.as_view()),
    path('cep/create/<str:cep>', CreateCEPView.as_view(), name='create'),

    path('cepslojacorr/', CepsLojaCorrList.as_view()),
    path('cepslojacorr/<str:ceplojacor>', CepsLojaCorrDetails.as_view()),
    path('cepslojacorr/create/<str:ceplojacor>', CreateCEPsLojaCorrView.as_view(), name='create'),
]
