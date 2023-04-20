import sys
sys.path.append('./')
from logger_base import log

class Contrato:
    def __init__(self, id = None, nocontrato=None, costo=None, fechainicio=None, fechafin=None) -> None:
        self._id = id
        self._nocontrato = nocontrato
        self._costo = costo
        self._fechainicio = fechainicio
        self._fechafin = fechafin
    
    def __str__(self) -> str:
        
        return f"""
        Id Contrato: {self._id}, No Contrato: {self._nocontrato}
        Costo: {self._costo}, Fecha inicio: {self._fechainicio}, Fecha Fin: {str(self._fechafin)}
        """
    
    @property
    def idC(self):
        return self._id
    @idC.setter
    def idC(self, id):
        self._id = id

    @property
    def Nocontrato(self):
        return self._nocontrato
    @Nocontrato.setter
    def Nocontrato(self, nocontrato):
        self._nocontrato = nocontrato
    
    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self, costo):
        self._costo = costo

    @property
    def FechaInicio(self):
        return self._fechainicio
    @FechaInicio.setter
    def FechaInicio(self, fechainicio):
        self._fechainicio = fechainicio

    @property
    def FechaFin(self):
        return self._fechafin
    @FechaFin.setter
    def FechaFin(self, fechafin):
        self._fechafin = fechafin


if __name__ == "__main__":
    contrato1 = Contrato(1,"Juan", "Perez", "Odontologia","drjuanp@hospital.com")
    log.debug(contrato1)

