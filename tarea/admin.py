from django.contrib import admin

from .models import Lista, Tarea


# Register your models here.


class TareaInline(admin.TabularInline):
	fields =['titulo_tarea', 'terminado', 'descripcion']
	model = Tarea
	extra =0

class ListaAdmin(admin.ModelAdmin):
	list_display = ['titulo_lista']
	search_fields = ['titulo_lista']
	inlines = [TareaInline]

class TareaAdmin(admin.ModelAdmin):
	list_display=['titulo_tarea', 'descripcion']


	

admin.site.register(Lista, ListaAdmin)
admin.site.register(Tarea, TareaAdmin)