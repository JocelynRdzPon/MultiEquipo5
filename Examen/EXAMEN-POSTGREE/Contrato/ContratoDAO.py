import sys
sys.path.append('./')

from Contrato import Contrato
from cursorDelPool import CursorDelPool
from logger_base import log
from conexion import Conexion

class ContratoDAO:

    _SELECCIONAR= "SELECT * FROM contrato ORDER BY id"
    _INSERTAR = "INSERT INTO contrato(nocontrato,costo,fechainicio, fechafin) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE contrato SET nocontrato = %s, costo = %s, fechainicio =%s , fechafin =%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM contrato WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato)
            return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.Nocontrato, contrato.Costo,contrato.FechaInicio, contrato.FechaFin)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.Nocontrato, contrato.Costo,contrato.FechaInicio, contrato.FechaFin, contrato.idC)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,contrato):
        with CursorDelPool as cursor:
            valores = (contrato.id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    ##Insertar
    contrato1 = Contrato(nocontrato="1",costo= "120",fechainicio="12-02-2023", fechafin="30-03-2023" )
    contratosInsertados = ContratoDAO.insertar(contrato1)
    log.debug(f"Doctores Agregados: {contratosInsertados}")
   
    
    # # UPDATE
    contrato1 = Contrato(nocontrato="1",costo= "120",fechainicio="12-02-2023", fechafin="30-03-2023", id="1" )
    doctoresActualizados = ContratoDAO.actualizar(contrato1)
    log.debug(f"Doctor Eliminado {doctoresActualizados}")

    # DELETE
    contrato1 = Contrato(id = 1)
    doctoresEliminados = ContratoDAO.eliminar(contrato1)
    log.debug(f"Doctor Eliminado {doctoresEliminados}")
    #Leer
    doctores = ContratoDAO.seleccionar()
    for d in doctores:
        log.debug(d)