from django.db import models

# Create your models here.

class intercorrencia(models.Model):
    Data: models.Data()
    horario: models.hora()
    descricao: models.TextField(blank=True)
