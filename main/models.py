from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Ocupacao_tipo(models.Model):
    tipo_occup = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_occup


class Quarto_Cat(models.Model):
    tipo_Quarto = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_Quarto


class Quartos(models.Model):
    num_Quarto = models.IntegerField(default=0)
    fk_tipoQuarto = models.ForeignKey(Quarto_Cat, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Quarto nº" + str(self.num_Quarto)


class Ocupacao(models.Model):
    data_ini = models.DateTimeField()
    data_fim = models.DateTimeField()
    fk_tipooccup = models.ForeignKey(
        Ocupacao_tipo, null=True, on_delete=models.SET_NULL
    )
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fk_quarto = models.ForeignKey(Quartos, on_delete=models.CASCADE)

    def __str__(self):
        return "ocupacao"
