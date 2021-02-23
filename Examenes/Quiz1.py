
#----Entradas----- 
MENSAJE_BIENVENIDA = "En el dia de hoy verificaremos el estado en el que estan tus niveles de trigliceridos y de homocisteina"
MENSAJE_DESPEDIDA = "Cuidate, tu salud es lo mas importante"
PREGUNTA_TRIGLICERIDOS = "Ingrese el valor de sus trigliceridos :"

MENSAJE_OPTIMO = "tus niveles de trigliceridos son optimos"
MENSAJE_SOBRE_LIMITE_OPTIMO = "tus niveles de trigliceridos sobrepasan el limite optimo"
MENSAJE_ALTO = "tus niveles de trigliceridos son altos"
MENSAJE_MUY_ALTO = "tus niveles de trigliceridos son muy altos"

PREGUNTA_HOMOCISTEINA = "Ingrese el valor de su homocisteina :"
MENSAJE_OPTIMO1 = "tus niveles de homocisteina son optimos"
MENSAJE_SOBRE_LIMITE_OPTIMO1 = "tus niveles de homocisteina sobrepasan el limite optimo"
MENSAJE_ALTO1 = "tus niveles de homocisteina son altos"
MENSAJE_MUY_ALTO1 = "tus niveles de homocisteina son muy altos"


#------Codigo------
print (MENSAJE_BIENVENIDA)
numeroTrigliceridos = float (input(PREGUNTA_TRIGLICERIDOS))
isOptimo = numeroTrigliceridos < 150
isSobreElLimiteOptimo = numeroTrigliceridos > 150  and numeroTrigliceridos <= 199
isAlto = numeroTrigliceridos >= 200 and numeroTrigliceridos <= 499 
isMuyAlto = numeroTrigliceridos >= 500

if(isOptimo):
    print (MENSAJE_OPTIMO)
elif (isSobreElLimiteOptimo):
    print (MENSAJE_SOBRE_LIMITE_OPTIMO)
elif (isAlto):
    print (MENSAJE_ALTO)
else:
    print (MENSAJE_MUY_ALTO)


numeroHomocisteina = float(input(PREGUNTA_HOMOCISTEINA))
isOptimo1 = numeroHomocisteina >= 2 and numeroHomocisteina < 15 
isSobreElLimiteOptimo1 = numeroHomocisteina >= 15 and numeroHomocisteina < 30 
isAlto1 = numeroHomocisteina >= 30 and numeroHomocisteina < 100
isMuyAlto1 = numeroHomocisteina >= 100

if (isOptimo1):
    print (MENSAJE_OPTIMO1)
elif (isSobreElLimiteOptimo1):
    print (MENSAJE_SOBRE_LIMITE_OPTIMO1)
elif (isAlto1):
    print (MENSAJE_ALTO1)
else:
    print (MENSAJE_MUY_ALTO1)

print (MENSAJE_DESPEDIDA)