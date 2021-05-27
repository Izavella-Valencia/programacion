#Punto 1
alimentoFavorito = []
print ('Ingrese sus 8 alimentos favoritos')
for i in range(8):
    elemento = input ('Ingrese: ')
    alimentoFavorito.append (elemento)

preciosAlimento = []
print ('''Ingrese los precios 
        de cada uno de los alimentos en el mismo
        orden que puso la primera lista''')
for i in range (8):
    elemento = input ('Ingrese: ')
    preciosAlimento.append (elemento)

import matplotlib.pyplot as plt
plt.bar (alimentoFavorito, preciosAlimento, width = 0.6, color = 'y')
plt.title ('Alimentos favoritos')
plt.xlabel ('nombre de los alimentos')
plt.ylabel ('Precio de los alimentos')
plt.savefig('GraficoAlimentos.png')
plt.show ()

#Punto2
class Humano ():
    def __init__ (self, nombre, sexo ,edad):
        self.nombreHumano = nombre 
        self.sexoHumano = sexo 
        self.edadHumano = edad 
    def mostrar (self, parrafo): 
        print (f'''Hola {self.nombreHumano}, espero te encuentres muy bien. 
        Tu sexo es {self.sexoHumano} y tu edad es {self.edadHumano} años.
        {parrafo}
        ''')
class Doctor (Humano):
    def IMC (self):
        peso = float (input('INGRESE SU PESO :'))
        estatura = float (input('INGRESE SU ESTATURA :'))
        IMC = peso/(estatura**2)
        print (IMC)
humano1 = Humano ('Izavella', 'Femenino', 18)
humano1.mostrar ('Ten un lindo día')
doctorHumano = Doctor ('Izavella Valencia', 'Femenino', 18)
doctorHumano.IMC ()

#punto 3
isCorrectData = False 
while (isCorrectData == False):
    try:
        nombre = str (input ('Ingrese su nombre, por favor: '))
        assert (nombre.isalpha())
        isCorrectData = True
    except AssertionError:
        print ('Los datos que ha ingresado son incorrectos, vuelva a ingresarlos')

isCorrectData = False
while (isCorrectData == False):
    try:
        Valor = float (input ('Ingrese su dinero en dolares: '))
        isCorrectData = True
    except ValueError:
        print ('Dato incorrecto, ingrese de nuevamente su dinero en dolares') 


Euros = Valor * (0.82)
print (f'''Hola {nombre}, espero que te encuentres muy bien en el dia de hoy
    tienes {Valor} dolares y su conversion 
    a Euros equivaldria a {Euros} euros''')


#Punto 4

import sys 
nombreArchivo = 'Pacientes.txt'
try: 
    archivoPacientes = open (nombreArchivo)
    print ('El archivo funciono correctamente')
except FileNotFoundError:
    archivoPacientes = open (nombreArchivo, 'w', encoding='UTF-8')
    print ('''El archivo no fue encontrado, por lo tanto no se guardo
    verifique que las entradas esten correctas''')
    sys.exit(1)

archivoPacientes = open (nombreArchivo, 'a')
nombrePaciente = (input ('Ingrese el nombre del paciente: '))
descripciónEnfermedad = (input ('Describa la enfermedad que tiene el paciente'))
precioConsulta = float (input ('Ingrese el precio que pago en la consulta'))
linea = '\nNombre: ' + nombrePaciente + 'descripcion: ' + descripciónEnfermedad + 'precio: ' str(precioConsulta)
archivoPacientes.writelines (linea)
archivoPacientes.close ()