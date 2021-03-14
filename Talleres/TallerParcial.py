#------Entradas------
PREGUNTA_NUMERO = '''
    1- Mostrar la conversión 
    2- Mostrar el tipo de ingreso al cual pertence
    3- Clasificacion de los valores en el tipo de ingreso
    4- Salir 
'''
PREGUNTA_MONEDA = '''
    C- Mostrar en pesos colombianos 
    D- Mostrar en Dolares 
    E- Mostrar en Euros
'''
preguntarIngresos = 'Ingrese el valor de sus ingresos :'
pregunta_moneda = 'Ingrese un valor en dolares'

#----------Mensajes--------
MensajeDolares = 'Mostrar lista en dolares'
MensajePesos = 'Mostrar lista en Pesos '
MensajeEuros = 'Mostrar lista en Euros'
MensajeIngresosBajos = 'El valor pertenece a un ingreso bajo'
MensajeIngresosMedios = 'El valor pertenece a un ingreso medio'
MensajeIngresosAltos  = 'El valor pertenece a un ingreso alto'
MensajeIngresosElevados = 'El valor pertenece a un ingreso elevado'
MensajeDespedida = 'Hemos terminado, ¡¡feliz día!!'
MensajeError = 'Ingrese una opcion valida '


#------Conversion punto 1---------
listaDolares = [20000, 30000, 2500, 1000, 7600]
ListaPesos = []
for elemento in listaDolares:
    conversorPesos = round (elemento * 3700,)
    ListaPesos.append(conversorPesos)
ListaEuros = []
for elemento in listaDolares:
    conversorEuros = round (elemento * 0.84,)
    ListaEuros.append(conversorEuros)

OpcionEscogida = int (input(PREGUNTA_NUMERO))
while (OpcionEscogida != 4):
    if (OpcionEscogida == 1):
        OpcionMoneda = input (PREGUNTA_MONEDA)
        if (OpcionMoneda == 'C' ):
            print (MensajePesos)
            print (ListaPesos)
        elif (OpcionMoneda == 'D' ):
            print (MensajeDolares)
            print (listaDolares)
        elif (OpcionMoneda == 'E' ):
            print (MensajeEuros)
            print (ListaEuros)
        else: 
            print (MensajeError)
    elif (OpcionEscogida == 2):
        Ingresos = int(input(preguntarIngresos))
        if (Ingresos < 1000):
            print (MensajeIngresosBajos)
        elif (Ingresos > 1000 and Ingresos < 7000):
            print (MensajeIngresosMedios)
        elif (Ingresos >= 7000 and Ingresos < 20000):
            print (MensajeIngresosAltos)
        else:
            print (MensajeIngresosElevados)
    elif (OpcionEscogida == 3):
        print ('el ingreso mayor es :', max (listaDolares))
        print ('el ingreso menor es :', min (listaDolares))
        print ('el promedio de los ingresos es :', sum (listaDolares)/len (listaDolares))
    else:
        print ('La opción ingresada no es válida, por favor verifique que este entre las opciones')
    OpcionEscogida = int(input(PREGUNTA_NUMERO))
print (MensajeDespedida)