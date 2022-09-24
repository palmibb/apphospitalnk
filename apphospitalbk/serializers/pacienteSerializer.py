from rest_framework import serializers
from apphospitalbk.models.paciente import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id_pac', 'id_usuario_pac', 'id_registra_pac']
        
