class Torta ():
    def __init__ (self, altura):
        self.alturaTorta = '10'
    def formaTorta (self):
        self.form = input (''' Escoja para determinar la forma de su torta
        forma1 = circular 
        forma2 = cuadrada 
        forma3 = triangular 
        forma4 = rectangular 
        : ''')
        if (self.form == 'forma1'):
            print ('Su torta tendra una forma circular')
        elif (self.form == 'forma2'):
            print ('Su torta tendra una forma cuadrada')
        elif (self.form == 'forma3'):
            print ('Su torta tendra una forma triangular')
        else:
            print ('Su torta tendra una forma rectangular')
    def sabortorta (self):
        self.sabor = input ('''Escoja el sabor de tu torta
        sabor1 = chocolate 
        sabor2 = arequipe
        sabor3 = fresa
        sabor4 = vainilla 
        : ''')
        if (self.sabor == 'sabor1'):
            print ('Su torta tendra un sabor de chocolate')
        elif (self.sabor == 'sabor2'):
            print ('Su torta tendra un sabor de arequipe')
        elif (self.sabor == 'sabor3'):
            print ('Su torta tendra un sabor de fresa')
        else:
            print ('Su torta tendra un sabor de vainilla')
    def medidaalturatorta (self):
        print ('La altura con la cual trabaja esta maquina para la torta es de', (self.alturaTorta))
tortas = Torta ('10')
tortas.formaTorta()
tortas.sabortorta ()
tortas.medidaalturatorta ()

print ("#"*15)
#punto2
class Estudiante ():
    def __init__ (self, edad, nombre, ID, carrera, semestre):
        self.edadEstudiante = edad
        self.nombreEstudiante = nombre 
        self.idestudiante = ID
        self.carreraEstudiante = carrera
        self.semestreEstudiante = semestre
    def mostraratributos (self, materia, tiempo):
        print (f'''El estudiante tiene {self.edadEstudiante}, su nombre es {self.nombreEstudiante}, su numero de ID es de {self.idestudiante}
        La carrera en la que esta el estudiante es {self.carreraEstudiante}, y el semestre que cursa es el {self.semestreEstudiante}''')
estudi = Estudiante(18, 'Izavella Valencia', 1003046943, 'Ingenieria Biomedica', 3)
estudi.mostraratributos('Morfofisiologia', '1 año')

print ("#"*15)
#punto 3
class Nutricionista ():
    def __init__ (self, nombre, edad, universidad):
        self.nombrenutri = nombre
        self.edadnutri = edad 
        self.universidadnutri = universidad 
    def mostraratributos1 (self):
        print (f'''El nombre de la nutricionista es {self.nombrenutri}
        La edad de la nutricionista es de {self.edadnutri}
        La edad de la cual es egresada la nutricionista es de la {self.universidadnutri}
        ''')
    def IMC (self):      
        peso = float (input('INGRESE SU PESO :'))
        estatura = float (input('INGRESE SU ESTATURA :'))
        IMC = peso/(estatura**2)
        print (IMC)
nutri = Nutricionista('Ana Lucia Doria', 30, 'Universidad CES')
nutri.mostraratributos1()
nutri.IMC()

print ("#"*15)
#punto4
class Canguro ():
    def __init__ (self, nombre, idcan, edad):
        self.nombrecanguro = nombre 
        self.idcanguro = idcan
        self.edadcanguro = edad
    def mostraratributos2 (self):
        print (f'''El nombre del canguro es {self.nombrecanguro}
        El ID del canguro es {self.idcanguro}
        La edad del canguro es de {self.edadcanguro} años
        ''')
    def saltoscanguros (self):
        numerodesaltos = int (input ('ingrese el numero de saltos que desea que de el canguro'))
        while (numerodesaltos != 5):
            if (numerodesaltos ==1):
                print ('El canguro ha dado 1 salto ')
            elif (numerodesaltos == 2):
                print ('El camguro ha dado 2 saltos')
            elif (numerodesaltos == 3):
                print ('El canguro ha dado 3 saltos')
            elif (numerodesaltos == 4):
                print ('El canguro ha dado 4 saltos')
            elif (numerodesaltos == 5):
                print ('El canguro ha dado 5 saltos')
            else:
                print ('Ingrese una opcion valida')
            numerodesaltos = int (input ('ingrese el numero de saltos que desea que de el canguro'))
saltos = Canguro ('Cafe', 34556, 8)
saltos.mostraratributos2()
saltos.saltoscanguros()

print ("#"*15)
#punto 5
class InstrumentoFav ():
    def __init__ (self, tipo, tamaño, Clasificacion):
        self.tipoinstru = tipo 
        self.tamañoinstru = tamaño 
        self.clasificacioninstru = Clasificacion
    def mostraratributos3 (self):
        print (f'''Mi instrumento favorito es el piano, es de tipo {self.tipoinstru}
        Su tamaño es de {self.tamañoinstru}
        Este es un piano {self.clasificacioninstru}
        ''')
instrumento = InstrumentoFav('percusion', 2.50 , 'de Cola')
instrumento.mostraratributos3()

