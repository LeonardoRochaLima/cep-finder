from django.urls import path
from api.views import CepList, CepDetails, CreateCEPView, EstadosList, EstadoDetails

urlpatterns = [
    path('cep/', CepList.as_view()),
    path('cep/<str:cep>', CepDetails.as_view()),
    path('cep/create/<str:cep>', CreateCEPView.as_view(), name='create'),

    path('estado/', EstadosList.as_view()),
    path('estado/<str:uf>', EstadoDetails.as_view()),
]
