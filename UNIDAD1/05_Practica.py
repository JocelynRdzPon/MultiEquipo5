"""
Escribir una función que reciba n parámetros de llave valor e imprima la información en formato 
“{llave}”: “{Valor}”
"""
llave = ""
valor = ""
diccionario={}

def llave_valor(llave,valor):
  
    diccionario[llave]=valor
    print(diccionario)


while True:
    llave = input("LLAVE: ")
    valor = input("VALOR: ")

    if llave and valor == "00":
        break

    llave_valor(llave,valor)     
print()









