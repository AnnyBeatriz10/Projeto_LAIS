from django.db import models

# Create your models here.

class Intercorrencia(models.Model):
    data = models.DateField()
    horario = models.DateTimeField(auto_now=True)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'intercorrencia'

#class Cuidador(models.Model):
 #   rg: models.IntegerField()
  #  nome = models.CharField(max_length=100)
   # telefone: models.IntegerField()

#class Paciente(models.Model):
 #   nome = models.CharField(max_length=100)
  #  rg = models.IntegerField()
   # rua = models.CharField(max_length=100)
    #numero_rua = models.IntegerField()
    #cep: models.CharField(max_length=100)
    #cidade: models.CharField(max_length=100)
    #estado = models.CharField(max_length=100)
    #medico = models.CharField(max_length=100)

  