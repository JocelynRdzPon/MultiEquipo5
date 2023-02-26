#1 Funciones con n parámetros 
"""
Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el 
producto total.
"""
print("SUMATORIA DE NUMEROS \n!!SI DESEA TERMINAR LA CAPTURA INGRESE EL CODIGO: 00 !!")
numeros = []
#Funcion que sumara los valores almacenados en la lista
def suma(*numeros):
        total = 0
        for num in numeros:
            total = total + num
        return total
##Llenado de la lista

while True:
    numero = float (input("Ingrese el numero: "))

    numeros.append(numero)
    if numero == 0:
        break
    ##Se hace la llamada a la funcion
print("TOTAL:",suma(*numeros))