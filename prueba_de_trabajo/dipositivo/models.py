from django.db import models
from usuario.models import AsuntoTratar,usuarios

class cat_tipo_dispositivo(AsuntoTratar):
    tipo_dispositivo=models.PositiveSmallIntegerField(verbose_name="Tipo de dispositivo",unique=True)
    descripccion=models.TextField(verbose_name="Descripccion",blank=True,default="")

    def __str__(self):
        return "Tipo de dispositivo: {}".format(self.tipo_dispositivo)

class dispositivos(AsuntoTratar):
    nombre=models.CharField(max_length=200,verbose_name="Nombre del dispositivo",blank=True,default="")
    id_tipo=models.ForeignKey(cat_tipo_dispositivo,on_delete=models.CASCADE,related_name='get_dispositivos',verbose_name="Tipo de dispositivo")
    # mas de un usuario puede estar al pendiente de un dispositivo...
    usuariosEncargados=models.ManyToManyField(usuarios,related_name='get_dispositivosQueVigila')

    def __str__(self):
        return "Dispositivo con id: {} de tipo: {}".format(self.id,self.id_tipo.id)

class ticket(AsuntoTratar):
    id_dispositivo=models.ForeignKey(dispositivos,on_delete=models.CASCADE,related_name='get_ticketsAsignados',verbose_name="Dispositivo:")
    id_usuario=models.ForeignKey(usuarios,on_delete=models.CASCADE,related_name='get_ticketsHechos',verbose_name="Creador del ticket")
    descripccion=models.TextField(verbose_name="Descripccion: ")
    send_email=models.BooleanField(verbose_name="¿Ya se mando el email de reporte?")
    

    def __str__(self):
        return "Ticket {} del dispositivo: {} por:{}".format(self.id,self.id_dispositivo.id,self.id_usuario.nombre)
    
class comentarios(AsuntoTratar):
    id_ticket=models.ForeignKey(ticket,on_delete=models.CASCADE,related_name='get_comentariosAportados',verbose_name="Ticket que se atiende")
    id_usuario=models.ForeignKey(usuarios,on_delete=models.CASCADE,related_name='get_comentariosHechos',verbose_name="Persona que realiza el comentario")
    comentario=models.TextField(verbose_name="Comentario: ")