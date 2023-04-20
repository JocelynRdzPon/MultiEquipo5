import sys
sys.path.append('./')
from logger_base import log

class Consulta:
    def __init__(self, idconsulta = None, paciente=None, motivoconsulta=None, tratamiento=None, diagnostico=None) -> None:
        self._idconsulta = idconsulta
        self._paciente = paciente
        self._motivoconsulta = motivoconsulta
        self._tratamiento = tratamiento 
        self._diagnostico = diagnostico   
    def __str__(self) -> str:
        
        return f"""
        Id Consulta: {self._idconsulta}, Paciente: {self._paciente}
        MotivoConsulta: {self._motivoconsulta}, Tratamiento: {self._tratamiento}, Diagnostico: {str(self._diagnostico)}
        """
    
    @property
    def idConsulta(self):
        return self._idconsulta
    @idConsulta.setter
    def idConsulta(self, idconsulta):
        self._idconsulta = idconsulta

    @property
    def Paciente(self):
        return self._paciente
    @Paciente.setter
    def Paciente(self, paciente):
        self._paciente = paciente
    
    @property
    def MotivoConsulta(self):
        return self._motivoconsulta
    @MotivoConsulta.setter
    def MotivoConsulta(self, motivoconsulta):
        self._motivoconsulta = motivoconsulta

    @property
    def Tratamiento(self):
        return self._tratamiento
    @Tratamiento.setter
    def Tratamiento(self, tratamiento):
        self._tratamiento = tratamiento

    @property
    def Diagnostico(self):
        return self._diagnostico
    @Diagnostico.setter
    def Diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

if __name__ == "__main__":
    consulta1 = Consulta(1,"Juan  Perez", "Sintomas de resfriado", "Jarabe, pastillas","Gripa")
    log.debug(consulta1)

