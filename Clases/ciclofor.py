for iteracion in range (10):
    print (iteracion)
print ("#"*30)
for iteracion in range (10):
    print (iteracion+1)
print ("#"*30)
for iteracion in range (1,11):
    print (iteracion)
print ("#"*30)
for iteracion in range (1,11,2):
    print (iteracion)
print ("#"*30)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion)
print ("#"*30)
for iteracion in range (1,11):
    if (iteracion % 2 != 0):
        print (iteracion)

print ("#"*30)

for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion, "------> es un numero par" )
    else:
        print (iteracion, "-------> es un numero impar" )

print ("#"*30)
rango = int (input ("ingrese el rango maximo"))
for iteracion in range (1,rango + 1):
    print (iteracion)

opcion = int (input('''
    1- Ver solo impares 
    2- Ver solo pares 
    3- Ver las dos clasificaciones
    n- cualquier numero para mostrar nada 
'''))

print ("#"*30)
if (opcion == 1 ):
    for iteracion in range (1, rango +1):
        if (iteracion % 2 !=0):
            print (iteracion)
elif (opcion == 2):
    for iteracion in range (1, rango + 1):
        if (iteracion % 2 == 0):
            print (iteracion)
elif (opcion != 3):
    for iteracion in range (1, rango + 1):
        if (iteracion % 2 == 0):
            print (iteracion)
else:
    print ('mostrando nada')
