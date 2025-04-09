import random
 
# 1)
 
def completar_album(figus_total):
    res = [0]*figus_total
    contador = 0
    while (sum(res)) < figus_total:
        figu = random.randint(0,figus_total-1)
        res[figu] = 1
        contador = contador + 1
    
    return contador
    
# 2) 
 
def cuantas_figus(figus_total,n_albumes):
    aux=[]
    contador=0
    if n_album == 0:
        return []
    while contador < n_albumes:
        aux.append(completar_album(figus_total))
        contador += 1
    return aux
 
# 3) 
 
def promedio_figus(figus,n_alb):
    lista = cuantas_figus(figus,n_alb)
    if lista == []:
        return 0.0
    promedio = (sum(lista))/(len(lista))
    return promedio
 
# 4) 
 
def chance_llenar_album(resultados_album_lleno, cantidad_maxima):
    res=0
    i=0
    while i < len(resultados_album_lleno):
        if resultados_album_lleno[i]<= cantidad_maxima:
            res += 1
        i +=1
    return res
    
# 5)    
def llenar_y_devolver_chance(figus_total_album,cantidad_maxima,n_albumes):
    lista_figus = cuantas_figus(figus_total_album,n_albumes) 
    res=0
    i=0
    while i < len(lista_figus):
        if lista_figus[i] <= cantidad_maxima:
            res+=1
        i+=1
    return res
 
 