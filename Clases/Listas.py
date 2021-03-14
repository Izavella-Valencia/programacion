nombres = []
print (type(nombres))
print (nombres)
nombres = ['Santiago', 'Samuel', 'Alejandra', 'Elsa']
print (nombres)
print (nombres[2])
nombres.append ('Mauricio')
print (nombres) 
print (nombres [2])
edades = [18,19,20,17]
estaturas = [1.62, 1.80, 1.67, 1.98]

#el ultimo numero 
print (edades [-2])
print (edades [0:2])
print (edades[:3])
print (edades [2:])
print (edades [:])

#para ordenarlas 
edades.sort ()  #menor-mayor 
print (edades)
edades.sort (reverse=True) #mayor-menor 
print (edades)

#mayor y menor de la lista 
mayor = max (edades)
print = (mayor)
menor  = min (edades)
print = menor 

#numero de elemtos 
largosListasEdades = len (edades)
print (largoListasEdades)

#Suma 
sumaEdades = sum (edades)
print (sumaEdades)

#promedio 
promedioEdades = sumaEdades/largosListasEdades
print (promedioEdades)

#eliminar un elemento de la lista 
edades.pop(2) #solo es poner la posicion de la lista
print (edades)

#ciclo for y las listas 
largosListasEdades = len (edades)
for indice in range (largosListasEdades):
    print ('Estoy en la posicion',
    indice, 'valgo',
    edades [indice])
largoListaNombres = len (nombres)
for indice in range (largoListaNombres):
    print (nombres [indice])

posicionesConValorPar = []
largoListaEdades = len (edades)
for posicion in range (largoListaEdades):
    if (edades [ppsicion]%2 == 0):
        posicionesConValorPar.append (posicion)

print (edades)
print (posicionesConValorPar)

#Solo cuando me interese mostrar la lista 
for edad in edades:
    print (edad)
for nombre in nombres: 
    print (nombre)
    print (posicion)
    posicion+=1

posicion = 0
posicionesPares = []
for edad in edades:
    if (edad %2 ==0):
        posicionesPares.appende (posicion)
    posicion +=1
print (posicionesPares)
