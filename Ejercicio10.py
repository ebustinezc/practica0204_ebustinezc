# Escribir un programa que almacene en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios = [50, 75, 46, 22, 80, 65, 8]
m = mx = precios[0]
for x in range(len(precios)):
    if precios[x] > mx:
        mx = precios[x]
    if precios[x] < m:
        m = precios[x]
print("El precio mayor es {} y el menor es {}".format(mx, m))