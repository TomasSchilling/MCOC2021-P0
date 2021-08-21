import numpy as np
import scipy as sp
import  sys as sys
from time import perf_counter
import matplotlib.pyplot as plt

from scipy.linalg import solve as sp_solve
from scipy.linalg import eigh as sp_eigh

def matriz_laplaciana(n,d):
    return 2*np.eye(n,dtype=d) -np.eye(n,k=1,dtype=d) -np.eye(n,k=-1,dtype=d)

def graficar(valores,Tiempos ,titulo,leyenda):
    plt.figure()
    for i in range(len(Tiempos)):
        plt.plot(valores,Tiempos[i],'-.',label=f"n* {i}")
    plt.legend()
    plt.title(f'Rendimiento  {titulo}')
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
    
    plt.savefig(f"Rendimiento {titulo} ")
    plt.show()
    plt.close()
    


dicc={0:np.float,1:np.double}
valores=[5,10,20,50,100,200,500,1000,2000]
opcion_1={0:'gen' ,1:'pos' ,2:'sym' ,3:'gen', 4:'gen',5:'gen'}  # asuumir a
opcion_2={0:False ,1:False ,2:False ,3:True, 4:False,5:True}    # overwrite a
opcion_3={0:False ,1:False ,2:False ,3:False, 4:True,5:True}    # overwrite b

opcion_4={0: None ,1:"ev" ,2:"evd" ,3:"evr", 4:"evx"}    #  driver
          
Grafo_promedio_solve=[ ]
Grafo_promedio_eigh=[ ]

Ciclo=[False,True]
for floa in range(2):
    for i in range(6):
        
        Tiempos=[[],[],[],[],[],[],[],[],[],[]]
        for cuenta in range(10):
                
            for a in valores:
                A= matriz_laplaciana(a,dicc[floa])
                b= np.ones(a)
                t0 = perf_counter()    
                C= sp_solve(A,b,assume_a=opcion_1[i],overwrite_a=opcion_2[i],overwrite_b=opcion_3[i])
                t1 = perf_counter()    
                Tiempos[cuenta].append(t1-t0)
            if floa==0:
                codigo="np_float"
            elif floa ==1:
                codigo="np_double"
        graficar(valores,Tiempos,"Solver Usando " +str(opcion_1[i])+" "+str( opcion_2[i])+" "+str(opcion_3[i])+" "+codigo,i)
        l=[]
        for q in range(len(valores)):
            num=0
            for w in range(len(Tiempos)):
                num+=Tiempos[w][q]
            l.append(num/len(Tiempos))
        Grafo_promedio_solve.append(l)
    graficar(valores,Grafo_promedio_solve, f"resumen graficos solver usando "+ str(floa),floa)
    for i in range(5):
        for tipo in Ciclo:
            Tiempos=[[],[],[],[],[],[],[],[],[],[]]
            for cuenta in range(10):
                for a in valores:
                    A= matriz_laplaciana(a,dicc[floa])
                    t0 = perf_counter()    
                    C= sp_eigh(A,driver=opcion_4[i],overwrite_a=tipo)
                    t1 = perf_counter()    
                    Tiempos[cuenta].append(t1-t0)
                if floa==0:
                    codigo="np_float"
                elif floa ==1:
                    codigo="np_double"
            graficar(valores,Tiempos," Eigh Usando driver=" +str(opcion_4[i]) +f" y overwrite= {tipo} "+codigo,floa)
        l=[]
        for q in range(len(valores)):
            num=0
            for w in range(len(Tiempos)):
                num+=Tiempos[w][q]
            l.append(num/len(Tiempos))
        Grafo_promedio_eigh.append(l)
    graficar(valores,Grafo_promedio_eigh, f"resumen graficos eigh usando "+ str(floa),i)


Comentario=""" Luego de termianr de realizar todas las operaciones y revisar los graficos se comprueba que hay 
diferencias entre el tipo de metodo utillizado para obtener la matriz de solucion a la ecuacion, todas las pendientes
presentan algunos metodos presentan mejores rendimiento en general a lo largo del proceso, se nota bien si que algunos
procesos generen una leve mejora en el tiempo al aumentar mas su tamano de la matriz de resolucion. 
A lo largo del sistema fueron requeridos mas de un procesasor, la memoria Rondo por el 80% de su uso de manera constante
EL metodo mas efectivo puede afectarse del tamano de la matriz, en los graficos resumen se ve esto a medida que se 
agranda el tamano de esta matriz. """
