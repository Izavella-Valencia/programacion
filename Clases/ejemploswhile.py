#-------Entradas-------
MENSAJE_BIENVENIDA = 'Muy buenos dias, despierte que esta en clase de 6'
MENSAJE_ERROR = 'Por favor ingresa una opcion valida'
PREGUNTA_MENU = ''' Igrese
    1- Para mostrar los numeros del 1-5
    2- Para preguntar tu nombre 
    3- Para mostrar el año en el que estamos 
'''
PREGUNTA_NOMBRE = 'Ingrese su nombre por favor :'

#----------codigo--------
entrada = 1
while (entrada >= 1 and entrada<= 3):
    entrada = int (input(PREGUNTA_MENU))
    if (entrada == 1):
        print (1,2,3,4,5)
    elif (entrada ==2):
        nombre = input(PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este menú, emplea alguna de las tres opciones')
    elif (entrada ==3):
        print ('estamos en el año 2021')
    elif (entrada == 4):
        print ('muchas gracias por usar el programa, feliz dia')
    else: 
        entrada=1
        print (MENSAJE_ERROR)
