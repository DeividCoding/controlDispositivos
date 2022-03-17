from rest_framework import serializers
from .models import dispositivos,cat_tipo_dispositivo,ticket,comentarios
from usuario.serializers import UsuariosSerializer




class ComentariosSerializer(serializers.ModelSerializer):
    nombreUsuario=serializers.SerializerMethodField()
    class Meta:
        model=comentarios
        #fields='__all__'

        fields=(
            'id_ticket',
            'id_usuario',
            'nombreUsuario',
            'comentario'


        )

    def get_nombreUsuario(self,obj):
        return obj.id_usuario.nombre


class TicketSerializer(serializers.ModelSerializer):
    comentarios=serializers.SerializerMethodField()
    nombreUsuario=serializers.SerializerMethodField()
    nombreDispositivo=serializers.SerializerMethodField()
    tipoUsuario=serializers.SerializerMethodField()
    
    class Meta:
        model=ticket
        #fields='__all__'
        fields=(
            'id_dispositivo',
            'nombreDispositivo',
            'id_usuario',
            'tipoUsuario',
            'nombreUsuario',
            'descripccion',
            'send_email',
            'comentarios'
        )
    
    def get_nombreDispositivo(self,obj):
        return obj.id_dispositivo.nombre

    def get_nombreUsuario(self,obj):
        return obj.id_usuario.nombre

    def get_tipoUsuario(self,obj):
        return obj.id_usuario.id_tipo_usuario.tipo_usuario

    def get_comentarios(self,obj):
        comentariosDelTicket=comentarios.objects.filter(
            id_ticket=obj.id
        )

        comentariosDelTicket_ser=ComentariosSerializer(comentariosDelTicket,many=True).data

        return comentariosDelTicket_ser


class DispositivosSerializerBasico(serializers.ModelSerializer):
    '''
    Mostrara todos los datos del dispositivo, incluidos los tickets
    que se le han generado a lo largo del tiempo
    '''
    class Meta:
        model=dispositivos    
        fields='__all__'


class TipoDispoitivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=cat_tipo_dispositivo
        fileds='__all__'
















class DispositivosSerializer(serializers.ModelSerializer):
    '''
    Mostrara todos los datos del dispositivo, incluidos los tickets
    que se le han generado a lo largo del tiempo
    '''

    # mas de una persona puede estar a cargo de un dispositivo...
    usuariosEncargados=UsuariosSerializer(many=True)

    # tickets que se han realizado del dispositivo...
    tickets=serializers.SerializerMethodField()
    tipoDeDispositivo=serializers.SerializerMethodField()
    #tickets=TicketSerializer()
    class Meta:
        model=dispositivos    
        #fields='__all__'
        fields=(
            'nombre',
            'id',
            'tipoDeDispositivo',
            'usuariosEncargados',
            'tickets'
        )

    def get_tickets(self,obj):
        #return "{}".format(obj.get_ticketsAsignados.all())
        return TicketSerializer(  obj.get_ticketsAsignados.all(),many=True  ).data
    
    def get_tipoDeDispositivo(self,obj):
        return obj.id_tipo.tipo_dispositivo


class TipoDispoitivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=cat_tipo_dispositivo
        fileds='__all__'







