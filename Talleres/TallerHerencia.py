#punto1

class Persona ():
    def __init__ (self, IDpersona, nombre, edad):
        self.idpersona = IDpersona
        self.nombrepersona = nombre
        self.edadpersona = edad 
    def mostraratributos (self):
        print (f'''Mi ID es {self.idpersona}, mi nombre es {self.nombrepersona}, mi edad es {self.edadpersona} años''')
persona1 = Persona (1003046943, "Izavella Valencia", 18)
persona1.mostraratributos()

print ("#"*15)
class Caminar ():
    def __init__ (self, pasos):
        self.pasosdados = pasos 
    def mostraratributos1 (self):
        print (f'Los pasos que usted ha dado segun el conteo es de {self.pasosdados}')
pasospersona = Caminar (1839919)
pasospersona.mostraratributos1()

print ("#"*15)

#punto2
class Doctor (Caminar):
    def __init__ (self, especialidad, enfermedadpersona):
        self.doctorespecialidad = especialidad 
    def mostraratributos2 (self):
        print (f'Los medicos especializados para tratar las enfermedades que se mencionaran son {self.doctorespecialidad}')
    def enfermedad (self):
        enferm = input ('''Ingrese la enfermedad de la cual desea recibir información
        Cancer = C
        Diabetes = D
        Calculos = CA
        ''')
        if (enferm == 'C'):
            print ('El tratamiento adecuado para tratar el cancer es a traves de la quimioterapia')
        elif (enferm == 'D'):
            print ('El tratamiento para esta enfermedad es a traves de la inyección de insulina')
        elif (enferm == 'DA'):
            print ('El tratamiento para esta enfermedad es el suministro de medicamentos')
        else:
            print ('Ingrese una opcion valida')
doctores = Doctor ('Oncologo para el cancer, Endocrinologo para la diabetes, Urologo para los calculos', 'quimioterapia')
doctores.mostraratributos2()
doctores.enfermedad() 

print ("#"*15)

#PUNTO3
class Nutricionista (Persona):
    def __init__ (self, universidad):
        self.universidadEgresado = universidad
    def mostraratributos3 (self):
        print (f'La universidad en la que usted se graduo como nutricionista es en la {self.universidadEgresado}')
    def IMC (self):
        peso = float (input('INGRESE SU PESO :'))
        estatura = float (input('INGRESE SU ESTATURA :'))
        IMC = peso/(estatura**2)
        print (IMC)
nutri = Nutricionista ('Universidad Ces')
nutri.mostraratributos3()
nutri.IMC()

print ("#"*15)
#punto 4
class Abogado (Persona):
    def __init__ (self, especialidad, Universidad):
        self.especialidadAbo = especialidad
        self.universidadAbo = Universidad
    def mostraratributos4 (self):
        print (f'La universidad de la cual usted se graduo como abogado es en la {self.universidadAbo} y su grado de especializacion actualmente es de {self.especialidadAbo}')
aboga = Abogado ('Derecho penal', 'Universidad CES')
aboga.mostraratributos4()

