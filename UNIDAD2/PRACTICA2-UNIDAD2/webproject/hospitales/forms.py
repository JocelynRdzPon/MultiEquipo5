from django.forms import ModelForm,EmailInput
from hospitales.models import Paciente, Consulta, Doctor, Expediente, Hospital, Habitacion

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class ExpedienteForm(ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
class HabitacionForm(ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }