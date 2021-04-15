class AnimalFavorito ():
    def __init__(self, entorno):
        self.tipodeanimal = 'Delfín'
        self.medio = entorno
        self.pesodelanimal = self.peso ()
    def animal (self):
        print ('Tu animal favorito es un', (self.tipodeanimal), ', y son animales muy inteligentes.')
    def peso (self):
        self.especie = input ('''Seleccione el tipo de especie:
        DHE - Delfines Hector 
        DHA - Delfines de Heaviside
        DTA - Delfines tornillo acrobáticos
        DRI - Delfines del río Indo
        DMA - Delfines manchados del Atlántico
        DFB - Delfines de flanco blanco del Pacífico
        DEM - Delfines mulares
        DRG - Delfines de Risso o Grampus
        ''')
        pesoA = ''
        if (self.especie == 'DHE'):
            peso ='El delfin tiene un peso de entre 40 kg y 60 kg'
            print (peso)
        elif (self.especie == 'DHA'):
            peso ='El delfin tiene un peso de entre 60 kg y 70 kg'
            print (peso)
        elif (self.especie == 'DTA'):
            peso ='El delfin tiene un peso de entre 59 kg y 77 kg'
            print (peso)
        elif (self.especie == 'DRI'):
            peso ='el delfin tiene un peso de entre 70 kg o 90 kg'
            print (peso)
        elif (self.especie == 'DMA'):
            peso ='El delfin tiene un peso de entre los 100 kg y los 143 kg'
            print (peso)
        elif (self.especie == 'DFB'):
            peso ='El delfin tiene un peso de entre 135 kg y 180 kg'
            print (peso)
        elif (self.especie == 'DEM'):
            peso ='El delfin tiene un peso de entre 150 kg y 200 kg'
            print (peso)
        else:
            peso ='el delfin tiene un peso de entre 300 kg  y 500 kg.'
            print (peso)
        return peso
    def medioacuatico (self):
        entornoacuatico = input(''' escoja una especie para saber su medio:
        DHE - Delfines Hector 
        DHA - Delfines de Heaviside
        DTA - Delfines tornillo acrobáticos
        DRI - Delfines del río Indo
        DMA - Delfines manchados del Atlántico
        DFB - Delfines de flanco blanco del Pacífico
        DEM - Delfines mulares
        DRG - Delfines de Risso o Grampus
        ''')
        if (entornoacuatico == 'DHE'):
            print ('El delfin se encuentra en los mares')
        elif (entornoacuatico == 'DHA'):
            print ('El delfin se encuentra en las costas de sudafrica')
        elif (entornoacuatico == 'DTA'):
            print ('El delfin se encuentra en los mares')
        elif (entornoacuatico == 'DRI'):
            print ('el delfin se encuentra en algunos rios')
        elif (entornoacuatico == 'DMA'):
            print ('El delfin se encuentra en el oceano atlantico norte')
        elif (entornoacuatico == 'DFB'):
            print ('El delfin se encuentra en el norte del oceano pacifico')
        elif (entornoacuatico == 'DEM'):
            print ('El delfin se encuentra en algunos mares')
        else:
            print ('El delfin se encuentra en algunos mares')


animal = AnimalFavorito ('mar')
animal.animal()
animal.peso()
animal.medioacuatico()



