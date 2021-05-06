import matplotlib.pyplot as plt
tiempo = [1,2,3,4,5,6]
sensor = [4,5,6,8,9,10]
plt.plot (tiempo,sensor,'-' ,'y')


plt.title ('Grarico del sensor contra el timepo')
plt.xlabel ('Tiempo en (s)')
plt.ylabel ('Voltaje (mV)')
plt.savefig('sensor')
plt.show ()

#################

