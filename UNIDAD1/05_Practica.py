"""
Escribir una función que reciba n parámetros de llave valor e imprima la información en formato 
“{llave}”: “{Valor}”
"""

diccionario={}

def llave_valor(**diccionario):
    for llave, valor in diccionario.items():
        print("{", llave,"}",":","{",valor,"}")

print(" CREANDO MI DICCIONARIO ")
print("CUANDO DESEE PARAR DE INGRESAR VALORES LLAVE-VALOR INGRESE EL CODIGO: 00")
while True:
    llave = input("LLAVE: ")
    valor = input("VALOR: ")

    if llave and valor == "00":
        break

    diccionario[llave] = valor
print("LISTO: ", llave_valor(**diccionario))







