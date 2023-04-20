import sys
sys.path.append('./')

from Contrato_Persona import ContratoPersona
from cursorDelPool import CursorDelPool
from logger_base import log
from conexion import Conexion

class DoctorDAO:

    _SELECCIONAR= "SELECT * FROM contrato_persona ORDER BY id"
    _INSERTAR = "INSERT INTO contrato_persona(idpersona,idcontrato) VALUES (%s, %s)"
   
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = ContratoPersona(r[0],r[1],r[2])
                contratos.append(contrato)
            return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.idpersona, contrato.idcontrato)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
   
        
if __name__ == "__main__":
    ###Insertar
    # doctor1 = Doctor(nombre="Antonia",apellido= "Rodriguez",especialidad="Odontologia", email="antoniar@doctors.com" )
    # doctoresInsertados = DoctorDAO.insertar(doctor1)
    # log.debug(f"Doctores Agregados: {doctoresInsertados}")
   
   
    # # UPDATE
    # doctor1 = Doctor(nombre="Jacqueline",apellido= "Ponce",especialidad="Cardiologia", email="jacqueliner@doctors.com", iddoctor=2)
    # doctoresActualizados = DoctorDAO.actualizar(doctor1)
    # log.debug(f"Doctor Eliminado {doctoresActualizados}")

    # # DELETE
    doctor1 = ContratoPersona(iddoctor = 2)
    doctoresEliminados = DoctorDAO.eliminar(doctor1)
    log.debug(f"Doctor Eliminado {doctoresEliminados}")
    #Leer
    doctores = DoctorDAO.seleccionar()
    for d in doctores:
        log.debug(d)