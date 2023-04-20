import sys
sys.path.append('./')
from logger_base import log

class Persona:
    def __init__(self, id = None, nombre=None, edad=None, correo=None) -> None:
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._correo = correo
    
    def __str__(self) -> str:
        
        return f"""
        Id ´Persona: {self._id}, Nombre: {self._nombre}
        Edad: {self._edad}, Correo: {self._correo}
        """
    @property
    def idP(self):
        return self._id
    @idP.setter
    def idP(self, id):
        self._id = id

    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad
    
    @property
    def Correo(self):
        return self._correo
    @Correo.setter
    def Correo(self, correo):
        self._apellido = correo

    