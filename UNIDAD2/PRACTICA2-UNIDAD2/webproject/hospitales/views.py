from django.shortcuts import render, redirect,get_object_or_404
from hospitales.models import Paciente, Consulta, Doctor, Expediente, Hospital, Habitacion
from hospitales.forms import PacienteForm, ConsultaForm, DoctorForm, ExpedienteForm, HospitalForm, HabitacionForm

# Create your views here.

#CRUD pacientes
def detallePaciente(request,id):
    paciente = get_object_or_404(Paciente,pk=id)
    return render(request,'detallePaciente.html',{'paciente':paciente})

def nuevoPaciente(request):
    if request.method == "POST":
        formaPaciente = PacienteForm(request.POST)
        if formaPaciente.is_valid():
            formaPaciente.save()
            return redirect('index')
    else:
        formaPaciente=PacienteForm()
        return render(request,'agregarPaciente.html',{'formaPaciente':formaPaciente})

def editarPaciente(request,id):
    paciente = get_object_or_404(Paciente,pk=id)
    if request.method == "POST":
        formaPaciente = PacienteForm(request.POST,instance=paciente)
        if formaPaciente.is_valid():
            formaPaciente.save()
            return redirect('index')
    else:
        formaPaciente = PacienteForm(instance=paciente)
        return render(request,'editarPaciente.html',{'formaPaciente':formaPaciente})

def eliminarPaciente(request,id):
    paciente = get_object_or_404(Paciente,pk=id)
    if paciente:
        paciente.delete()
    return redirect('index')


#CRUD consultas
def detalleConsulta(request,id):
    consulta = get_object_or_404(Consulta,pk=id)
    return render(request,'detalleConsulta.html',{'autor':consulta})

def nuevaConsulta(request):
    if request.method == "POST":
        formaConsulta = ConsultaForm(request.POST)
        if formaConsulta.is_valid():
            formaConsulta.save()
            return redirect('index')
    else:
        formaConsulta=ConsultaForm()
        return render(request,'agregarConsulta.html',{'formaConsulta':formaConsulta})

def editarConsulta(request,id):
    consulta = get_object_or_404(Consulta,pk=id)
    if request.method == "POST":
        formaConsulta = ConsultaForm(request.POST,instance=consulta)
        if formaConsulta.is_valid():
            formaConsulta.save()
            return redirect('index')
    else:
        formaConsulta = ConsultaForm(instance=consulta)
        return render(request,'editarConsulta.html',{'formaConsulta':formaConsulta})

def eliminarConsulta(request,id):
    consulta = get_object_or_404(Consulta,pk=id)
    if consulta:
        consulta.delete()
    return redirect('index')

#CRUD doctor
def detalleDoctor(request,id):
    doctor = get_object_or_404(Doctor,pk=id)
    return render(request,'detalleDoctor.html',{'doctor':doctor})

def nuevoDoctor(request):
    if request.method == "POST":
        formDoctor = DoctorForm(request.POST)
        if formDoctor.is_valid():
            formDoctor.save()
            return redirect('index')
    else:
        formDoctor=DoctorForm()
        return render(request,'agregarDoctor.html',{'formaDoctor':formDoctor})

def editarDoctor(request,id):
    doctor = get_object_or_404(Doctor,pk=id)
    if request.method == "POST":
        formaDoctor = DoctorForm(request.POST,instance=doctor)
        if formaDoctor.is_valid():
            formaDoctor.save()
            return redirect('index')
    else:
        formaDoctor = DoctorForm(instance=doctor)
        return render(request,'editarDoctor.html',{'formaDoctor':formaDoctor})

def eliminarDoctor(request,id):
    doctor = get_object_or_404(Doctor,pk=id)
    if doctor:
        doctor.delete()
    return redirect('index')



#CRUD expediente
def detalleExpediente(request,id):
    expediente = get_object_or_404(Expediente,pk=id)
    return render(request,'detalleExpediente.html',{'expediente':expediente})

def nuevoExpediente(request):
    if request.method == "POST":
        formaExpediente = ExpedienteForm(request.POST)
        if formaExpediente.is_valid():
            formaExpediente.save()
            return redirect('index')
    else:
        formaExpediente=ExpedienteForm()
        return render(request,'agregarExpediente.html',{'formaExpediente':formaExpediente})

def editarExpediente(request,id):
    expediente = get_object_or_404(Expediente,pk=id)
    if request.method == "POST":
        formaExpediente = ExpedienteForm(request.POST,instance=expediente)
        if formaExpediente.is_valid():
            formaExpediente.save()
            return redirect('index')
    else:
        formaExpediente = ExpedienteForm(instance=expediente)
        return render(request,'editarExpediente.html',{'formaExpediente':formaExpediente})

def eliminarExpediente(request,id):
    expediente = get_object_or_404(Expediente,pk=id)
    if expediente:
        expediente.delete()
    return redirect('index')

#CRUD hospital
def detalleHospital(request,id):
    hospital = get_object_or_404(Hospital,pk=id)
    return render(request,'detalleHospital.html',{'hospital':hospital})

def nuevoHospital(request):
    if request.method == "POST":
        formaHospital = HospitalForm(request.POST)
        if formaHospital.is_valid():
            formaHospital.save()
            return redirect('index')
    else:
        formaHospital=HospitalForm()
        return render(request,'agregarHospital.html',{'formaHospital':formaHospital})

def editarHospital(request,id):
    hospital = get_object_or_404(Hospital,pk=id)
    if request.method == "POST":
        formaHospital = HospitalForm(request.POST,instance=hospital)
        if formaHospital.is_valid():
            formaHospital.save()
            return redirect('index')
    else:
        formaHospital = HospitalForm(instance=hospital)
        return render(request,'editarHospital.html',{'formaHospital':formaHospital})

def eliminarHospital(request,id):
    hospital = get_object_or_404(Hospital,pk=id)
    if hospital:
        hospital.delete()
    return redirect('index')

#CRUD habitacion
def detalleHabitacion(request,id):
    habitacion = get_object_or_404(Habitacion,pk=id)
    return render(request,'detalleHabitacion.html',{'habitacion':habitacion})

def nuevaHabitacion(request):
    if request.method == "POST":
        formaHabitacion = HabitacionForm(request.POST)
        if formaHabitacion.is_valid():
            formaHabitacion.save()
            return redirect('index')
    else:
        formaHabitacion=HabitacionForm()
        return render(request,'agregarHabitacion.html',{'formaHabitacion':formaHabitacion})

def editarHabitacion(request,id):
    habitacion = get_object_or_404(Habitacion,pk=id)
    if request.method == "POST":
        formaHabitacion = Habitacion(request.POST,instance=habitacion)
        if formaHabitacion.is_valid():
            formaHabitacion.save()
            return redirect('index')
    else:
        formaHabitacion = HabitacionForm(instance=habitacion)
        return render(request,'editarHabitacion.html',{'formaHabitacion':formaHabitacion})

def eliminarHabitacion(request,id):
    habitacion = get_object_or_404(Habitacion,pk=id)
    if habitacion:
        habitacion.delete()
    return redirect('index')
