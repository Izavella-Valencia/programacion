#------Punto 1---------
MENSAJE_DE_BIENVENIDA1 = "Hoy haremos comparaciones entre dos numeros"
NUMEROA = "Inserte un numero entero :"
NUMEROB = "Inserte un numero entero :"

#codigos 
print (MENSAJE_DE_BIENVENIDA1)
numeroA = int(input(NUMEROA))
numeroB = int(input(NUMEROB))

isMayorNumero = numeroA < numeroB
print (isMayorNumero)
isMenorNumero = numeroA > numeroB
print (isMenorNumero)
isIgualNumero = numeroA == numeroB
print (isIgualNumero)


#---------Punto 2----------
print ("#"*15, "punto numero 2", "#"*15)
#Entradas 
MENSAJE_BIENVENIDA2 = "Hola, hoy haremos la clasificacion segun su edad"
PREGUNTA_EDAD = "¿cuantos años tiene? :"
MENSAJE_MENOR_EDAD = "Eres m¿enor de edad"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Ya te estas pasando, eres un adulto"
MENSAJE_ADULTO_MAYOR = "te pasaste, haces parte la la poblacion de aultos mayores"

#codigos
print (MENSAJE_BIENVENIDA2)
edad =  int(input(PREGUNTA_EDAD))
isMenorEdad = edad < 18 
isJoven = edad >= 18 and edad < 26
isAdulto = edad >= 26 and edad < 60 
isAdultoMayor = edad >= 60
resultado = ""
if (isMenorEdad):
    print (MENSAJE_MENOR_EDAD)
elif(isJoven):
    print (MENSAJE_JOVEN)
elif(isAdulto):
    print (MENSAJE_ADULTO)
else:
    print (MENSAJE_ADULTO_MAYOR)


#--------Punto 3---------
print ("#"*15, "punto numero 3", "#"*15)
MENSAJE_ENTRADA = "Hallaremos cuantos años faltan para que suceda el año escogido de manera aleatoria"
MENSAJE_AÑO_ACTUAL = "Inserte el año en el que se encuentra actualmente :"
MENSAJE_AÑO_ALEATORIO = "Inserte el año del cual quiere tener información :"
MENSAJE = "°Si el resultado es un numero negativo significa que ha pasado esa cantidad de tiempo"
MENSAJE2 = "°Si el resultado es un numero positivo significa que hacen falta ese numero de años"

#codigos 
print (MENSAJE_ENTRADA)
añoactual = int(input(MENSAJE_AÑO_ACTUAL))
añoescogido = int(input(MENSAJE_AÑO_ALEATORIO))
tiempo = añoescogido - añoactual
print(f"el tiempo que hay entre el año actual y el deseado es de  {tiempo} años")
print (MENSAJE)
print (MENSAJE2)



#---------Punto 4--------------
print ("#"*15, "punto numero 2", "#"*15)
#entradas
MENSAJE_DE_BIENVENIDA2 = "Hoy escogeremos una medida y la llevaremos a varias unidades de longitud"
PREGUNTA_MEDIDA = "Escoja una medida en cm :"

#codigos 
print (MENSAJE_DE_BIENVENIDA2)
medidaencm = float(input(PREGUNTA_MEDIDA))
medidaenkm = ((1 * medidaencm)/ 100000)
medidaenm = ((1 * medidaencm)/100)
print (f"la medida en cm fue pasada a kilometros dando asi {medidaenkm}km exitosamente")
print (f"la medida en cm fue pasda a metros, dando asi {medidaenm}m exitosamente ")