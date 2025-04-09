import numpy as np
import matplotlib.pyplot as plt
import random
# 1
 
def crear_recipiente(n_filas,m_columnas):
    lista = np.zeros((n_filas,m_columnas), np.int16)
    for j in range(m_columnas):
        lista[(0,j)] = -1
        lista[(n_filas-1,j)] = -1
    for i in range(n_filas):
        lista[(i,0)] = -1
        lista[(i,m_columnas-1)] = -1
    return(lista)
# 2
 
def visualizar_recipiente(recipiente):
    plt.figure()
    cmap = plt.cm.Blues # inicializar mapa de colores azules
    cmap.set_under("black") # darle color negro a las posiciones con valor menor a vmin
    plt.imshow(recipiente, cmap=cmap, vmin=0) # graficar el heatmap usando vmin = 0
    plt.colorbar() # graficar la barra de escala de colores
    plt.show() # terminar de graficar y mostrar la figura
 
# 3
def agregar_particulas(recipiente,posicion,cantidad):
    
    if recipiente[posicion] != -1:
        recipiente[posicion] += cantidad
    return recipiente
 
# 4
def es_borde(recipiente,posicion):
    if recipiente[posicion] == -1:
        return True
    else:
        return False
    
# 5
def vecinos(recipiente,posicion):
    res=[]
    if recipiente[posicion] != -1:
        if recipiente[(posicion[0]+1,posicion[1])] != -1:
            res.append((posicion[0]+1,posicion[1]))
            
        if recipiente[(posicion[0]-1,posicion[1])] != -1:
            res.append((posicion[0]-1,posicion[1]))
        
        if recipiente[(posicion[0],posicion[1]+1)] != -1:
            res.append((posicion[0],posicion[1]+1))
            
        if recipiente[(posicion[0],posicion[1]-1)] != -1:
            res.append((posicion[0],posicion[1]-1))
    
    return res
 
# 6
def elegir_al_azar(lista):
    posicion_al_azar=random.randint(0,len(lista)-1)
    return lista[posicion_al_azar]
 
 
def mover_particula(recipiente,posicion):
    recipiente[posicion] -=1 
    vecino = elegir_al_azar(vecinos(recipiente,posicion))
    recipiente[vecino] += 1
    return recipiente
 
# 7
def mover_muchas_particulas(recipiente,posicion,cantidad):
    while cantidad > 0:
        mover_particula(recipiente,posicion)
        cantidad -= 1
        
    return recipiente