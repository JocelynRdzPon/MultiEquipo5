from django.db import models

# Create your models here.
class Consulta(models.Model):
    motivoconsulta = models.CharField(max_length=200)
    tratamiento = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=125)
    def __str__(self) -> str:
        return f'Consulta {self.id} : {self.motivoconsulta} {self.tratamiento} {self.diagnostico}'
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    peso = models.CharField(max_length=200)
    Consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f'Paciente {self.nombre} {self.apellido} {self.edad} {self.peso} {self.Consulta}'
    
class Expediente(models.Model):
    motivoconsulta = models.CharField(max_length=200)
    medicamento = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=125)
    def __str__(self) -> str:
        return f'Expediente {self.id} : {self.motivoconsulta} {self.medicamento} {self.diagnostico}'

class Doctor(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    Expediente= models.ForeignKey(Expediente, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f' Doctor {self.nombre} {self.apellidos} {self.cedula} {self.especialidad} {self.Expediente}'

class Hospital(models.Model):
    nombre = models.CharField(max_length=200)
    rfc = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f' Hospital {self.nombre} {self.rfc} {self.domicilio}'

class Habitacion(models.Model):
    numero = models.CharField(max_length=255)
    piso = models.CharField(max_length=255)
    categoria = models.CharField(max_length=250)
    def __str__(self) -> str:
        return f' Habitacion {self.numero} {self.piso} {self.categoria}'
