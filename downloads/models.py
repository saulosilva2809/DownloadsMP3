from django.db import models

# Create your models here.

class Musica(models.Model):
    url = models.URLField()
    nome_arquivo = models.CharField(max_length=100)
