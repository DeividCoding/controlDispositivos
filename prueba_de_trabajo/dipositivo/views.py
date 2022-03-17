from rest_framework.generics import (
    ListAPIView,CreateAPIView,RetrieveAPIView,
    DestroyAPIView,RetrieveUpdateAPIView
    )
from rest_framework.response import Response


from .serializers import (
    ComentariosSerializer, DispositivosSerializer, TicketSerializer,TipoDispoitivoSerializer,
    DispositivosSerializerBasico
    
    )
from .models import comentarios, dispositivos,ticket


class DispositivosListApiView(ListAPIView):

    serializer_class=DispositivosSerializer

    def get_queryset(self):
        '''
        Nos retornar la lista de resultados particulares que
        cumplan con el filtro
        '''

        return dispositivos.objects.all()
        
        #kword=self.kwargs['kword']
        #return Person.objects.filter(
        #    full_name__icontains=kword
        #)

class DispositivoCreateView(CreateAPIView):
    serializer_class=DispositivosSerializerBasico

class DispositivoDeleteView(DestroyAPIView):
    serializer_class=DispositivosSerializerBasico
    # indicandole donde buscar
    queryset=dispositivos.objects.all()

class DispositivoEditar(RetrieveUpdateAPIView):
    serializer_class=DispositivosSerializerBasico
    # indicandole donde buscar
    queryset=dispositivos.objects.all()

class DipositivoDetailView(RetrieveAPIView):
    serializer_class=DispositivosSerializer
    # indicandole donde buscar
    queryset=dispositivos.objects.all()





#class PersonEditar(RetrieveUpdateAPIView):
#    serializer_class=PersonSerializer
#    # indicandole donde buscar
#    queryset=Person.objects.all()




#####################################################################################################
# TICKETS...
#####################################################################################################
class TicketsListApiView(ListAPIView):

    serializer_class=TicketSerializer

    def get_queryset(self):
        '''
        Nos retornar la lista de resultados particulares que
        cumplan con el filtro
        '''
        
        return ticket.objects.all()

class TicketCreateView(CreateAPIView):
    '''
    Solo podran crear tickets los usuario  de tipo: 1
    '''
    serializer_class=TicketSerializer

    def create(self,request,*args,**kwargs):
        '''
        Cada vez que se hace un metodo POST, este 
        metodo sera llamado, con la finalidad de registrar
        los datos que vienen en el POST
        '''

        datosEnviadosPorPost=request.data
        datosSerializados=TicketSerializer(data=datosEnviadosPorPost)
        datosSerializados.is_valid(raise_exception=True)
        usuarioCreadorTicket=datosSerializados.validated_data['id_usuario']
        tipoUsuario=usuarioCreadorTicket.id_tipo_usuario.tipo_usuario

        
        # solo pueden crear tickets los usuario de tipo: 1
        if tipoUsuario==1:
            print("Solo tu puedes crear el ticket")

            ticketCreara=ticket.objects.create(
                   id_dispositivo=datosSerializados.validated_data['id_dispositivo'],
                   id_usuario=datosSerializados.validated_data['id_usuario'],
                   descripccion=datosSerializados.validated_data['descripccion'],
                   send_email=datosSerializados.validated_data['send_email'],
                   activo=True
            ) 

            ticketCreara.save()

            return  Response(
                {
                    'estatus':"Registro de ticket exitoso"
                }
            )
        else:
            return  Response(
                {
                    'estatus':"Registro denegado,solo los usuario de tipo:1 pueden crear los tickets"
                }
            )

#####################################################################################################
# CRUDS COMENTARIOS...
#####################################################################################################
class ComentarioListApiView(ListAPIView):
    serializer_class=ComentariosSerializer
    def get_queryset(self):
        '''
        Nos retornar la lista de resultados particulares que
        cumplan con el filtro
        '''
        return comentarios.objects.all()

class ComentarioCreateView(CreateAPIView):
    '''
    Solo podran crear tickets los usuario  de tipo: 1
    '''
    serializer_class=ComentariosSerializer

    def create(self,request,*args,**kwargs):
        '''
        Cada vez que se hace un metodo POST, este 
        metodo sera llamado, con la finalidad de registrar
        los datos que vienen en el POST
        '''

        datosEnviadosPorPost=request.data
        datosSerializados=ComentariosSerializer(data=datosEnviadosPorPost)
        datosSerializados.is_valid(raise_exception=True)
        usuarioCreadorTicket=datosSerializados.validated_data['id_usuario']
        tipoUsuario=usuarioCreadorTicket.id_tipo_usuario.tipo_usuario

        # solo pueden crear comentarios los usuario de tipo: 3
        if tipoUsuario==3:
            print("Solo tu puedes crear comentarios")

            comentarioCreara=comentarios.objects.create(
                   id_ticket=datosSerializados.validated_data['id_ticket'],
                   id_usuario=datosSerializados.validated_data['id_usuario'],
                   comentario=datosSerializados.validated_data['comentario'],
                   activo=True
            ) 
            comentarioCreara.save()

            return  Response(
                {
                    'estatus':"Registro de comentario exitoso"
                }
            )
        else:
            return  Response(
                {
                    'estatus':"Registro denegado,solo los usuario de tipo:3 pueden crear los comentarios"
                }
            )




