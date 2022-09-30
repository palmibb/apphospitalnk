from django.db import models
from .usuario import Usuario
from .auxiliar import Auxiliar

class Medico(models.Model):
    id_med = models.BigAutoField(primary_key=True)
    id_usuario_med = models.ForeignKey(Usuario, related_name='UsuarioMedico', on_delete=models.CASCADE)
    id_registra_med = models.ForeignKey(Auxiliar, related_name='AuxiliarRegistraMed', on_delete=models.CASCADE)