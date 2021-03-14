#-------mensajes------
SALUDAR = "Bienvenid, te ayudare ahorrando"
PREGUNTA_VALOR_CPU= "Cuanto vale el PC que deseas :"
PREGUNTA_CUANTO_TIENE = "Cuanto llevas ahorrado :"
MENSAJE_AHORRO = 'Llevas ahorrado...'
#----codigo -------
print (SALUDAR)
valor = float (input(PREGUNTA_VALOR_CPU))
ahorrado = float(input(PREGUNTA_CUANTO_TIENE))

while (valor > ahorrado): 
    print (MENSAJE_AHORRO, ahorrado, 'te faltan...', valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)