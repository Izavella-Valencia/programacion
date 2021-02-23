#----------condicionales------ 
MENSAJE_BIENVENIDA = "Hola ¿como estas? en el dia de hoy vamos a calcular tu IMC"
PREGUNTA_PESO = "¿cuanto pesas en Kg?"
PREGUNTA_ESTATURA = "¿cuanto mides en metros?"
MENSAJE_BAJO_PESO = "Estas muy delgado"
MENSAJE_PESO_NORMAL = "Estas en forma"
MENSAJE_SOBRE_PESO = "Ten cuidado, tienes sobre peso"
MENSAJE_OBESO = "Cuidado, tu salud corre riesgo"
MENSAJE_DESPEDIDA = "Tu IMC es"

#-----Entrada de codigo-------
print (MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
isBajoPeso = IMC < 18.5 
isPesoNormal = IMC >=18.5 and IMC < 25
isSobrePeso = IMC >=25 and IMC < 30 
isObeso = IMC >= 30 
Resultado = ""
if(isBajoPeso):
    Resultado = MENSAJE_BAJO_PESO
if(isPesoNormal):
    Resultado = MENSAJE_PESO_NORMAL
if(isSobrePeso):
    Resultado = MENSAJE_SOBRE_PESO
if(isObeso):
    Resultado = MENSAJE_OBESO

print (MENSAJE_DESPEDIDA, IMC)
print (Resultado)