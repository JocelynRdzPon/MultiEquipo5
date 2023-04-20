import sys
sys.path.append('./')
from logger_base import log

class ContratoPersona:
    def __init__(self, id = None, idpersona=None, idcontrato=None) -> None:
        self._id = id
        self._idPersona = idpersona
        self._idContrato = idcontrato
        
    
    def __str__(self) -> str:
        
        return f"""
        Id Contrato_Persona: {self._id}, Id Persona: {self._nocontrato}
        Id Contrato: {self._costo}
        """
    
    @property
    def idC(self):
        return self._id
    @idC.setter
    def idC(self, id):
        self._id = id

    @property
    def IdPersona(self):
        return self._idPersona
    @IdPersona.setter
    def IdPersona(self, idpersona):
        self._idPersona = idpersona
    
    @property
    def IdContrato(self):
        return self._idContrato
    @IdContrato.setter
    def Contrato(self, idcontrato):
        self._idContrato = idcontrato





