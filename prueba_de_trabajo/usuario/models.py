from django.db import models

# Create your models here.

class AsuntoTratar(models.Model):
    activo=models.BooleanField("¿Esta activo?")

class cat_tipo_usuario(AsuntoTratar):
    tipo_usuario=models.PositiveSmallIntegerField(verbose_name="Tipo de usuario",unique=True)
    descripccion=models.TextField(verbose_name="Descripccion",blank=True,default="")

    def __str__(self):
        return "Tipo de usuario: {}".format(self.tipo_usuario)


class usuarios(AsuntoTratar):
    id_tipo_usuario=models.ForeignKey(cat_tipo_usuario,on_delete=models.CASCADE,related_name='get_usuariosConEsteTipo',verbose_name="Tipo de usuario:")
    nombre=models.CharField(verbose_name="Nombre del usuario:",max_length=200)
    email=models.EmailField(verbose_name="Correo electronico",max_length=200)
    
    def __str__(self):
        return "USUARIO:{} TIPO DE USUARIO:{}".format(self.nombre,self.id_tipo_usuario.tipo_usuario)
    