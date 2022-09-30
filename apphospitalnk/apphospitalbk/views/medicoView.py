from ast import Delete
from cgitb import lookup
from logging import exception
from apphospitalbk.models.medico import Medico
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from models.medico import Medico
from apphospitalbk.serializers.usuarioSerializer import UsuarioSerializer
from apphospitalbk.serializers.medicoSerializer import MedicoSerializer

class MedicoListCreateView(generics.ListCreateAPIView):
    queryset= Medico.objects.all()
    serializer_class = MedicoSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Usuarios")
        queryset=   self.get_queryset()
        serializer = MedicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POST a Medico")
        print(request.data)
        usuarioData = request.data.pop('Usuario')
        seriallizerU = UsuarioSerializer(data=usuarioData)
        seriallizerU.is_valid(raise_exception=True)
        Usuario=seriallizerU.save()

        medData = request.data
        medData.update({"Usuario":id_usuario_med.id})
        seriallizerMed = MedicoSerializer(data=medData)
        seriallizerMed.is_valid(raise_exception=True)
        seriallizerMed.save()
        return Response(status=status.HTTP_201_CREATED)

        """tokenData = {
                "username":request.data["username"],
                "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)"""
        
    

class MedicoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset= Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = "id_med"        #campo con el que se realiza la busqueda
    lookup_url_kwarg = "pk"         #nomnre dadio en el argumentp de la URL
    #permission_classes = (IsAuthenticated,)

def get (self, request, *args, **kwargs):
    print("GET a Medico")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)

def put (self, request, *args, **kwargs):
    print("PUT a Medico")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)