import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
import  sys as sys  # Para obtener la memoria del objeto https://www.analyticslane.com/2018/11/19/reducir-el-consumo-de-memoria-en-python/


Tiempos=[[],[],[],[],[],[],[],[],[],[],[],[]]
Memoria=[]
valores=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,1000,2000,5000,10000]
for i in range(len(valores)):
    serie=[]
    n=valores[i]
    A= np.random.rand(n,n)
    B= np.random.rand(n,n)
    for a in range (len(Tiempos)):
        
        t0 = perf_counter()    
        C= A@B
        t1 = perf_counter()    
        Tiempos[a].append(t1-t0)
    Mem= sys.getsizeof(A)/(1024*1024)+sys.getsizeof(B)/(1024*1024)+sys.getsizeof(C)/(1024*1024)
    Memoria.append(Mem)  

archivo= open("resultados.txt","w")
archivo.write("Tiempo por serie                , memoria utilizada \n")

for i in range(len(valores)): 
    for a in range (len(Tiempos)):
        archivo.write(str(Tiempos[a][i])+ "  ")
    archivo.write(",  "+str(Memoria[i])+" \n ")
archivo.close()



plt.figure()
plt.subplot(2, 1, 1)    
for i in range (len(Tiempos)):
    plt.plot(valores,Tiempos[i],'-.')
    
plt.title('Rendimiento  A*B')
plt.grid()
plt.ylabel("Tiempo transcurrido (seg.)")
plt.yscale('log')
plt.xscale('log')



valores_x=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.0001,0.001,0.01,0.1,1,10,60,600]
yTicks_Text = ['0.1ms','1ms','10ms','0.1s','1s','10s','1min','10min']
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text)   


plt.subplot(2, 1, 2)

plt.plot(valores,Memoria)
plt.grid()
plt.ylabel("Memoria utilizada")
plt.xlabel("Tamaño matriz N")
plt.yscale('log')
plt.xscale('log')

xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.001,0.01,0.1,1,10,100,1000,10000]
yTicks_Text = ['1KB','10KB','100KB','1MB','10MB','100MB','1GB','10GB']

plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text) 

plt.show()    