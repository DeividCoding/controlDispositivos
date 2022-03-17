from django.shortcuts import render
from django.views.generic import (
    ListView
)
from rest_framework.generics import (
    ListAPIView,CreateAPIView,RetrieveAPIView,
    DestroyAPIView,RetrieveUpdateAPIView
    )

from .serializers import (
    UsuariosSerializer
    )
    
from .models import usuarios

class UsuariosListApiView(ListAPIView):

    serializer_class=UsuariosSerializer

    def get_queryset(self):
        '''
        Nos retornar la lista de resultados particulares que
        cumplan con el filtro
        '''

        return usuarios.objects.all()
        
        #kword=self.kwargs['kword']
        #return Person.objects.filter(
        #    full_name__icontains=kword
        #)

class UsuariosCreateView(CreateAPIView):
    serializer_class=UsuariosSerializer

class UsuariosDetailView(RetrieveAPIView):
    serializer_class=UsuariosSerializer
    # indicandole donde buscar
    queryset=usuarios.objects.all()


class UsuariosDeleteView(DestroyAPIView):
    serializer_class=UsuariosSerializer
    # indicandole donde buscar
    queryset=usuarios.objects.all()

class UsuariosEditar(RetrieveUpdateAPIView):
    serializer_class=UsuariosSerializer
    # indicandole donde buscar
    queryset=usuarios.objects.all()

