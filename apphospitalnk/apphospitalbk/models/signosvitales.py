from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class SignosVitales(models.Model):
    id_sgv = models.BigAutoField(primary_key=True)
    id_paciente_sgv = models.ForeignKey(Paciente, related_name='PacienteSGV', on_delete=models.CASCADE)
    satOxigeno_sgv = models.CharField('Saturacion de Oxigeno', max_length = 30)
    presion_sgv= models.CharField('Presion', max_length = 30)
    freCardiaca_sgv = models.CharField('Frecuencia Cardiaca', max_length = 30)
    create_date_sgv = models.DateTimeField('Fecha Registro')
