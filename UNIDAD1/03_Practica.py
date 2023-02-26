#3 Entrada de datos y manipulación. 
"""
Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de 
manera inversa letra por letra
"""

##DECLARACION
nombre = input("Ingrese su nombre completo:")
invertido = list(nombre)

##PROCEDIMIENTO
invertido.reverse()
print("\nNOMBRE INVERTIDO \n",invertido)

