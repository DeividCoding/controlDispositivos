from django.contrib import admin
from .models import *

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display=('nombre','tipoUsuario','activo')

    # ordenando por tipo de usuarios, para que los iguales se
    # ordenen de forma igual
    ordering=('id_tipo_usuario',)


    def tipoUsuario(self,obj):
        return obj.id_tipo_usuario.tipo_usuario


# Register your models here.
class TipoUsuariosAdmin(admin.ModelAdmin):
    list_display=('tipo_usuario','breveDescripccion','activo')

    # ordenando de menor a mayor...
    ordering=('tipo_usuario',)

    def breveDescripccion(self,obj):
        return obj.descripccion[:50]

 

admin.site.register(usuarios,UsuariosAdmin)
admin.site.register(cat_tipo_usuario,TipoUsuariosAdmin)
