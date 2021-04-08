#-----------Punto 1----------
a= float(input('Ingrese un número :'))
b= float(input('Ingrese un número :'))
c= float(input('Ingrese un número :'))

def operaciones (a, b, c):
    suma = a+b+c
    resta = a-b-c
    multiplica = a*b*c
    divide = a/b/c
    potencia = a**b**c

    print ('La suma es ',suma)
    print ('La resta es',resta)
    print ('La multiplicacion es ',multiplica)
    print ('La division es ',divide)
    print ('La potencia es ', potencia)

operaciones (a,b,c)
print ("#"*15)

#-------------Punto 2------------
lista1= [1,2,3,4,5,6,7,8,9]
lista2 = [5,10,15,20,25,30,35,40,35]
lista3 = [3,6,9,12,15,18,21,24,27]
def todaslaslistas (listaA, listaB, listaC):
    if len (listaA) == len (listaB) == len (listaC):
        print (listaA, listaB, listaC)
todaslaslistas(lista1,lista1,lista3)

print ("#"*15)

#-------------Punto 3-----------------
print ('Vamos a calcular el area de un triangulo, para eso necesitamos que nos ayudes con las medidas de su base y altura')
base = float (input ('Ingrese la medida de la base del triangulo :'))
altura = float (input ('Ingrese la medida de la altura del triangulo :'))
def areatriangulo (altura=0, base=0):
    operacion = (base*altura) / 2
    return operacion
print ('El area del triangulo es',areatriangulo (base, altura))

print ("#"*15)

#------------Punto 4----------------
lista4 = [2,4,6,8,10,12,14,16,16,18,20]
print ('La lista es ',lista4)
def clasificacionenlista (listaEntrada2 = []):
    mayorvalor = max (listaEntrada2)
    menorvalor = min (listaEntrada2)
    sumalista = sum (listaEntrada2)
    largolista = len (listaEntrada2)
    promedio = (sumalista) / (largolista)

    print ('El valor mayor de la lista es', mayorvalor)
    print ('El valor menor de la lista es', menorvalor)
    print ('El promedio de la lista es', promedio)
clasificacionenlista (lista4)

print ("#"*15)

#------------Punto 5-------------------
def sucesion (n):
    a = 0 
    b = 1
    for elemento in range (n-1):
        c = a + b
        a = b
        b = c
    return (b)

n = int (input ('Ingrese la posicion que desea saber :'))
lugar = sucesion (n)
print (lugar)

