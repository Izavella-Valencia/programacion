pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
#se ponen los datos a trabajar 
edad = 18
estatura = 1.60
peso = 60 
NOMBRE = "Izavella Valencia Padilla"
#verificar si la edad cumple con ser mayor de edad o no 
isMayorEdad = edad >= 18 
print (isMayorEdad)
#la estatura esta en el promedio?
print ("#"*15, "Bajo la estura promedio", "#"*15)
isMayorEstatura = estatura < 1.70 
print (isMayorEstatura)
print ("#"*15, "Peso diferente 60", "#"*15)
isPesoDiferente = peso != 60 
print (isPesoDiferente)
# vamos a ver si el apellido esta o no en el nombre 
apellido = "Valencia"
isApellido = apellido in NOMBRE 
print ("#"*15, "apellido en el NOMBRE", "#"*15)
print (isApellido)