PREGUNTA_PESO = "cuanto pesas :"
PREGUNTA_ESTATURA = "cuanto mides en metros :"
MENSAJE_BIENVENIDA = "hola como estas, calcularemos tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es"

#----entrada de codigos 
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
print (MENSAJE_DESPEDIDA, IMC)
print (MENSAJE_DESPEDIDA, IMC)
isObeso = IMC >= 30
print ("el resultado de la prueba obesidad es ...", isObeso)