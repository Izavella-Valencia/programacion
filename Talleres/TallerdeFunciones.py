#-------Punto 1------------
def mostrarlista (lista= []):
    for elemento in lista1:
        print (elemento)
lista1 = [1,2,3,4,5,6,7,8,9,15,20,25,30,35,40,45]
mostrarlista (lista1)

print ("#"*15)

#-------Punto 2------------
def valoreslista (lista = []):
    valormayor = max (lista)
    valormenor = min (lista)
    largolista = len (lista)
    sumalista = sum (lista)
    promedio  = (sumalista) / (largolista)

    print ('El valor mayor de la lista es',valormayor)
    print ('El valor menor de la lista es',valormenor)
    print ('El promedio de la lista es',promedio)
valoreslista(lista1)

print ("#"*15)

#---------Punto 3-----------
def saludorepetitivo (n=1):
    print ('Buenos días, espero se encuentre muy bien, y que su día este lleno de exitos...'* n)
n = int (input ('¿Cuantas veces desea recibir el saludo? :'))
saludorepetitivo (n)

print ("#"*15)

#---------Punto 4-----------
def posicionesPares (lista= []):
    numeropar = []
    for elemento in lista:
        if (elemento %2 == 0):
            numeropar.append(elemento)
    return numeropar
lista1 = [1,2,3,4,5,6,7,8,9,15,20,25,30,35,40,45]
print ('Los números pares dentro de la lista son',posicionesPares(lista1))

print ("#"*15)

#-----------Punto 5------------
def numeromayores (lista= []):
    numeromayor = []
    for elemento in lista:
        if (elemento > 24):
            numeromayor.append(elemento)
    return numeromayor
lista1 = [1,2,3,4,5,6,7,8,9,15,20,25,30,35,40,45]
print ('Los números mayores que 24 dentro de la lista son', numeromayores(lista1))

print ("#"*15)

#-----------Punto 6-----------
preguntapeso = '¿cual es su peso? :'
preguntaaltura = '¿cual es su altura? :'
peso = float(input(preguntapeso))
altura = float(input(preguntaaltura)) 
def IMC (altura = 1, peso =0):
    Operación = (peso) / (altura**2)
    return Operación
print (IMC (peso, altura))

print ("#"*15)

#----------Punto 7--------------
def despedir ():
    print ('Que tenga un feliz día, vuelva pronto')
    return despedir 
despedir()
