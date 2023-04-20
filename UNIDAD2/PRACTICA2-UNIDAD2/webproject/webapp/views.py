from django.shortcuts import render
from hospitales.models import Paciente, Consulta, Doctor, Expediente, Hospital, Habitacion

# Create your views here.
def index(req):
    paciente = Paciente.objects.order_by('id')
    consulta = Consulta.objects.order_by('id')
    doctor = Doctor.objects.order_by('id')
    expediente = Expediente.objects.order_by('id')
    hospital = Hospital.objects.order_by('id')
    habitacion = Habitacion.objects.order_by('id')

    return render(req,'index.html',{'paciente':paciente, 'consulta':consulta, 'doctor':doctor, 'expediente':expediente, 'hospital': hospital, 'habitacion': habitacion })


