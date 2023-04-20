import sys
sys.path.append('./')
from logger_base import log

class Paciente:
    def __init__(self, idpaciente = None, nombre=None, apellido=None, edad=None, telefono=None) -> None:
        self._idpaciente = idpaciente
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._telefono = telefono
    
    def __str__(self) -> str:
        
        return f"""
        Id Paciente: {self._idpaciente}, Nombre: {self._nombre}
        Apellido: {self._apellido}, Edad: {self._edad}, Telefono: {str(self._telefono)}
        """
    
    @property
    def idPaciente(self):
        return self._idpaciente
    @idPaciente.setter
    def idPaciente(self, idpaciente):
        self._idpaciente = idpaciente

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
    def Edad(self):
        return self._edad
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad

    @property
    def Telefono(self):
        return self._telefono
    @Telefono.setter
    def Telefono(self, telefono):
        self._telefono = telefono

if __name__ == "__main__":
    paciente1 = Paciente(1,"Juan", "Perez", 20,"8672335413")
    log.debug(paciente1)

