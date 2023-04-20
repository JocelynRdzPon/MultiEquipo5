import sys
sys.path.append('./')

from Paciente import Paciente
from cursorDelPool import CursorDelPool
from logger_base import log

class PacienteDAO:

    _SELECCIONAR= "SELECT * FROM paciente ORDER BY idpaciente"
    _INSERTAR = "INSERT INTO paciente(nombre,apellido,edad,telefono) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE paciente SET nombre = %s, apellido = %s, edad =%s, telefono =%s WHERE idpaciente = %s"
    _ELIMINAR = "DELETE FROM paciente WHERE idpaciente = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            pacientes = []
            for r in registros:
                paciente = Paciente(r[0],r[1],r[2],r[3],r[4])
                pacientes.append(paciente)
            return pacientes
    
    @classmethod
    def insertar(cls,paciente):
        with CursorDelPool() as cursor:
            valores = (paciente.Nombre, paciente.Apellido,paciente.Edad,paciente.Telefono)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,paciente):
        with CursorDelPool() as cursor:
            valores = (paciente.Nombre, paciente.Apellido, paciente.Edad, paciente.Telefono, paciente.idPaciente)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,paciente):
        with CursorDelPool as cursor:
            valores = (paciente.idPaciente,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    ###Insertar
    paciente1 = Paciente(nombre="Antonia",apellido= "Rodriguez",edad=22, telefono="85671233" )
    pacientesInsertados = PacienteDAO.insertar(paciente1)
    log.debug(f"´Pacientes Agregados: {pacientesInsertados}")
    #UPDATE
    paciente2 = Paciente(nombre="Jacqueline",apellido= "Rodriguez",edad=28, telefono="8671235434", idpaciente=2)
    pacientesActualizados = PacienteDAO.actualizar(paciente2)
    log.debug(f"Pacientes Actualizados {pacientesActualizados}")
    #DELETE
    # pacientesEliminados = PacienteDAO.eliminar(paciente2)
    # log.debug(f"Paciente Eliminado {pacientesEliminados}")
    #Leer
    pacientes = PacienteDAO.seleccionar()
    for p in pacientes:
        log.debug(p)