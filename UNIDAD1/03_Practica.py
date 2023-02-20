#3 Entrada de datos y manipulación. 
"""
Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de 
manera inversa letra por letra
"""

##ENTRADA DEL NOMBRE COMPLETO
nombre = input("Ingrese su nombre completo:")
invertido = []
letra = len(nombre)

while letra > 0: 
    invertido += nombre[letra-1]
    letra = letra - 1 
print("El nombre invertido es:", invertido) 


##OTRA FORMA
# nombre = input("Ingrese su nombre completo: ")
# nombre_invertido=''.join(reversed(nombre))
# print("El nombre invertido es:", nombre_invertido)

