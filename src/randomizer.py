import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import random

# Definir los parámetros de la distribución normal truncada
a, b = (0 - 40000) / 20000, (79999 - 40000) / 20000  # Límite inferior y superior estandarizados
media = 40000  # loc
desviacion_estandar = 20000  # scale

# Generar la distribución normal truncada
trunc_normal_gen = truncnorm(a, b, loc=media, scale=desviacion_estandar)

# Generar arreglo de números aleatorios
sorted = []
cnt=0
while(cnt<80000):
    sorted.append(cnt)
    cnt+=1
random.shuffle( sorted )

# Generar números de azar

def indiceAleatorio():
    indice_aleatorio = int(trunc_normal_gen.rvs())
    return indice_aleatorio

def generarRandom():
    indice_aleatorio = int(trunc_normal_gen.rvs())
    valor = sorted[indice_aleatorio]
    return valor

#Funciones de graficas a partir de aquí

def graficaNormalIndices():
    x, y = generarDatosGraficaNormal()
    # Crear la gráfica
    plt.bar(x, y)

    # Añadir título y etiquetas
    plt.title('Distribución de frecuencias de índices aleatorios.')
    plt.xlabel('Índices del arreglo aleatorio.')
    plt.ylabel('Número de veces seleccionado.')

    # Mostrar la gráfica
    plt.show()

def generarDatosGraficaNormal():
    x = []
    y = []
    cnt=0

    while(cnt<80000):
        x.append(cnt)
        y.append(0)
        cnt+=1
    
    cnt = 0
    while(cnt<200000):
        indice_aleatorio = int(trunc_normal_gen.rvs())
        y[indice_aleatorio] += 1
        cnt+=1

    return x, y

def graficaDatos():
    x, y = generarDatosGrafica()
    # Crear la gráfica
    plt.bar(x, y)

    # Añadir título y etiquetas
    plt.title('Distribución de frecuencias de números aleatorios.')
    plt.xlabel('Número aleatorio.')
    plt.ylabel('Número de veces seleccionado.')

    # Mostrar la gráfica
    plt.show()

def generarDatosGrafica():
    x = []
    y = []
    cnt=0
    while(cnt<80000):
        x.append(cnt)
        y.append(0)
        cnt+=1

    cnt = 0
    while(cnt<200000):
        indice_aleatorio = int(trunc_normal_gen.rvs())
        valor = sorted[indice_aleatorio]
        y[valor] += 1
        cnt+=1

    return x, y