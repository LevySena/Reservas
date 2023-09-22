from django.contrib import admin
from main.models import Quartos, Cliente, Ocupacao, Quarto_Cat, Ocupacao_tipo

# Register your models here.
admin.site.register(Quartos)
admin.site.register(Cliente)
admin.site.register(Ocupacao)
admin.site.register(Quarto_Cat)
admin.site.register(Ocupacao_tipo)
