import matplotlib.pyplot as plt 
#creamos los labels, sizes y explode 
pielabels = ['Clase 1', 'Clase 2', 'Clase 3', 'Clase 4', 'Clase 5', 'Clase 6']
#Los tamaños de cada porcion de la torta
sizes = [25, 23, 29, 24, 27, 26]

#explode = Que tan alejado del origen esta la torta
pieExplode = [0, 0 , 0, 0.1, 0, 0]
plt.pie (sizes, labels=pielabels, explode= pieExplode, shadow = True, startangle =45)
plt.title ('Asistencia a las clases de programacion')
plt.savefig ('AsistenciaClases.png')

plt.show ()