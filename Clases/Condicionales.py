#------constantes-------
MENSAJE_BIENVENIDA = "Hola, espero que estes bien"
NUMERO_A = "ingrese un numero A :"
NUMERO_B = "ingrese un numero B :"
MENSAJE_MAYOR = "el numero A es mayor que B"
MENSAJE_MENOR = "el numero A es menor que B"
MENSAJE_IGUAL = "A y B son iguales "

#-----entrada del codigo----
print (MENSAJE_BIENVENIDA)
numeroA = int (input (NUMERO_A))
numeroB = int (input (NUMERO_B))
isMayorNumero = numeroA > numeroB
isMenorNumero = numeroA < numeroB

if (isMayorNumero):
    print (MENSAJE_MAYOR)
elif (isMenorNumero):
    print (MENSAJE_MENOR)
else:
    print (MENSAJE_IGUAL)


if(isMayorNumero):
    resultado = MENSAJE_MAYOR
elif (isMenorNumero):
    resultado= MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print (resultado)