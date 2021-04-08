guardar = print ('hola')
print (guardar)

guardar = round (14.2534897,2)
print (guardar)

def linedesign (cantidad = 10, simbolo = '#'):
    print (simbolo * cantidad)



#-----------mostrar lista---------
def mostrarLista (listaEntrada = []):
    for elemento in listaEntrada:
        print (elemento)


lista= [213,32,23123,321,321,233,1232,23]
lista2 = [564654,645,64543,2565,547,57865]
linedesign (30, '#')
mostrarLista (lista)
mostrarLista (lista2)

#---------sumar----------
def sumar (a=0, b=0):
    suma = a + b

print(sumar(12,14))
round (12.234897,2)

linedesign (30, '#')
#-------restar---------
def restar (a=0, b=0):
    resta = a - b


linedesign (30, '#')

#----------multiplicar------
def multiplicar (a=0, b=0):
    multiplica= a*b


linedesign (30, '#')

#-------dividir-----------
def dividir (a=0, b=1):
    divide = a/b

linedesign (30, '#')

#---------potenciacion------- 
def potenciacion (a=12, b=13):
    potencia = a**b
