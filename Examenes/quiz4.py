#punto 1
snackfavorito = []
print ('Ingrese sus 5 nacks favoritos')
for i in range(5):
    elemento = input ('Ingrese: ')
    snackfavorito.append (elemento)

preciosnack = []
print ('''Ingrese los precios 
        de cada snack en el mismo
        orden que puso la primera lista''')
for i in range (5):
    elemento = input ('Ingrese: ')
    preciosnack.append (elemento)

import matplotlib.pyplot as plt
plt.bar (snackfavorito, preciosnack, width = 0.6, color = 'y')
plt.title ('Snacks favoritos')
plt.xlabel ('nombre de los snacks')
plt.ylabel ('Precio de los snacks')
plt.savefig('GraficoSnacks.png')
plt.show ()
#punto 2
ciudades = []
print ('Ingrese sus 5 ciudades')
for i in range(5):
    elemento = input ('Ingrese: ')
    ciudades.append (elemento)
poblaciones = []
print ('''Ingrese la poblacion
        de cada una de las ciudades escogidas''')
for i in range (5):
    elemento = input ('Ingrese: ')
    poblaciones.append (elemento)

import matplotlib.pyplot as plt 
pielabels = ciudades
sizes = poblaciones 
pieExplode = [0,0,0,0,0]
plt.pie (sizes, labels = pielabels, explode = pieExplode, shadow = True, startangle = 45)
plt.title ('Ciudades y sus poblaciones')
plt.savefig('GraficoCiudades.png')
plt.show()
#punto3
print ('''(PPG) es una técnica óptica simple usada para descubrir cambios volumétricos en sangre en la circulación periférica.
Es un bajo costo y un método no invasor que hace mediciones en la superficie de la piel.
La técnica ofrece relacionado con la información valioso a nuestro sistema cardiovascular
''')
import pandas as pd 
import matplotlib.pyplot as plt 
ppgData = pd.read_csv ('ppg1.csv', encoding = 'UTF-8', header= 0, delimiter = ';').to_dict ()
muestra = list (ppgData['muestra'].values())
voltaje = list (ppgData['valor'].values())
plt.plot (muestra, voltaje)
plt.title ('Fotopletismografía')
plt.xlabel ('Tiempo en segundos')
plt.ylabel ('Volataje en mV')
plt.savefig ('PPG(1).png')
plt.show()

print ('''Un electrocardiograma (ECG) es un procedimiento 
simple e indoloro que mide la actividad eléctrica del corazón.
Cada vez que el corazón late, una señal eléctrica circula a través de él.
Un electrocardiograma muestra si su corazón está latiendo a un ritmo y con una fuerza normal.''')

import pandas as pd 
import matplotlib.pyplot as plt 
ecgData = pd.read_csv ('ecg1.csv', encoding = 'UTF-8', header= 0, delimiter = ';').to_dict ()
muestra = list (ecgData['muestra'].values())
voltaje = list (ecgData['valor'].values())
plt.plot (muestra, voltaje)
plt.title ('electrocardiograma')
plt.xlabel ('Tiempo en segundos')
plt.ylabel ('Volataje en mV')
plt.savefig ('ECG1.png')
plt.show()