from math import sqrt, pi


def imprimir_hola_mundo ():
    print("Hola Mundo!")

#imprimir_hola_mundo()
def raiz_de_2() -> str:
    return round(sqrt(2),4)

#print(raiz_de_2())

def factorial () -> int:
    return 2 * 1

def perimetro () -> int:
    return 2 * pi

# 2)
def imprimir_saludo(nombre:str) -> str :
    print("Hola", nombre )

def raiz_cuadrada_de (numero:int) -> int:
    return (round(sqrt(numero)), 2)

def fahrenheit_a_cel (temp_far:int) -> int:
    return ((temp_far - 32) * 5) / 9

def imprimir_dos_veces(estribillo:str) -> str:
    return (estribillo * 2)

#print(imprimir_dos_veces("muevelo lisa rompe la patricia alejandra es fina como monalisa"))

def es_multiplo_de (n: int,m:int) -> bool:
    return (n % m == 0)

def es_par (n:int) -> bool:
    return (es_multiplo_de (n,2) == 0)

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> float:
    return ((min_cant_de_porciones * comensales)/8)

# 3)
def alguno_es_0(x:int, y:int) -> bool:
    resultado:bool = x == 0 or y == 0
    return resultado

def ambos_son_0(x:int, y:int) -> bool:
    resultado1:bool = x == 0 and y == 0
    return resultado1

def  es_nombre_largo (nombre: str) ->bool:
    res:bool = (len(nombre) >= 3) and  (len(nombre) <= 8)
    return res

def es_bisiesto(año:int) -> bool:
    res:bool= (es_multiplo_de (año,400))== True or (es_multiplo_de (año,4)) == True and (es_multiplo_de (año,100)) == False

# 5)

def devolver_el_doble_si_es_par(numero:int) -> int:
    res:int 
    if (es_par (numero)) ==True :
        return (numero *2)
    
    else: 
        return numero
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int :
    res:int
    if  (es_par (numero)) ==True :
        return numero
    else:
        return (numero +1)
    
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    res:int
    if (es_multiplo_de (numero,3)) == True :
        return numero * 2
    
    if (es_multiplo_de (numero,9)) == True :
        return numero * 3
    
#print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (3))

def lindo_nombre(nombre:str) -> str:
    res:str
    if len(nombre) >= 5:
        print("Tu nombre tiene muchas letras!")

    else:
        print("Tu nombre tiene menos de 5 caracteres")

def elRango(numero:int) -> str:
    res:str
    if numero < 5:
        print("Menor a 5")

    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")

    elif numero > 20:
        print("Mayor a 20")


# 6)
def imprimir_1_al_10 ():
    i:int=1
    while i <= 10:
        print(i)
        return imprimir_1_al_10(i+1)

#print(imprimir_1_al_10(1))

def imprimir_pares ():
    i:int=10
    while i <= 40:
        print(i)
        i += 2

#print (imprimir_pares())

def imprimir_eco()->None:
    i:int=0
    while i < 10:
        print("eco")
        i += 1

#print(imprimir_eco())

def cuenta_regresiva (n:int) -> None:
    i:int=n
    while i > 0:
        print(i)
        n += -1
    print("Despegue!")

print(cuenta_regresiva(10))