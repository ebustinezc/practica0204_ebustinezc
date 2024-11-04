# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = list(input("Dime una palabra:"))
a = palabra.count("a")
e = palabra.count("e")
i = palabra.count("i")
o = palabra.count("o")
u = palabra.count("u")
print("Tu palabra tiene {} a, {} e, {} i, {} o, {} u".format(a, e, i, o, u))