from rest_framework import  serializers
from .models import usuarios


class UsuariosSerializer(serializers.ModelSerializer):

    tipoDeUsuario=serializers.SerializerMethodField()
    class Meta:
        model=usuarios
        #fields='__all__'
        #     
        fields=(
            'nombre',
            'id',
            'email',
            'tipoDeUsuario',
            'id_tipo_usuario'
        )
    

    def get_tipoDeUsuario(self,obj):
        return obj.id_tipo_usuario.tipo_usuario

