
from django.urls import path
from . import views

app_name="usuarios_app"

urlpatterns=[
    # CRUD USUARIOS...
    
    path('api/usuarios/list/',views.UsuariosListApiView.as_view(),name="usuarios_list"),
    path('api/usuarios/update/<pk>/',views.UsuariosEditar.as_view(),name="usuarios_update"),
    path('api/usuarios/create',views.UsuariosCreateView.as_view(),name="usuarios_create"),
    path('api/usuarios/delete/<pk>/',views.UsuariosDeleteView.as_view(),name="usuarios_delete"),
    path('api/usuarios/detail/<pk>/',views.UsuariosDetailView.as_view(),name='usuarios_detail'),



]