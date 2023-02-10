from django.urls import path
from api.views import CepList, CepDetails, CreateCEPView

urlpatterns = [
    path('cep/', CepList.as_view()),
    path('cep/<str:cep>', CepDetails.as_view()),
    path('cep/create/<str:cep>', CreateCEPView.as_view(), name='create'),
]
