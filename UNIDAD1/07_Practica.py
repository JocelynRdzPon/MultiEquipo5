"""
#7 Formateo y conversiones 
Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
YYYY/MM/DD” la segunda “2.- Imprimir  MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
del día de hoy en el formato seleccionado.
"""
from datetime import date

print("FORMATO FECHA. SELECCIONA EL FORMATO DE FECHA A SU SELECCION.    \n       OPCIONES     \n 1.- Imprimir YYYY/MM/DD \n 2.- Imprimir MM/DD/YYYY \n")

opcion = int (input("Ingrese la opcion a realizar: "))

opcion1 = date.today().strftime('%Y/%m/%d')
opcion2 = date.today().strftime('%m/%d/%Y')
if opcion == 1:
    print("\nFECHA: ", opcion1, "\n")
elif opcion == 2:
    print("\nFECHA: ",opcion2, "\n")
