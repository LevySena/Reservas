from django.urls import path
from main.views import *


urlpatterns = [
    path("", Reservas, name="reservas"),
    path("cliente",Cadastro,name="cadastro"),
    path("clientef",CadFinal,name="cadfinal"),
]
