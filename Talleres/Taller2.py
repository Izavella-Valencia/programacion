#------preguntas------
MENSAJE_INTRODUCCION = "procederemos a hacer operaciones con numeros escogidos por ti"
NUMERO_A = "escoja un numero entero del 1 al 20 :"
NUMERO_B = "escoja un numero entero del 1 al 20 :"


#-------codigos--------
print ("#"*15, "insertar numeros", 15*"#")
print (MENSAJE_INTRODUCCION)
numeroA = int(input(NUMERO_A))
numeroB = int(input(NUMERO_B))


#----comparaciones entre los números------
print ("#"*15, "comparacion entre los numeros", 15*"#")
isMayorNumero = numeroA > numeroB
print (isMayorNumero)
isMenorNumero = numeroA < numeroB
print (isMenorNumero)
isDiferenteNumero = numeroA != numeroB 
print (isDiferenteNumero)
isIgualNumero = numeroA == numeroB
print (isIgualNumero)


#------operaciones entre números----- 
print ("#"*15, "operaciones entre los numeros", 15*"#")
sumar = numeroA + numeroB
print (f"la suma entre los dos numeros dio {sumar} exitosamente")
restar = numeroA - numeroB
print (f"la resta entre los dos numeros dio {restar} exitosamente")
multiplicar = numeroA * numeroB
print (f"la multiplicacion entre los dos numeros dio {multiplicar} exitosamente")
dividir = numeroA / numeroB
print (f"la division entre estos numeros dio {dividir} exitosamente")
exponente = numeroA**numeroB
print (f"la potenciacion tiene un resultado de {exponente}")
