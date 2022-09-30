from ast import Delete
from cgitb import lookup
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from models.usuario import Usuario
from apphospitalbk.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Usuarios")
        queryset=   self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
    

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "id_user"        #campo con el que se realiza la busqueda
    lookup_url_kwarg = "pk"         #nomnre dadio en el argumentp de la URL
    #permission_classes = (IsAuthenticated,)

def get (self, request, *args, **kwargs):
    print("GET a Usuario")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)

def put (self, request, *args, **kwargs):
    print("PUT a Usuario")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)

def delete (self, request, *args, **kwargs):
    print("Delete a Usuario")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)  
