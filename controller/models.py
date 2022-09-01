from turtle import Turtle
from django.db import models

# Create your models here.


class Cuidador(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.IntegerField()
    telefone = models.IntegerField()

    

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.IntegerField()
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)



  