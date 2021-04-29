import matplotlib.pyplot as plt
clases = ['Clase 1', 'Clase 2', 'Clase 3', 'Clase 4', 'Clase 5', 'Clase 6']
numeroEstudiantes = [25, 23, 29, 24, 27, 26]
plt.bar (clases, numeroEstudiantes, width= 0.6, color= 'm')
plt.title ('Asistencia a las clases de programación')
plt.xlabel ('Clases')
plt.ylabel ('Número de estudiantes que asistieron')
plt.savefig ('Grafico de asistencia.png')
plt.show ()
