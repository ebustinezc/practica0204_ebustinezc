# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
# correspondientes notas introducidas por el usuario.
asignatura = ['RETE', 'SIPA', 'GPIT', 'SHID', 'SIRC', 'DAPI']
nota = []
for i in range(len(asignatura)):
    n = input('Dime la notta de {}: '.format(asignatura[i]))
    nota.append(n)
for i in range(len(asignatura)):
    print('En {} has sacado {}.' .format(asignatura[i], nota[i]))