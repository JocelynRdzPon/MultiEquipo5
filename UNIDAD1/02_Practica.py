"""
#2 Manejo y manipulación de elementos de una lista 
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
##ABECEDARIO
abecedario =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
longitud = len(abecedario)
print("ABECEDARIO COMPLETO \n", abecedario, "\n")

for letra  in range(longitud,1,-1):
    if letra % 3 == 0:
        abecedario.pop(letra - 1)
print("ABECEDARIO SIN MULTIPLOS DE 3 \n",abecedario,"\n")