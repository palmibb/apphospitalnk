from django.db import models
from .usuario import Usuario


class Auxiliar(models.Model):
    id_aux = models.BigAutoField(primary_key=True)
    id_usuario_aux = models.ForeignKey(Usuario, related_name='Auxiliar', on_delete=models.CASCADE)
    #id_registra_aux = models.ForeignKey(Auxiliar, related_name='AuxiliarRegistra', on_delete=models.CASCADE)