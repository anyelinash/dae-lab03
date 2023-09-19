from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=50)
    pub_date =models.DateTimeField('date publishied')

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=80)
    votos = models.IntegerField(default=0)