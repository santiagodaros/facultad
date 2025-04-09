import random
# 1)
 
def tirar_cubilete():
    res=[]
    while len(res) < 5:
        numero = random.randint(1,6)
        res.append(numero)
    return res
 
# 2)
 
def cuantos_hay(elemento,lista):
    i = 0
    contador = 0
    while i < (len(lista)):
        if lista[i] == elemento:
            contador +=1
        i +=1 
    return contador
 
# 3)
 
def puntos_por_unos(lista_dados):
    res=0
    if cuantos_hay(1,lista_dados) == 1:
        res += 100
    elif cuantos_hay(1,lista_dados) == 2:
        res += 200
    elif cuantos_hay(1,lista_dados) == 3:
        res += 1300
    elif cuantos_hay(1,lista_dados) == 4:
        res += 1500
            
    elif cuantos_hay(1,lista_dados) == 5:
        res += 10500
            
    return res
    
# 4)
 
def puntos_por_cincos(lista_dados):
    res=0
    if cuantos_hay(5,lista_dados) == 1:
        res += 50
    elif cuantos_hay(5,lista_dados) == 2:
        res += 100
    elif cuantos_hay(5,lista_dados) == 3:
        res += 650
    elif cuantos_hay(5,lista_dados) == 4:
        res+= 750
    elif cuantos_hay(5,lista_dados) == 5:
        res += 850
            
    return res
 
# 5)
 
def total_puntos(lista_dados):
    res:int=0
    res = puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados)
    return res
 
# 6)
 
def jugar_ronda(cant_jugadores):
    lista_puntos=[0]*cant_jugadores
    i = 0
    while i < cant_jugadores:
        tirada = tirar_cubilete()
        lista_puntos[i] += total_puntos(tirada)
        i += 1
        
    return lista_puntos
    
# 7)
 
def acumular_puntos(puntajes_acumulados,puntajes_ronda_actual):
    res=[0] * len(puntajes_acumulados)
    i = 0
    while i < len(puntajes_acumulados):
        res[i] = (puntajes_acumulados[i] + puntajes_ronda_actual[i])
        i+=1
        
    return res
 
# 8
 
def hay_10mil(puntajes_acumulados):
    res = False
    i = 0
    while i < len(puntajes_acumulados):
        if puntajes_acumulados[i] >= 10000:
            return True
        i += 1
    return res
 
# 9)
 
def partida_completa(cant_jugadores):
    res:int=0
    acumulados = [0]*cant_jugadores
    while hay_10mil(acumulados) == False:
        res += 1
        ronda = jugar_ronda(cant_jugadores)        
        for i in range(len(acumulados)):
            acumulados[i] += ronda[i]
    return res
 
 