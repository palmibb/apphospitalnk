from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class HistoriaClinica(models.Model):
    id_hc = models.BigAutoField(primary_key=True)
    id_paciente_hc = models.ForeignKey(Paciente, related_name='PacienteHC', on_delete=models.CASCADE)
    observaciones_hc = models.CharField('obeservaciones', max_length = 200)
    create_date_hc = models.DateTimeField('Fecha Registro')
    activo_hc = models.BooleanField(default=True)