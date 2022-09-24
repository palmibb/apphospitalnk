from django.db import models
from .usuario import Usuario
from .auxiliar import Auxiliar

class Paciente(models.Model):
    id_pac = models.BigAutoField(primary_key=True)
    id_usuario_pac = models.ForeignKey(Usuario, related_name='UsuarioPaciente', on_delete=models.CASCADE)
    id_registra_pac = models.ForeignKey(Auxiliar, related_name='AuxiliarRegistraPac', on_delete=models.CASCADE)