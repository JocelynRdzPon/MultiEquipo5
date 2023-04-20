import sys
sys.path.append('./')
from logger_base import log

class Doctor:
    def __init__(self, iddoctor = None, nombre=None, apellido=None, especialidad=None, email=None) -> None:
        self._iddoctor = iddoctor
        self._nombre = nombre
        self._apellido = apellido
        self._especialidad = especialidad
        self._email = email
    
    def __str__(self) -> str:
        
        return f"""
        Id Doctor: {self._iddoctor}, Nombre: {self._nombre}
        Apellido: {self._apellido}, Especialidad: {self._especialidad}, Email: {str(self._email)}
        """
    
    @property
    def idDoctor(self):
        return self._iddoctor
    @idDoctor.setter
    def idDoctor(self, iddoctor):
        self._iddoctor = iddoctor

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def Apellido(self):
        return self._apellido
    @Apellido.setter
    def Apellido(self, apellido):
        self._apellido = apellido

    @property
    def Especialidad(self):
        return self._especialidad
    @Especialidad.setter
    def Especialidad(self, especialidad):
        self._especialidad = especialidad

    @property
    def Email(self):
        return self._email
    @Email.setter
    def Email(self, email):
        self._email = email

if __name__ == "__main__":
    doctor1 = Doctor(1,"Juan", "Perez", "Odontologia","drjuanp@hospital.com")
    log.debug(doctor1)

