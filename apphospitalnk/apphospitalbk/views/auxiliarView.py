from ast import Delete
from cgitb import lookup
from logging import exception
from apphospitalbk.models.auxiliar import Auxiliar
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from models.auxiliar import Auxiliar
from apphospitalbk.serializers.usuarioSerializer import UsuarioSerializer
from apphospitalbk.serializers.auxiliarSerializer import AuxiliarSerializer

class AuxiliarListCreateView(generics.ListCreateAPIView):
    queryset= Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Auxiliares")
        queryset=   self.get_queryset()
        serializer = AuxiliarSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POST a Auxiliares")
        print(request.data)
        usuarioData = request.data.pop('Usuario')
        seriallizerU = UsuarioSerializer(data=usuarioData)
        seriallizerU.is_valid(raise_exception=True)
        Usuario=seriallizerU.save()

        auxData = request.data
        auxData.update({"Usuario":id_usuario_aux.id})
        seriallizerAux = AuxiliarSerializer(data=auxData)
        seriallizerAux.is_valid(raise_exception=True)
        seriallizerAux.save()
        return Response(status=status.HTTP_201_CREATED)

        """tokenData = {
                "username":request.data["username"],
                "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)"""
        
    

class AuxiliarRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset= Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer
    lookup_field = "id_aux"        #campo con el que se realiza la busqueda
    lookup_url_kwarg = "pk"         #nomnre dadio en el argumentp de la URL
    #permission_classes = (IsAuthenticated,)

def get (self, request, *args, **kwargs):
    print("GET a Auxiliar")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)

def put (self, request, *args, **kwargs):
    print("PUT a Auxiliar")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)