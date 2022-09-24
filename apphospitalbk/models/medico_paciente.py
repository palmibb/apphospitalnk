from django.db import models
from .auxiliar import Auxiliar
from .paciente import Paciente
from .medico import Medico

class MedicoPaciente(models.Model):
    id_medpac = models.BigAutoField(primary_key=True)
    id_paciente_medpac = models.ForeignKey(Paciente, related_name='PacienteMedPac', on_delete=models.CASCADE)
    id_medico_medpac = models.ForeignKey(Medico, related_name='MedicoMedPAC', on_delete=models.CASCADE)
    id_registra_medpac = models.ForeignKey(Auxiliar, related_name='AuxiliarRegistraMedPac', on_delete=models.CASCADE)
    fechaIni_medpac = models.DateTimeField('Fecha Inicio')
    fechaFin_medpac = models.DateTimeField('Fecha Fin')