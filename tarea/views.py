import datetime
from datetime import datetime, timedelta
from datetime import date
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages


from .models import Lista, Tarea
from .forms import ListaForm, TareaForm


class BaseView(object):
	
	def get_active_title(self):
		if self.active_title:
			return self.active_title

	def get_context_data(self):
		context = super(BaseView, self).get_context_data()
		context['active_title'] = self.get_active_title()
		return context


class IndexView(BaseView, generic.ListView):
	active_title = 'lista'
	model = Lista
	template_name = 'tarea/index.html'


class ListaCreateView(generic.CreateView):
	active_title = 'lista'
	model = Lista
	form_class = ListaForm
	template_name = 'tarea/lista_form.html'
	success_url =reverse_lazy('tarea:clase_index')


class ListaUpdateView(generic.UpdateView):
	active_title = 'lista'
	model = Lista
	form_class = ListaForm
	template_name = 'tarea/lista_form.html'
	success_url =reverse_lazy('tarea:clase_index') 



class DetailList(generic.DetailView):
	active_title = 'lista'
	model = Lista
	template_name = 'tarea/lista_detail.html'



class ListaDeleteView(generic.DeleteView):
	model = Lista
	template_name = 'tarea/lista_delete.html'
	success_url = reverse_lazy('tarea:clase_index')



class TareaIndexView(BaseView, generic.ListView):
	active_title = 'tarea'
	model = Tarea
	template_name = 'tarea/tarea_index.html'
		
	def get_queryset(self):
		queryset = Tarea.objects.filter(fecha_creacion_tarea__lte=timezone.now()).order_by('-fecha_creacion_tarea')
		return queryset



class TareaCreateView(generic.CreateView):
	model = Tarea
	form_class = TareaForm
	template_name = 'tarea/tarea_form.html'
	success_url = reverse_lazy('tarea:clase_tarea')


class TareaUpdateView(generic.UpdateView):
	model = Tarea
	form_class = TareaForm
	template_name = 'tarea/tarea_form.html'
	success_url = reverse_lazy('tarea:clase_tarea')



class TareaDeleteView(generic.DeleteView):
	model = Tarea
	template_name = 'tarea/tarea_delete.html'
	success_url = reverse_lazy('tarea:clase_tarea')


class TareaPendiente(generic.ListView):
	model = Tarea
	
	template_name = 'tarea/tareas_pendientes.html'
	def get_queryset(self):
		queryset = Tarea.objects.exclude(terminado=True)
		return queryset



class TareaTerminadaMes(generic.ListView):
	model = Tarea
	template_name = 'tarea/tareas_terminadas.html'

	def get_queryset(self):
		queryset = Tarea.objects.filter(fecha_modificacion__month=timezone.now().month, terminado=True)
		return queryset



class TareaPendienteMes(generic.ListView):
	model = Tarea
	template_name = 'tarea/tareas_pendientes_mes.html'

	def get_queryset(self):
		
		queryset = Tarea.objects.filter( fecha_creacion_tarea__lt= timezone.now() - timedelta(days=30), terminado=False )
		return queryset

def terminarTarea(request, lista_id):
	lista = get_object_or_404(Lista, pk= lista_id)
	try:
		id_tarea = request.GET.get('tarea', 0)
		tarea_marcada = lista.tarea_set.select_for_update().get(pk=id_tarea)
	except (KeyError, Tarea.DoesNotExist):
		message_text = "Error"
		messages.add_message(request, messages.ERROR, message_text)
		return render(request, 'tarea/lista_detail.html',  {
			'lista':lista,
			'error_message': message_text,

			})
	else:


		tarea_marcada.terminado= True
		tarea_marcada.save()
		message_text = "Tarea Finalizada"
		messages.add_message(request, messages.SUCCESS, message_text)
		return HttpResponseRedirect(reverse('tarea:detalle_lista', args=(lista.id,)))

def desmarcar(request, lista_id):
	lista = get_object_or_404(Lista, pk= lista_id)
	try:
		id_tarea = request.GET.get('tarea', 0)
		tarea_marcada = lista.tarea_set.select_for_update().get(pk=id_tarea)
	except (KeyError, Tarea.DoesNotExist):
		message_text = "Error"
		messages.add_message(request, messages.ERROR, message_text)
		return render(request, 'tarea/lista_detail.html',  {
			'lista':lista,
			'error_message': message_text,

			})
	else:
		if tarea_marcada.fecha_creacion_tarea >= timezone.now() - timedelta(days=30):
			tarea_marcada.terminado= False
			tarea_marcada.save()
			message_text = "Tarea Finalizada"
			messages.add_message(request, messages.SUCCESS, message_text)
			return HttpResponseRedirect(reverse('tarea:detalle_lista', args=(lista.id,)))
		else: 
			message_text = "No se puede desmarcar esta tarea"
			messages.add_message(request, messages.ERROR, message_text)
			return HttpResponseRedirect(reverse('tarea:detalle_lista', args=(lista.id,)))








	





	