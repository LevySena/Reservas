from django.urls import path
from main.views import *


urlpatterns = [
    path("", Reservas, name="reservas"),
    path("cliente",Cadastro,name="cadastro"),
    path("clientef",CadFinal,name="cadfinal"),
    path("update/<id>/",Atualizar,name='update'),
    path("lista/",Listar_Cli,name='list'),
    path("detroyer",Limpar_Table,name="apagar"),
    path("murderer/<id>/",Limpar_ind,name='delCli')
]
