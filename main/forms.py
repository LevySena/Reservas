from django import forms
from main.models import *

class Cliente_Form(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = ['nome','telefone']
        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder' : 'Nome do Cliente'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : 'Telefone/Cel.'}),
        }
class Cad_Form(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = ['data_ini','data_fim','fk_tipooccup','fk_quarto']
        widgets = {
            'data_ini' : forms.DateInput(attrs={'type' : 'date'}),
            'data_fim' : forms.DateInput(attrs={'type' : 'date'}),
    
        }