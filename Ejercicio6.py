# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repe
asignaturas = ['RETE', 'SIPA', 'GPIT', 'SHID', 'SIRC', 'DAPI']
aprobadas = []
for i in asignaturas:
    score = float(input('¿Qué nota has sacado en ' + i + '?'))
    if score >= 5:
        aprobadas.append(i)
for j in aprobadas:
    asignaturas.remove(j)
print('Tienes que repetir ' + str(asignaturas))