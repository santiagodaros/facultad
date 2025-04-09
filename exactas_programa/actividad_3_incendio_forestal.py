import random
import numpy as np
import matplotlib.pyplot as plt


def generar_bosque(n): 
    lista = np.zeros(n) # hice un array con n ceros osea longitud prefijada por parametro de entrada
    return lista

def cuantos(bosque,tipo_celda):
    res=0
    for elem in bosque:
        if elem == tipo_celda:
            res += 1

    return res

def suceso_aleatorio(p):
    numero = random.randint(0,100) # este numero lo que hace es dependiendo cual sale es a que respuesta va a ir dependiendo de p
    if numero <= p:
        return True
    
    else:
        return False

def brotes(bosque,p):
    if p == 0:
        return bosque
    for i in range(len(bosque)):
        hay_arbol = suceso_aleatorio(p)
        if hay_arbol == True:
            bosque[i] = 1

        else:
            bosque[i] = 0 

    return bosque

def rayos(bosque,f):
    for i in range(len(bosque)):
        suceso = suceso_aleatorio(f)
        if suceso == True:
            bosque[i] = -1

    return bosque

def propagacion(bosque):
    for i in range(len(bosque)-1):
        if bosque[i] == -1:
            if bosque[i-1] == 1:
                bosque[i-1] == -1
            if bosque[i+1] == 1:
                bosque[i+1] = -1
    return bosque

def limpieza(bosque):
    for i in range(len(bosque)):
        elem = bosque[i]
        if elem == -1:
            bosque[i] = 0
    return bosque

def dinamica(n,a,p,f):
    aux=[]
    while a > 0:
        bosque = generar_bosque(n)
        brotar = brotes(bosque,p)
        caen_rayos = rayos(brotar,f)
        propagacion1 = propagacion(caen_rayos)
        limpieza_quemados = limpieza(propagacion1)
        aux2=0
        for elem in limpieza_quemados:
            if elem == 1:
                aux2 += 1
        aux.append(aux2)
        a -= 1

    return (sum(aux)/len(aux))

def arboles_sobrevivientes(f,a,n):
    aux = []
    aux2 = []
    while len(aux) < 101:
        p = random.randint(0,100)
        if p not in aux2:
            aux.append(dinamica(n,a,p,f))
            aux2.append(p)
    return (aux,aux2)

