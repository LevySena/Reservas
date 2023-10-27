from django.shortcuts import render,redirect
from django.http import HttpRequest
from main.models import Quartos,Ocupacao
from datetime import datetime,timedelta
from django.utils import timezone
from main.forms import *
from main.models import *

def Reservas(request):
    today=datetime.now()
    period=[timezone.make_aware(today+timedelta(days=x)) for x in range(90)]
    quarto=Quartos.objects.all()
    ocupacao=Ocupacao.objects.all()
    contexto={
        'room':quarto,
        'ocup':ocupacao,
        'dias':period,
    }
    return render(request, "Tela_Reservas/index.html",context=contexto)

def Cadastro(request):
    formulario = Cliente_Form()
    contexto = {
        'form' : formulario
    }
    if request.method == 'POST':
        formulario = Cliente_Form(request.POST)
        if formulario.is_valid():
            novo = formulario.save()
            request.session["id"] = novo.id
            return redirect(CadFinal)
    return render(request,"CadastroCliente/cadastro.html",context=contexto)

def CadFinal(request):
    formulario = Cad_Form()
    contexto = {
        'form' : formulario
    }
    if request.method == 'POST':
        formulario = Cad_Form(request.POST)
        if formulario.is_valid():
            novo = Ocupacao()
            novo.data_ini = formulario.cleaned_data['data_ini']
            novo.data_fim = formulario.cleaned_data['data_fim']
            novo.fk_tipooccup = formulario.cleaned_data['fk_tipooccup']
            novo.fk_quarto = formulario.cleaned_data['fk_quarto']
            novo.fk_cliente = Cliente.objects.get(pk=request.session['id'])
            novo.save()
            return redirect(Reservas)
    return render(request,"CadastroCliente/CadReserv.html",context=contexto)

def Atualizar(request,id):
    verify=Ocupacao.objects.filter(fk_cliente=id)
    if not verify:
        request.session["id"]=id
        return redirect(CadFinal)
    instance = Ocupacao.objects.get(fk_cliente=id)
    formulario=UpcliForm(instance=instance)
    if request.method == 'POST':
        formulario = UpcliForm(request.POST, instance=instance)
        if formulario.is_valid():
            formulario.save()
            return redirect(Reservas)
    contexto = {
        'form' : formulario,
    }
    return render(request,"UpdCliente/clienteUpdate.html", context=contexto)


def Limpar_Table(request):
    Banco = Cliente.objects.all()
    for i in Banco:
        i.delete()
    return redirect(Reservas)

def Limpar_ind(request,id):
    individuo = Ocupacao.objects.get(pk=id)
    individuo.delete()
    return redirect(Reservas)
        
def Listar_Cli(request):
    individuo = Cliente.objects.all()
    contexto={
        'pessoas' : individuo,
    }
    return render(request,"UpdCliente/listCliente.html",context=contexto)