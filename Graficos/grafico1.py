import matplotlib.pyplot as plt
lenguajes = ['py', 'java', 'dart', 'ts', 'elixir']
resultado = [50, 10, 20, 10, 10]
plt.bar (lenguajes, resultado, width = 0.6, color = 'y')
######Titulo#########
plt.title ('Lenguajes mas usados')
#######ejes 
plt.xlabel ('Lenguajes de programacion')
plt.ylabel ('% de uso de lenguajes de programacion')
plt.savefig ('graficos de lenguaje.png')
################3
plt.show()