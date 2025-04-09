import numpy as np
import random
# 1
 
tablero = np.repeat(" ",42).reshape((6,7))
#print(crear_tablero)
 
# 2
# hago una funcion para ver que fila esta 
 
def ultima_fila_vacia(columna):
    if tablero[(0,columna)] != " ":
        return -1
    pos_act=0
    for j in range(1,tablero.shape[0]):
        if tablero[(j,columna)]==" ":
            pos_act = j
        else:
            return pos_act
    
    return pos_act
 
 
# 3
 
def poner_ficha(tablero,columna,ficha):
    posicion_fila = ultima_fila_vacia(columna)
    if posicion_fila != -1:
        tablero[(posicion_fila,columna)] = ficha
    return tablero
 
# 4
 
def maquina():
    n = random.randint(0,6)
    while ultima_fila_vacia(n) == -1:
        n = random.randint(0,6)
        
    poner_ficha(tablero,n,"O")
    return tablero
 
# 5
def jugador():
    columna = int(input("Introduzca la columna donde se quiere ejecutar: "))
    if ultima_fila_vacia(columna) == -1:
        nuevamente = int(input("Introduzca otro, esa columna esta llena: "))
    else:
        poner_ficha(tablero, columna, "X")
        
    return tablero
 
# 6
 
def chequeo_4(tablero):
    for i in range(tablero.shape[0]-3):
        for j in range(tablero.shape[1]):
            if tablero[(i,j)] == tablero[(i+1,j)]== tablero[(i+2,j)] == tablero[(i+3,j)] == "O" or tablero[(i+3,j)] == "X":
                return "Gano"
    
    for j in range(tablero.shape[1]-3):
        for i in range(tablero.shape[0]):
            if tablero[(i,j)] == tablero[(i,j+1)]== tablero[(i,j+2)] == tablero[(i,j+3)] == "O" or tablero[(i,j+3)] == "X":
                return "Gano"