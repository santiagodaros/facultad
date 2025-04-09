from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing
from typing import List, TextIO
"""
def generar_num_al_azar(cantidad:int,desde:int,hasta:int) -> Pila[int]:
    p:Pila=Pila()

    for i in range(cantidad):
        n:int=random.randint(desde,hasta)
        p.put(n)

    return p
"""

# ejercicio 2
def cantidad_elementos(p: Pila) -> int:
    cantidad: int = 0
    pila_clonada: Pila = Pila()
    otra_pila: Pila = Pila()
    
    while not p.empty():
        elem: int = p.get()
        pila_clonada.put(elem)
        otra_pila.put(elem)
    
    while not otra_pila.empty():
        otra_pila.get()
        cantidad += 1
    
    while not pila_clonada.empty():
        p.put(pila_clonada.get())
    
    return cantidad


def cantidad_elementos2(p:Pila)->int:
    cantidad: int = 0
    pila_clonada: Pila = Pila()

    while not(p.empty()):
        elem=p.get()
        pila_clonada.put(elem)

    while not(pila_clonada.empty()):
        pila_clonada.get()
        cantidad +=1

    return cantidad


p=Pila()
p.put(1)
p.put(2)
p.put(3)
#print(cantidad_elementos2(p))

def cantidad_elementos3(p:Pila)->int:
    contenido_pila:[int]=[]
    contador:int=0

    while not(p.empty()):
        contenido_pila.append(p.get())
        contador +=1

    return contador

#p=Pila()
#p.put(1)
#p.put(2)
#p.put(3)
#p.put(5)

#print(cantidad_elementos3(p))

def buscar_el_maximo(p:Pila)->int:
    contenido_pila:[int]=[]

    while not(p.empty()):
        contenido_pila.append(p.get())
        res=maximo_lista(contenido_pila)

    return res

def maximo_lista(lista:list)->int:
    maximo_actual:int=0
    for i in range(len(lista)):
        if lista[i] >= maximo_actual:
            maximo_actual=lista[i]
            i+=1

        else:
            i+=1

    return maximo_actual


#print(maximo_lista([1,2,3,4]))
"""
p=Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(5)
print(buscar_el_maximo(p))
"""

def buscar_nota_maxima(p:Pila)->(str,int):
    contenido_pila:[(str,int)]=[]

    while not(p.empty()):
        contenido_pila.append(p.get())
        res =buscar_nota(contenido_pila)

    return res 


def buscar_nota(lista:list)->(str,int):
    tupla_actual:(str,int)=lista[0]
    maximo= lista[0][1]

    for i in range(1,len(lista)):
        if lista[i][1] > maximo:
            maximo = lista[i][1]
            tupla_actual=lista[i]

    return tupla_actual

p=Pila()
p.put(("A",1))
p.put(("B",2))
p.put(("C",3))
p.put(("D",9))
#print(buscar_nota_maxima(p))



def buscar_el_maximo(c:Cola)->int:
    res:int=0
    while not(c.empty()):
        numero=c.get()
        if numero >= res:
            res=numero

    return res

p=Cola()
p.put(1)
p.put(2)
p.put(4)
p.put(4)
#print(buscar_el_maximo(p))

def buscar_nota_minima(c:Cola)->int:
    res:int=0
    lista_comparar:[int] = []
    while not (c.empty()):
        tupla=c.get()
        lista_comparar.append(tupla[1])
        res=minimo(lista_comparar)

    return res

def minimo(s:list) -> int:
    numero_reciente:int=s[0]
    for i in range(len(s)):
        if s[i] < numero_reciente:
            numero_reciente=s[i]
            i+=1

        else:
            i+=1

    return numero_reciente


p=Cola()
p.put(("s",2))
p.put(("b",2))
p.put(("N",4))
p.put(("J",1))
#print(buscar_nota_minima(p))

def intercalar(c1:Cola, c2:Cola)->Cola:
    res:Cola=Cola()
    while not(c1.empty()) or not(c2.empty()):
        if not c1.empty():
            res.put(c1.get())
        if not c2.empty():
            res.put(c2.get())
    return res

c1=Cola()
c2=Cola()
c1.put(1)
c1.put(3)
c1.put(5)

c2.put(2)
c2.put(4)
c2.put(6)
res = intercalar(c1,c2)
#print(res.get(), end=" ")

def intercalar_colas(cola1: Cola, cola2: Cola) -> Cola:
    cola_intercalada = Cola()
    
    # Mientras haya elementos en al menos una de las colas
    while not cola1.empty() or not cola2.empty():
        # Añadir un elemento de cola1 si no está vacía
        if not cola1.empty():
            elemento1 = cola1.get()
            cola_intercalada.put(elemento1)
        
        # Añadir un elemento de cola2 si no está vacía
        if not cola2.empty():
            elemento2 = cola2.get()
            cola_intercalada.put(elemento2)
    
    return cola_intercalada

cola1 = Cola()
cola2 = Cola()

cola1.put(1)
cola1.put(3)
cola1.put(5)

cola2.put(2)
cola2.put(4)
cola2.put(6)

# Intercalar las colas
cola_intercalada = intercalar_colas(cola1, cola2)

# Mostrar los elementos de la cola intercalada
#while not cola_intercalada.empty():
    #print(cola_intercalada.get(), end=" ")



def n_pacientes_urg(c:Cola)->int:
    contador_urg:int=0
    while not c.empty():
        tripla=c.get()
        if (tripla[0] == 1) or (tripla[0] == 2) or (tripla[0] == 3):
            contador_urg+=1

    return contador_urg


p=Cola()
p.put((2,"s","b"))
p.put((1,"s","b"))
p.put((3,"s","b"))
p.put((7,"s","b"))
p.put((8,"s","b"))
p.put((9,"s","b"))
p.put((1,"s","b"))
#print(n_pacientes_urg(p))
"""
def obtener_palabra(texto:str)->list:
    palabras: list[str] = []
    palabra_actual: str = ''
    for c in texto:
        if c == ' ' or c == '\n':
            if palabra_actual != '':
                palabras.append(palabra_actual)
                palabra_actual = ''
        else:
            palabra_actual += c
    if palabra_actual != '':
        palabras.append(palabra_actual)
    return palabras

#print(obtener_palabra("hola que tal"))

def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    archivo: TextIO = open(nombre_archivo, 'r')
    palabras: List[str] = obtener_palabra(archivo.read())
    archivo.close()
    agrupadas: dict[int,int] = {}

    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in agrupadas:
            agrupadas[longitud] = 1
        else:
            agrupadas[longitud] += 1
    return agrupadas
"""
def promedio_tuplas(notas:list,alumno:str)-> float:
    lista_notas_alumno_x:[float] = []
    for tupla in notas:
        if tupla[0] == alumno:
            lista_notas_alumno_x.append(tupla[1])
        if not(lista_notas_alumno_x == []):
            return suma_total(lista_notas_alumno_x)/len(lista_notas_alumno_x)

        

def suma_total (s:list) -> float:
    res:float=0.0
    for i in range(len(s)) :
        res += s[i]
    return res


def calcular_promedio_por_estudiante(notas:list)->dict:
    res:dict={}  # notas: [(String,Int)] -> {String:Float}
    for tupla in notas:
        res[tupla[0]] = (promedio_tuplas(notas,tupla[0]))
    return res

#print(calcular_promedio_por_estudiante([("a",10.0),("b",2.0)]))


#print(promedio_tuplas([("a",2),("a",3),("b",6)],"a"))

def obtener_palabra(texto:str)->list:
    palabras: list[str] = []
    palabra_actual: str = ''
    for c in texto:
        if c == ' ' or c == '\n':
            if palabra_actual != '':
                palabras.append(palabra_actual)
                palabra_actual = ''
        else:
            palabra_actual += c
    if palabra_actual != '':
        palabras.append(palabra_actual)
    return palabras
#print(obtener_palabra("hola que tal"))

def contar_apariciones(lista:list,palabra:str)->int:
    res:int=0
    for i in range(len(lista)):
        if lista[i] == palabra:
            res +=1

    return res

#print(contar_apariciones(["a","a","a","b"],"a"))

def diccionario_obtener_palabra(frases:list)->dict:
    res:dict={}
    for i in range(len(frases)):
        res[frases[i]] = contar_apariciones(frases,frases[i])

    return res

#print(diccionario_obtener_palabra(["hola","que","tal","que"]))

def comparar_dicc(diccionario:dict)->str:
    clave_max = None
    valor_max=0
    for clave,valor in diccionario.items():
        if valor >= valor_max :
            valor_max = valor
            clave_max = clave

    return clave_max



def la_palabra_mas_frecuente(archivo_texto:str) -> str:
    archivo: TextIO = open(archivo_texto, 'r')
    palabras: List[str] = obtener_palabra(archivo.read())
    archivo.close()
    return comparar_dicc(diccionario_obtener_palabra(palabras))

print(la_palabra_mas_frecuente("C:/Users/santi/OneDrive/Escritorio/xd/python/archivo.txt"))


   
