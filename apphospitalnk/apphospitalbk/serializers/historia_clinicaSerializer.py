from rest_framework import serializers
from apphospitalbk.models.historia_clinica import HistoriaClinica


class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id_hc', 'id_paciente_hc', 'observaciones_hc','create_date_hc', 'activo_hc']




