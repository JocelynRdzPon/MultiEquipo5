import sys
sys.path.append('./')

from Doctor import Doctor
from cursorDelPool import CursorDelPool
from logger_base import log
from conexion import Conexion

class DoctorDAO:

    _SELECCIONAR= "SELECT * FROM doctor ORDER BY iddoctor"
    _INSERTAR = "INSERT INTO doctor(nombre,apellido,especialidad,email) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE doctor SET nombre = %s, apellido = %s, especialidad =%s, email =%s WHERE iddoctor = %s"
    _ELIMINAR = "DELETE FROM public.doctor WHERE iddoctor = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            doctores = []
            for r in registros:
                doctor = Doctor(r[0],r[1],r[2],r[3],r[4])
                doctores.append(doctor)
            return doctores
    
    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.Apellido,doctor.Especialidad,doctor.Email)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.Apellido, doctor.Especialidad, doctor.Email, doctor.idDoctor)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,doctor):
        with CursorDelPool as cursor:
            valores = (doctor.idDoctor,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    ###Insertar
    # doctor1 = Doctor(nombre="Antonia",apellido= "Rodriguez",especialidad="Odontologia", email="antoniar@doctors.com" )
    # doctoresInsertados = DoctorDAO.insertar(doctor1)
    # log.debug(f"Doctores Agregados: {doctoresInsertados}")
   
    # doctor1 = Doctor(nombre="Jocelyn",apellido= "Rodriguez",especialidad="Oftalmologo", email="jocelynr@doctors.com" )
    # doctoresInsertados = DoctorDAO.insertar(doctor1)
    # log.debug(f"Doctores Agregados: {doctoresInsertados}")

    # # UPDATE
    # doctor1 = Doctor(nombre="Jacqueline",apellido= "Ponce",especialidad="Cardiologia", email="jacqueliner@doctors.com", iddoctor=2)
    # doctoresActualizados = DoctorDAO.actualizar(doctor1)
    # log.debug(f"Doctor Eliminado {doctoresActualizados}")

    # # DELETE
    doctor1 = Doctor(iddoctor = 2)
    doctoresEliminados = DoctorDAO.eliminar(doctor1)
    log.debug(f"Doctor Eliminado {doctoresEliminados}")
    #Leer
    doctores = DoctorDAO.seleccionar()
    for d in doctores:
        log.debug(d)