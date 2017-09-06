from datetime import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Lista(models.Model):
	titulo_lista = models.CharField(max_length=50)
	fecha_creacion_lista = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.titulo_lista


class Tarea(models.Model):
	lista = models.ForeignKey(Lista, null=True, on_delete=models.CASCADE)
	titulo_tarea = models.CharField(max_length=50)
	terminado =models.BooleanField(default=False)
	fecha_creacion_tarea = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	descripcion = models.TextField(blank=True)

	def __str__(self):
		return self.titulo_tarea

	