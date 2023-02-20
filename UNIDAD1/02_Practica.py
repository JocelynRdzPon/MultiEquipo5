"""
#2 Manejo y manipulación de elementos de una lista 
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
##ABECEDARIO
abecedario =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listanueva = []
print("ABECEDARIO COMPLETO", abecedario)
# ##########################
for letra  in range(len(abecedario),1,-1):
    if letra % 3 == 0:
        abecedario.pop(letra - 1)
print(abecedario)
#######################

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet)
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)


