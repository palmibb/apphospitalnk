from rest_framework import serializers
from apphospitalbk.models.auxiliar import Auxiliar


class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['id_aux', 'id_usuario_aux']


