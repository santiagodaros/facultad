def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as archivo:
        res = archivo.read()
    return res
 
alfabeto = leer_archivo("alfabeto.txt")
 
# 1
 
def obtener_indice(letra,alfabeto):
    aux = 0
    for i in range(len(alfabeto)):
        if letra == alfabeto[i]:
            return aux
        
        else:
            aux +=1
    
 
def codificar_caracter(letra,alfabeto,k):
    if obtener_indice(letra, alfabeto) + k > (len(alfabeto)-1):
        n = (obtener_indice(letra, alfabeto) + k) % (len(alfabeto))
        return alfabeto[n]
    else:
        return alfabeto[obtener_indice(letra, alfabeto) + k]    
        
# 2
 
def normalizacion_cadena(mensaje):
    aux=""
    mensaje = mensaje.lower()
    for char in mensaje:
        if char in ['á','é','í','ó','ú']:
            if char == 'á':
                aux += 'a'
            if char == 'é':
                aux += 'e'
            if char == 'í':
                aux += 'i'
            if char == 'ó':
                aux += 'o'
            if char == 'ú':
                aux += 'u'
        else:
            aux += char
                
    return aux
 
# 3
 
def codificar(mensaje,alfabeto,k):
    mensaje = normalizacion_cadena(mensaje)
    aux = ""
    for char in mensaje:
        if char not in alfabeto:
            aux += char
            
        else:
            aux += codificar_caracter(char, alfabeto, k)
            
    return aux
 
# 4
 
def decodificar_caracter(letra,alfabeto,k):
    if ((obtener_indice(letra, alfabeto))-k) < 0:
        return alfabeto[((obtener_indice(letra, alfabeto))-k) + len(alfabeto)]
    else:
        return alfabeto[((obtener_indice(letra, alfabeto))-k)]
 
# 5
 
def decodificar(mensaje,alfabeto,k):
    aux = ""
    for char in mensaje:
        if char not in alfabeto:
            aux += char
            
        else:
            if ((obtener_indice(char, alfabeto))-k) < 0:
                aux += alfabeto[((obtener_indice(char, alfabeto))-k) + len(alfabeto)]
            else:
                aux += alfabeto[((obtener_indice(char, alfabeto))-k)]
    return aux
 
 
# 6
 
def quitar(elementos,lista):
    res=[]
    for elemento in lista:
        if elemento not in elementos:
            res.append(elemento)
 
    return res
 
# 7
 
def sin_repetidos(cadena):
    cadena=normalizacion_cadena(cadena)
    aux=""
    for char in cadena:
        if char not in aux:
            aux += char
            
    return aux
 
# 8
 
def crear_codificacion(palabra,alfabeto):
    palabra_sin_reps = sin_repetidos(palabra)
    alfabeto_sin_elementos_de_palabra = quitar(palabra_sin_reps, alfabeto)
    lista_nuevo_para_values = list(palabra_sin_reps) + alfabeto_sin_elementos_de_palabra
    res = dict(zip(alfabeto,lista_nuevo_para_values))
    
    return res
    
# 9
 
def codificar_con_dicc(mensaje,diccionario):
    mensaje = normalizacion_cadena(mensaje)
    aux = ""
    for char in mensaje:
        for clave in diccionario.keys():
            if char == clave and char != " ":
                aux += diccionario[clave]
            elif char == " ":
                aux += char
                
    return aux
 
# 10
 
def decodificar_con_dicc(mensaje,diccionario):
    dicc_dec = dict(zip(diccionario.values(),diccionario.keys()))
    res = ""
    for char in mensaje:
        if char in dicc_dec.keys():
            for clave in dicc_dec:
                if char == clave:
                    res += dicc_dec[clave]
        else:
            res += char
            
    return res