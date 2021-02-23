#-----entradas-----
MENSAJE_BIENVENIDA = "Hola, como estas?"
PREGUNTA_EDAD = "¿cuantos años tienes? :"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad, puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad, no puedes seguir"

#------entrada de codigos------
print (MENSAJE_BIENVENIDA)
edad = int (input(PREGUNTA_EDAD))
isMayorEdad = edad >=18 
if(isMayorEdad):
    print (MENSAJE_MAYOR_EDAD)
else:
    print (MENSAJE_MENOR_EDAD)
