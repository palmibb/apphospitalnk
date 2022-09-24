from rest_framework import serializers
from apphospitalbk.models.signosvitales import SignosVitales


class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['id_sgv', 'id_paciente_sgv', 'satOxigeno_sgv', 'presion_sgv', 'freCardiaca_sgv','create_date_sgv']
        