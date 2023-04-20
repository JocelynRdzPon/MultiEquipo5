from django.contrib import admin
from hospitales.models import Paciente, Consulta, Doctor, Expediente, Hospital, Habitacion

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Doctor)
admin.site.register(Expediente)
admin.site.register(Hospital)
admin.site.register(Habitacion)