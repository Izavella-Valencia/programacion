#vamos a evaluar dos numeros y las distintas operaciones que se pueden hacer entre ellos 
numeroA = 26
numeroB = 13
#se suman los números 
sumar = numeroA + numeroB
print (f"la suma entre los dos numeros dio {sumar} exitosamente")
#se restan los números 
print ("#"*15, "restar los numeros", "#"*15)
restar = numeroA - numeroB
print (f"la resta entre los dos numeros dio {restar} exitosamente")
#multiplicar los números 
print ("#"*15, "multiplicar los numeros", "#"*15)
multiplicar = numeroA * numeroB
print (f"la multiplicacion entre los dos numeros dio {multiplicar} exitosamente")
#dividir los numeros 
print ("#"*15, "dividir los numeros", "#"*15)
dividir = numeroA / numeroB
print (f"la division entre los dos numeros dio {dividir} exitosamente")
#exponente 
print ("#"*15, "elevar el numero", "#"*15)
exponente = numeroA**numeroB
print (f"el resultado de la potenciacion dio {exponente} exitosamente")
#verificar si el numero A es mayor, igual, o menor que el numero B 
isMayorNumero = numeroA > numeroB
print (isMayorNumero)
isIgualNumero = numeroA != numeroB
print (isIgualNumero)
isMenornumero = numeroA < numeroB
print (isMenornumero)
isMayorNumeroB = numeroB == numeroA
print (isMayorNumeroB)
#comparando números 
print ("#"*15, "comparando números", "#"*15)
numeroA = 26
isMayorNumeroA = numeroA >= 50
print (isMayorNumeroA)
isMenorNumeroB = numeroB < 50
print (isMenorNumeroB)
