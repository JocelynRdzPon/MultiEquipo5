"""Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture 
las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato 
“{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre
"""

print("CALCULADORA DE CREDITOS ")
print("!! Para TERMINAR el registro de asignaturas y creditos INGRESE el codigo 00  !! ")

reticula = {}
total = 0

while True:

    asignatura = input("INGRESE EL NOMBRE DE LA MATERIA: ")
    creditos = int (input("INGRESE LOS CREDITOS: "))

    if asignatura and creditos == 00:
        break
    reticula[asignatura] = creditos  
print("LISTO")


for asignatura, creditos in reticula.items():
    print(asignatura,  " tiene " , creditos, " creditos" )
    total += creditos
print("TOTAL DE CREDITOS: " , total)




    


    
    












