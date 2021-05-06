import pandas as pd 
import matplotlib.pyplot as plt 
ppgData = pd.read_csv ('ppg.csv', encoding = 'UTF-8', header= 0, delimiter = ';').to_dict ()
muestra = list (ppgData['muestra'].values())
voltaje = list (ppgData['valor'].values())
plt.plot (muestra, voltaje)
plt.title ('Fotopletismografía')
plt.xlabel ('Tiempo en segundos')
plt.ylabel ('Volataje en mV')
plt.savefig ('PPG.png')
plt.show()