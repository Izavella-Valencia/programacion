import matplotlib.pyplot as plt 
pielabels = ['Medellin', 'Bogota', 'Bucaramanga', 'Cali', 'Monteria']
sizes = [382, 1775, 162, 564, 3141]
pieExplode = [0, 0 , 0, 0, 0.1]
plt.pie (sizes, labels=pielabels, explode= pieExplode, shadow = True, startangle =45)
plt.title ('Superficie de algunas ciudades de Colombia, dadas inicialmente en km²')
plt.savefig ('Ciudades.png')
plt.show ()