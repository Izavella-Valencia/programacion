#---------Entradas--------
Temperatura_Corporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.33, 33]
print (Temperatura_Corporal)
Menu = '''
    1- Conversion a Farenheit o Kelvin
    2- Clasificacion de la temperatura
    3- Temperatura maxima, minima, tiempo entre toma de datos
    4- Salir 
'''
PREGUNTA_TEMPERATURA = '''
    F- Temperatura en grados Farenheit 
    K- Temperatura en grados Kelvin 
    C- Temperatura en grados Celsius 
'''
PreguntaTemperatura = 'Ingrese el grado de la temperatura corporal del paciente :'

mensaje_farenheit = 'mostrar temperatura en grados farenheit'
mensaje_kelvin = 'mostrar temperatura en grados kelvin'
mensaje_Celsius = 'la conversion no es necesaria '
mensaje_error = 'Ingrese una opcion valida'
MensajeHipotermia = 'El paciente presenta hipotermia'
MensajeFiebre = 'El paciente presenta fiebre'
MensajeNormal = 'El paciente presenta una temperatura corporal normal'
MensajeDespedida = 'Gracias por utilizar nuestro programa'

#-----Conversion punto 1------
Temperatura_Corporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.33, 33]
ListaFarenheit = []
for elemento in Temperatura_Corporal:
    ConvertidorFarenheit = round ((elemento*1.8) + 32 )
    ListaFarenheit.append (ConvertidorFarenheit)
ListaKelvin = []
for elemento in Temperatura_Corporal:
    ConvertidorKelvin = round (elemento + 273.15)
    ListaKelvin.append (ConvertidorKelvin)

opcionMenu = int (input(Menu))
while (opcionMenu != 4):
    if (opcionMenu == 1):
        Opcion_temperatura = input (PREGUNTA_TEMPERATURA)
        if (Opcion_temperatura == 'F'):
            print (mensaje_farenheit)
            print (ListaFarenheit)
        elif (Opcion_temperatura == 'K'):
            print (mensaje_kelvin)
            print (ListaKelvin)
        elif (Opcion_temperatura == 'C'):
            print (mensaje_Celsius)
            print (Temperatura_Corporal)
        else:
            print (mensaje_error)
    elif (opcionMenu == 2):
        for Temperatura in Temperatura_Corporal:
            if (Temperatura < 36):
                print (MensajeHipotermia, Temperatura)
            elif (Temperatura > 36 and Temperatura <= 37.5):
                print (MensajeNormal, Temperatura)
            else:
                print (MensajeFiebre, Temperatura)
    elif (opcionMenu == 3):
        print ('La temperatura maxima es', max (Temperatura_Corporal))
        print ('La temperatura minima es', min (Temperatura_Corporal))
        TiempoEntreMuestra = 24/len (Temperatura_Corporal)
        print('El tiempo que transcurre entre cada toma de temperatura es de', TiempoEntreMuestra)
    else:
        print ('Ingrese una opcion valida')
    opcionMenu = int (input(Menu))
print (MensajeDespedida)




