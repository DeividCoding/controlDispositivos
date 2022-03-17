from django.contrib import admin
from .models import *


# Register your models here.
class DispostivoAdmin(admin.ModelAdmin):
    list_display=('nombre','tipoDispositivo','activo')

    # ordenando por tipo de dispositivo, para que los iguales se
    # ordenen de forma igual
    ordering=('id_tipo',)


    def tipoDispositivo(self,obj):
        return obj.id_tipo.tipo_dispositivo



# Register your models here.
class TipoDispositivosAdmin(admin.ModelAdmin):
    list_display=('tipo_dispositivo','breveDescripccion','activo')

    # ordenando de menor a mayor...
    ordering=('tipo_dispositivo',)

    def breveDescripccion(self,obj):
        return obj.descripccion[:50]




# Register your models here.
class TicketsAdmin(admin.ModelAdmin):
    list_display=('id_usuario','id_dispositivo','activo','send_email')


class ComentariosAdmin(admin.ModelAdmin):
    list_display=('id_ticket','id_usuario')




# Register your models here.
admin.site.register(cat_tipo_dispositivo,TipoDispositivosAdmin)
admin.site.register(dispositivos,DispostivoAdmin)
admin.site.register(ticket,TicketsAdmin)
admin.site.register(comentarios,ComentariosAdmin)
