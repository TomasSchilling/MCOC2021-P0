# MCOC2021-P0

# Mi computador principal

* Marca/modelo: Dell inspiron 7559
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel® Core™ i5-6300HQ
  * Velocidad Base: 2.3GHz (6M Cache ).
  * Velocidad Máxima: up to 3.20GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 4
  * Arquitectura: x86_64
  * Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
* Tamaño de las cachés del procesador
  * L1d: 256 kB
  * L2: 1.0 MB
  * L3: 6.0 MB
* Memoria 
  * Total: 8GB 1 DIMM (1x8GB) 
  * Tipo memoria: DDR3L
  * Velocidad 1600 Mhz
  * Numero de (SO)DIMM: 1
  * Form Factor: SODIMM.
* Tarjeta Gráfica
  * Marca / Modelo: NVIDIA GeForce 960M
  * Memoria dedicada: 4 GB GDDR5 a 5 GHz
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Marca: SanDisk Modelo: Z400s M.2 2280.
  * Tipo: SSD M2  (5400rpm) sin particion .
  * Tamaño: 256 GB
  * Particiones: 1
  * Sistema de archivos: 
* Disco 2: 
  * Marca: WDC (china) Modelo : Wd5000BPVT.
  * Tipo: HDD SATA (5400rpm) sin particion.
  * Tamaño: 512 GB
  * Particiones: 1
  * Sistema de archivos: 

  
* Dirección MAC de la tarjeta wifi: 
* Dirección IP (Interna, del router): 192.168.1.235
* Dirección IP (Externa, del ISP): 
* Proveedor internet: GTD Mnaquehue, Fibra Optica



# Resultados Matmul
<https://github.com/TomasSchilling/MCOC2021-P0/blob/main/Graficos%20trabajo%20matmul.png>
* El grafico del profesor y del alumno difieren mas que nada en la fluctuacion del los valores couendo se trabaja con matrices de tamano mediano, es decir n= 100, 200.
La memoria sigue en bosquejo simlar, mas que nada varia en la primera seccion del , pero luego sigue la linea de menara equitativa.
* as diferencias en cada corrida puede deberse al mayor o menor uso de el pprocesador para procesos cortos, donde este puede verse afectado por realizar otras tareas dependientes del mismo computador, como tambien a la apertira de otro procesador para el calculo de la matriz.
* el grafico de tiempos no es linearl debido a que el tiemp ode prosesamiento no es continuo, varia dpendiendo de lo mencionado anteriormente, sim embargo, para guardar informacion se necesita el mismo especio para guardar un dato en un pc, si es del mismo tipo de archivo (float 32, float 64, etc)
* Se usa la version python 3.8.5 en spyder version 4.1.5
* numpy version: 1.19.2
* se llegaron a utilizar todos los procesadores, el screenshort es el siguiente
