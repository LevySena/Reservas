from django import forms
from main.models import *

class Cliente_Form(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = ['nome','telefone']
        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder' : 'Insira o nome'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : 'Insira o telefone/cell'}),
        }

class Cad_Form(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = ['data_ini','data_fim','fk_tipooccup','fk_quarto']
        widgets = {
            'data_ini' : forms.DateInput(attrs={'type' : 'date'}),
            'data_fim' : forms.DateInput(attrs={'type' : 'date'}),
        }

class UpcliForm(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = '__all__'
        widgets = {
            'data_ini' : forms.DateInput(attrs={'type' : 'date'}),
            'data_fim' : forms.DateInput(attrs={'type' : 'date'})
        }