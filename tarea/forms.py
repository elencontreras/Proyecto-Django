from django import forms
from . import models

class ListaForm(forms.ModelForm):

	class Meta:
		model = models.Lista
		fields = ['titulo_lista']

		labels = { 

			'titulo_lista': 'Titulo de la lista'
			}

		widgets = {
			'titulo_lista': forms.TextInput(attrs={'class': 'form-control'})
			}


class TareaForm(forms.ModelForm):

	class Meta:
		model = models.Tarea
		fields = ['lista', 'titulo_tarea','descripcion']


		widgets = {
			'lista': forms.Select(attrs={'class': 'form-control'}),
			'titulo_tarea': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
		}


	