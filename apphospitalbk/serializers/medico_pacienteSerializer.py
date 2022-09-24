from rest_framework import serializers
from apphospitalbk.models.medico_paciente import MedicoPaciente


class MedicoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoPaciente
        fields = ['id_medpac', 'id_paciente_medpac', 'id_medico_medpac','id_registra_medpac', 'fechaIni_medpac', 'fechaFin_medpac']

