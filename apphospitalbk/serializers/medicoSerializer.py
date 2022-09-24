from rest_framework import serializers
from apphospitalbk.models.medico import Medico


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id_med', 'id_usuario_med', 'id_registra_med']
