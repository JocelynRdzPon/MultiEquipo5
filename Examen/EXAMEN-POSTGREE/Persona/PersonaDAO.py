import sys
sys.path.append('./')

from Persona import Persona
from cursorDelPool import CursorDelPool
from logger_base import log
from conexion import Conexion

class PersonaDAO:

    _SELECCIONAR= "SELECT * FROM persona ORDER BY id"
    _INSERTAR = "INSERT INTO persona(nombre,edad,correo) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, edad = %s, correo =%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad,persona.Correo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad, persona.Correo, persona.idP)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,persona):
        with CursorDelPool as cursor:
            valores = (persona.id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    ###Insertar
    # doctor1 = Persona(nombre="Antonia",edad= "18",correo="antonia@gmail.com" )
    # doctoresInsertados = PersonaDAO.insertar(doctor1)
    # log.debug(f"Doctores Agregados: {doctoresInsertados}")
   
   

    # # UPDATE
    # doctor1 = Persona(nombre="Maria",edad= "18",correo="antonia@gmail.com", id="1" )
    # doctoresActualizados = DoctorDAO.actualizar(doctor1)
    # log.debug(f"Doctor Eliminado {doctoresActualizados}")

    # # DELETE
    doctor1 = Persona(iddoctor = 2)
    doctoresEliminados = PersonaDAO.eliminar(doctor1)
    log.debug(f"Doctor Eliminado {doctoresEliminados}")
    #Leer
    doctores = PersonaDAO.seleccionar()
    for d in doctores:
        log.debug(d)