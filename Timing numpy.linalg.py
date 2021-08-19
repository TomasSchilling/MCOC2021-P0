import scipy as sp
import  sys as sys
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

from numpy.linalg import inv as inv_np
from scipy.linalg import inv as inv_sp


def matriz_laplaciana(n,d):
    return 2*np.eye(n,dtype=d) -np.eye(n,k=1,dtype=d) -np.eye(n,k=-1,dtype=d)

valores=[5,10,20,50,100,200,500,1000,2000,3000,5000]


# ##################### Este valor de i se cambia para los 4 datos ##########################
dicc={0:np.half, 1:np.single,2:np.double, 3:np.longdouble}
i=2


try:
    Tiempos=[]
    Memorias=[]
    for a in valores:
        A= matriz_laplaciana(a,dicc[i])
        t0 = perf_counter()    
        C= inv_np(A)
        t1 = perf_counter()    
        Memorias.append(sys.getsizeof(C)/(1024*1024))
        Tiempos.append(t1-t0)

except:
    print(f"TypeError se presenta un error que no permite leer bien arrays_float16 en linalg :{TypeError} ")
    pass






plt.figure()
plt.subplot(2, 1, 1)    
plt.plot(valores,Tiempos,'-.',label=str(dicc[i]))
plt.legend()
plt.title(f'Rendimiento  INV A usando Estilo {dicc[i]} codigo inv_np')
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



plt.plot(valores,Memorias,'-.',label=str(dicc[i]))

plt.legend()
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