from django.db import models

class Presentacion(models.Model):
  titulo = models.CharField(max_length=150)
  texto = models.TextField()
