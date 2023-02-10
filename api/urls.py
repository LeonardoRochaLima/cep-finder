from django.urls import path
from api.views import CepList, CepDetails

urlpatterns = [
    path('cep/', CepList.as_view()),
    path('cep/<str:cep>', CepDetails.as_view()),
]
