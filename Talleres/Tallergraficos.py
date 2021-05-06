#niveles de ingreso de una persona durante el 2020 
import matplotlib.pyplot as plt
ingresos = [300, 450, 420, 200, 540, 210, 360, 410, 520, 600, 390, 550]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
plt.bar (meses, ingresos, width=0.3, color= 'y')
plt.title ('Ingresos de una persona en el 2020')
plt.xlabel ('Meses')
plt.ylabel ('Ingresos de una persona en miles')
plt.savefig ('ingresos.png')
plt.show()

