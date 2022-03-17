
from django.urls import path
from . import views

app_name="dispositivos_app"

urlpatterns=[
    # Buscando por filtro la lista de tickets de un dispositivo en especifico
    path('api/ticketsDe/<idDipositivo>/',views.TicketsDeUnDispositivoListApiView.as_view(),name="ticketsDeDispositivo_list"),

    # CRUD  dispositivos...
    path('api/dispositivos/list/',views.DispositivosListApiView.as_view(),name="dipositivos_list"),
    path('api/dispositivos/create/',views.DispositivoCreateView.as_view(),name="dipositivos_create"),
    path('api/dispositivos/update/<pk>/',views.DispositivoEditar.as_view(),name="dipositivos_update"),
    path('api/dispositivos/delete/<pk>/',views.DispositivoDeleteView.as_view(),name="dipositivos_delete"),
    path('api/dispositivos/detail/<pk>/',views.DipositivoDetailView.as_view(),name='dispositivos_detail'),


   # tickets ... SOLO LOS PUEDEN CREAR LOS  USUARIOS DE TIPO 1
   path('api/tickets/list/',views.TicketsListApiView.as_view(),name="dipositivos_list"),
   path('api/tickets/create/',views.TicketCreateView.as_view(),name="dipositivos_create"),
   
   # comentarios CRUD... SOLO LOS PUEDEN CREAR LOS USUARIOS DE TIPO 3
   path('api/comentarios/list/',views.ComentarioListApiView.as_view(),name="comentarios_list"),
   path('api/comentarios/create/',views.ComentarioCreateView.as_view(),name="comentarios_create"),
   

]