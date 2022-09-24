from django.contrib import admin

from apphospitalbk.models import usuario
from .models.usuario import Usuario
from .models.auxiliar import Auxiliar
from .models.paciente import Paciente
from .models.medico import Medico
from .models.historia_clinica import HistoriaClinica
from .models.medico_paciente import MedicoPaciente
from .models.signosvitales import SignosVitales
    
admin.site.register(Usuario)
admin.site.register(Auxiliar)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(HistoriaClinica)
admin.site.register(MedicoPaciente)
admin.site.register(SignosVitales)
