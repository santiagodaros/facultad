import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("Actividad6-Datos.csv")


# 3                 
#describe = df.describe()
#info = df.info()

# 4

def obtener_alturas():
    alturas = df["Altura"]
    return alturas
  
def promedio_alturas():
    alturas = df["Altura"] != 0
    return alturas.mean()

def minimo_alturas():
    filtro_alturas = df["Altura"] != 0
    return alturas.min()

def max_alturas():
    alturas = df["Altura"] != 0
    return alturas.max()

# 5

#promedio_por_columna = df.mean()

#promedio_de_promedios = promedio_por_columna.mean()

# 6

def estudiante_mas_joven():
    filtro_edad = df["Edad"]
    return filtro_edad.min()

def estudiante_mas_viejo():
    filtro_edad = df["Edad"] 
    return (filtro_edad.max(),)

# 7

def estudiantes_datos():
    filtro_carrera=df["Carrera"] == "Computacion"
    return (filtro_carrera.sum())

def edad_promedio_estudiantes_datos():
    filtro_carrera=df["Carrera"] == "Computacion"
    return df["Edad"].mean()

def cuadro_mayor_promedio():
    # Filtrar las filas donde la carrera sea "Computación"
    filtro_carrera = df["Carrera"] == "Computacion"
    df_computacion = df[filtro_carrera]
    
    # Encontrar la fila con el mayor promedio
    fila_mayor_promedio = df_computacion.loc[df_computacion["Promedio"].idxmax()]
    
    # Devolver el valor de la columna "Cuadro" correspondiente
    return fila_mayor_promedio["Cuadro"]


# 8

def promedio_cada_carrera():
    valores_unicos = df["Carrera"].unique()
    lista_valores=valores_unicos.tolist()
    
    promedios = df.groupby("Carrera")["Promedio"].mean()
    
    carrera_por_mayor = promedios.idxmax()
    mayor_promedio= promedios.max()
    
    carrera_menor_promedio = promedios.idxmin()
    menor_promedio = promedios.min()
    
    return (lista_valores,mayor_promedio,menor_promedio)

# 9

def contar_hinchas_boca():
    filtro = df["Cuadro"] == "Boca"
    cant_hinchas_boca  = filtro.sum()
    if cant_hinchas_boca / df.shape[0] > 0.5:
        return True
    else:
        return False

def biologia():
    filtro = df["Carrera"] == "Biologia"
    cant_biologos = filtro.sum()
    if cant_biologos / df.shape[0] > 0.5:
        return True
    else:
        return False
    
    
def hinchas():
    # Contar la cantidad de hinchas por cuadro
    agrupo = df["Cuadro"].value_counts().reset_index()
    agrupo.columns = ["Cuadro", "count"]  # Renombrar las columnas
    
    # Crear el gráfico de barras
    sns.barplot(data=agrupo, x="Cuadro", y="count")
    
    # Añadir etiquetas y título
    plt.xlabel("Cuadro")
    plt.ylabel("Cantidad de hinchas")
    plt.title("Cantidad de hinchas por cuadro")
    
    # Mostrar el gráfico
    plt.show()
