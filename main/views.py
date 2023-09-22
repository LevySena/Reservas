from django.shortcuts import render
from main.models import Quartos,Ocupacao


def Reservas(request):
    quarto=Quartos.objects.all
    ocupacao=Ocupacao.objects.all
    contexto={
        'room':quarto,
        'ocup':ocupacao,
    }
    return render(request, "Tela_Reservas/index.html",context=contexto)
