import array
from typing import List
from queue import Queue as Cola

def pertenece (s:list,e:int)->bool:
    res:bool
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False


#print(pertenece([1,2,3,4,5,6], 2))

def divide_a_todos (s:list,e:int) -> bool:
    indice_actual:int=0
    longitud_lista:int=len(s)
    
    while (indice_actual < longitud_lista):
        if s[indice_actual] % e == 0:
            indice_actual+=1

        else:
            return False
        
    return True

"""
    while (indice_actual<longitud_lista):
        if s[indice_actual] % e != 0:
            return False    
        else:
            indice_actual += 1
    return True

"""

#print(divide_a_todos([2,4,6,8],2))

def suma_total (s:list) -> int:
    res:int=0
    for i in range(len(s)) :
        res += s[i]
        i+=1
    return res

#print(suma_total([1,2,3,0,0,0,1]))

def maximo(s:list) -> int:
    numero_reciente:int=0
    for i in range(len(s)):
        if s[i] >= numero_reciente:
            numero_reciente = s[i]
            i +=1
        
        else:
            i+=1

    return numero_reciente

#print(maximo([9,2,3,4,5]))

def minimo(s:list) -> int:
    numero_reciente:int=s[0]
    for i in range(len(s)):
        if s[i] < numero_reciente:
            numero_reciente=s[i]
            i+=1

        else:
            i+=1

    return numero_reciente

#print(minimo([7,2,3,4]))

def ordenados(s:list)-> bool:
    for i in range(0,len(s)-1):
        if (not(s[i]<s[i+1])):
            return False
        
    return True


#print(ordenados([1,2,3,4,9,7]))

def pos_maximo(s:[int])->int:
    if len(s)==0:
        return -1
    
    numero_actual:int=0
    posicion_actual:int=0
    for i in range(len(s)):
        if s[i] >=numero_actual:
            posicion_actual=i
            numero_actual = s[i]
            i+=1

        else:
            i+=1
    
    return posicion_actual


#print(pos_maximo([]))


def chequeo_longitud(lista:[str])-> bool:
    for palabra in lista:
        if (len(palabra)>7):
            return True
            
    return False
            
        
#print(chequeo_longitud(["Jirafa","Leonidass"]))

def invertir_string(s:[str]):
    res:[str] = []
    for i in range(len(s)-1,-1,-1):
        res.append(s[i])
        i +=1

    return res

#print(invertir_string(["n","e","u","q","u","e","n"]))

def es_palindromo(s:[str])->bool:
    if s == []:
        return True
    
    for i in s:
        if s == (invertir_string(s)):
            return True
        
    return False

#print(es_palindromo([]))

def subseq_mas_larga(s:[int])->int:
    max_long=1
    max_inicio=0
    longitud_ac=1
    inicio_actual=0

    for i in range(1,len(s)):
        if s[i] > s[i-1] :
            longitud_ac +=1
        
        else:
            if longitud_ac > max_long:
                max_long = longitud_ac
                max_inicio = inicio_actual

            longitud_ac = 1
            inicio_actual = i

    if longitud_ac > max_long:
        max_long = longitud_ac
        max_inicio = inicio_actual

    return max_inicio


#print(subseq_mas_larga([1,2,3,4,2,3,4,5,6,7]))

def sumar_Todos(s:[int]) -> int:
    res:int=0
    for i in range(0,len(s)):
        res += s[i]

    return res

#print(sumar_Todos([1,2,3,4,5]))

def pertenece2(s:[chr],e:chr) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


#print(pertenece2(["h","o","l","a"],'e'))

def eliminar_repetidos(s:[chr]) -> [chr]:
    res:[chr]=[]
    for i in range(len(s)):
        if not(pertenece2(res,s[i])):
            res.append(s[i])

    return res

#print(eliminar_repetidos(["a","b","c","a"]))

def resultadoMateria(notas:[int])->int:
    for i in range(len(notas)):
        if notas[i] >= 4 and (promedio(notas)) >= 7:
            return 1
        elif notas[i] >= 4 and (promedio(notas)) >= 4 and (promedio(notas)) < 7:
            return 2 
        elif menos_a_cuatro(notas) or (promedio(notas)) < 4:
            return 3
        


def promedio(s:[int])->int:
    for i in range(len(s)):
        return ((sumar_Todos(s))/(len(s)))

#print(promedio([1,2,3]))

def menos_a_cuatro(s:[int]) -> bool:
    for i in range(len(s)):
        if s[i] < 4:
            return True
        
        return False

#print(menos_a_cuatro([1,2,3]))

#print(resultadoMateria([4,5,6,7,8]))

# MATRICES

def pertenece_a_cada_uno_version_1(s:[[int]],e:int)->[bool]:
    res:[bool] = []
    for i in range(len(s)):
        if pertenece(s[i],e):
            res.append(True)
    
    return res


#print(pertenece_a_cada_uno_version_1([[1,2,3],[2,2,1],[2,7,8]],3))

def es_matriz(s:[[int]])->bool:
    if s == [[]] or s[0] == []:
        return False
    
    for i in range(len(s)):
        if (s[0] == s[i]):
            return True
        
    return False
        

#print(es_matriz([[1,2,3],[]]))

def filas_ordenadas(s:[[int]])->[bool]:
    res:[bool] = []
    for i in range(len(s)):
        if (ordenados(s[i]))==True:
            res.append(True)

        else:
            res.append(False)

    return res

#print(filas_ordenadas([[1,6,3],[4,5,6]]))

def columna(m:[[int]],e:int) -> [int]:
    res:[int]=[]
    for i in m:
        res.append(i[e-1])
    return res

#print(columna([[1,2,3],[4,5,6],[7,8,9]],2))

def columnas(m:[[int]])->[[int]]:
    res:[[int]] = []
    num_columnas=len(m[0])
    for i in range(1,num_columnas+1):
        res.append(columna(m,i))

    return res


#print(columnas([[1,2,3],[4,5,6],[7,8,9]]))

def numeros_impares(s:list)->int:
    contador:int=0
    for i in range(len(s)):
        numeros=s[i]
        while numeros > 0:
            digito = numeros % 10
            if digito % 2 != 0:
                contador +=1
            numeros //= 10

    return contador

#print(numeros_impares([57,2383,812,246]))

