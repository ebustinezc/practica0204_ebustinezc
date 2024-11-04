# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
abecedario = []
for i in range(len(alfabeto)):
    if (i + 1) % 3 != 0:
        abecedario.append(alfabeto[i])
print(abecedario)