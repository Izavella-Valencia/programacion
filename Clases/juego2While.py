import random 
#--------entradas----------
MENSAJE_SALUDAR = '''
    Bienveido 
    a este programa 
    ¡¡¡juguemoooos!!!
'''
MENSAJE_SEGUNDO_NIVEL = 'Felicidades pasaste el primer nivel, ahora ve por el ultimo'
MENSAJE_CALIENTE = 'Estas caliente'
MENSAJE_FRIO = 'Estas frio'
PREGUNTAR_NUMERO = '''
    En este juego debes asertar un numero entero 
    que va desde el 1-10, la idea es que lo puedas intentar varias veces
    antes de que se te acaben las vidas...
    No existe via 0
    Muchos exitos, ingresa tu numero
'''
PREGUNTA_DIFICULTAD = '''
    1- Facil 
    2-Moderado 
    Dificil 
'''
PREGUNTA_FALLIDA = 'Fallaste, ingresa otro numero :'
MENSAJE_GANASTE = 'Felicidades ganaste'
MENSAJE_PERDISTE = 'Perdiste, vuelvelo a intentar'


#-------codigo--------- 
numeroOculto = random.randint(1,10)
numeroOcultoDos = random.randint (1,10)
vidas = None 


dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad != q and dificultad != 2 and diificultad !=3 ):
    print ('ingresa una opcion valida')
    dificultad = int (input(PREGUNTA_DIFICULTAD))


if (dificultad == 1):
    print ('modo facil activado')
    vidas = 10 




