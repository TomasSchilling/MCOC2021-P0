  
# la misma pero la subo yo ( eso entendi) 
from numpy import zeros
from time import perf_counter



#Tamaño
N = 1000
A = zeros((N, N))+1
B = zeros((N, N))+2


t1 = perf_counter()
C = A@B
t2 = perf_counter()


dt = t2 - t1

print(f"dt = {dt} s")

# dt = 0.09375370000088878 s