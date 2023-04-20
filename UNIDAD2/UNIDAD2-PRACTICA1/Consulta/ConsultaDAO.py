import sys
sys.path.append('./')

from Consulta import Consulta
from cursorDelPool import CursorDelPool
from logger_base import log
from conexion import Conexion

class ConsultaDAO:

    _SELECCIONAR= "SELECT * FROM consulta ORDER BY idconsulta"
    _INSERTAR = "INSERT INTO consulta(paciente,motivoconsulta,tratamiento,diagnostico) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE consulta SET paciente = %s, motivoconsulta = %s, tratamiento =%s, diagnostico =%s WHERE idconsulta = %s"
    _ELIMINAR = "DELETE FROM public.consulta WHERE idconsulta = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consultas = []
            for r in registros:
                consulta = Consulta(r[0],r[1],r[2],r[3],r[4])
                consultas.append(consulta)
            return consultas
    
    @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Paciente, consulta.MotivoConsulta,consulta.Tratamiento,consulta.Diagnostico)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Paciente, consulta.MotivoConsulta, consulta.Tratamiento, consulta.Diagnostico, consulta.idConsulta)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,consulta):
        with CursorDelPool as cursor:
            valores = (consulta.idConsulta,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    ##Insertar
    # consulta1 = Consulta(paciente="Antonia Ponce",motivoconsulta= "Malestar estomacal",tratamiento="Pastillas", diagnostico="Infeccion en el estomago" )
    # consultasInsertadas = ConsultaDAO.insertar(consulta1)
    # log.debug(f"Consultas Agregadas: {consultasInsertadas}")
   
    # consulta1 = Consulta(paciente="Enrique Reyes",motivoconsulta= "Sintomas de resfriado",tratamiento="Jarabe, pastillas", diagnostico="Gripe" )
    # consultasInsertadas = ConsultaDAO.insertar(consulta1)
    # log.debug(f"Consultas Agregados: {consultasInsertadas}")

    # # UPDATE
    consulta1 = Consulta(paciente="Jacqueline Ponce",motivoconsulta= "Malestar estomacal",tratamiento="Pastillas", diagnostico="Infeccion en el estomago", idconsulta= 1 )
    consultasActualizadas = ConsultaDAO.actualizar(consulta1)
    log.debug(f"Consulta Eliminada {consultasActualizadas}")

    # # # DELETE
    # doctor1 = Consulta(iddoctor = 2)
    # doctoresEliminados = ConsultaDAO.eliminar(doctor1)
    # log.debug(f"Doctor Eliminado {doctoresEliminados}")
    #Leer
    consultas = ConsultaDAO.seleccionar()
    for c in consultas:
        log.debug(c)