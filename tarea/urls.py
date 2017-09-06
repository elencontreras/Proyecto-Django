from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name ="clase_index"),
    url(r'^create/lista$', views.ListaCreateView.as_view(), name ="crear_lista"),
    url(r'^edit/(?P<pk>[0-9]+)$', views.ListaUpdateView.as_view(), name ="modificar_lista"),
    url(r'^(?P<pk>[0-9]+)$', views.DetailList.as_view(), name ="detalle_lista"),
    url(r'^eliminar/lista(?P<pk>[0-9]+)$', views.ListaDeleteView.as_view(), name ="eliminar_lista"),
    url(r'^tareas$', views.TareaIndexView.as_view(), name ="clase_tarea"),
    url(r'^create/tarea$', views.TareaCreateView.as_view(), name ="crear_tarea"),
    url(r'^edit/tarea(?P<pk>[0-9]+)$', views.TareaUpdateView.as_view(), name ="modificar_tarea"),
    url(r'^eliminar/tarea(?P<pk>[0-9]+)$', views.TareaDeleteView.as_view(), name ="eliminar_tarea"),
    url(r'^pendientes$', views.TareaPendiente.as_view(), name ="tareas_pendientes"),
    url(r'^terminadas$', views.TareaTerminadaMes.as_view(), name ="tareas_terminadas"),
    url(r'^pendiente/mes$', views.TareaPendienteMes.as_view(), name ="tareas_pendientes_mes"),
    url(r'^(?P<lista_id>[0-9]+)/finalizada$', views.terminarTarea, name ="marcar_tarea"),
    url(r'^(?P<lista_id>[0-9]+)/curso$', views.desmarcar, name ="desmarcar_tarea"),

]