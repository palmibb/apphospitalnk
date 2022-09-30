from ast import Delete
from cgitb import lookup
from logging import exception
from apphospitalbk.models.paciente import Paciente
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from models.paciente import Paciente
from apphospitalbk.serializers.usuarioSerializer import UsuarioSerializer
from apphospitalbk.serializers.pacienteSerializer import PacienteSerializer

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset= Paciente.objects.all()
    serializer_class = PacienteSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Pacientes")
        queryset=   self.get_queryset()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POST a Paciente")
        print(request.data)
        usuarioData = request.data.pop('Usuario')
        seriallizerU = UsuarioSerializer(data=usuarioData)
        seriallizerU.is_valid(raise_exception=True)
        Usuario=seriallizerU.save()

        pacData = request.data
        pacData.update({"Usuario":id_usuario_pac.id})
        seriallizerPac = PacienteSerializer(data=pacData)
        seriallizerPac.is_valid(raise_exception=True)
        seriallizerPac.save()
        return Response(status=status.HTTP_201_CREATED)

        """tokenData = {
                "username":request.data["username"],
                "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)"""
        
    

class PacienteRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset= Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = "id_pac"        #campo con el que se realiza la busqueda
    lookup_url_kwarg = "pk"         #nomnre dadio en el argumentp de la URL
    #permission_classes = (IsAuthenticated,)

def get (self, request, *args, **kwargs):
    print("GET a Paciente")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)

def put (self, request, *args, **kwargs):
    print("PUT a Paciente")
    """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
    return super().get(request, *args, **kwargs)