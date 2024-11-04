# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = list(input("Dime una palabra:"))
b = palabra[::-1]
if palabra == b:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")