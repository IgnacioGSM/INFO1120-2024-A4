import pandas as pd
from sqlite3 import connect
import entradas as ent

def get_database(file):
    conexion = connect(file)

    db = pd.read_sql("SELECT * from Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol",conexion)
    return db

def filtro(dataframe="df",columna="rut", condicion=False):
    if condicion:
        subDF = dataframe[dataframe[columna] == condicion]
    else:
        subDF = dataframe[[columna]]
    return subDF


df = get_database("db_personas.db")

columnas_seleccion_unica = {
    1 : "rut",
    2 : "nombre_completo"
}
columnas_seleccion_multiple = {
    1 : "profesion",
    2 : "nacionalidad"
}

print("1- Un solo documento\n2- Multiples documentos")
seleccion_numero_documentos = ent.seleccion_opciones(2)

if seleccion_numero_documentos == 1:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_unica.items():
        print(f"{key}- {value}")
    columna_elegida = ent.seleccion_opciones(len(columnas_seleccion_unica))
    subDF = filtro(df,columnas_seleccion_unica[columna_elegida])
    print(subDF)
    print()
    while True:
        condicion = ent.entrada_numero("Seleccione una fila: ")
        if condicion > 0 and condicion < len(subDF):
            break
        print("ERRORRR")
    
    subDF = df.iloc[condicion]
    print(subDF)


else:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_multiple.items():
        print(f"{key}- {value}")
    columna_elegida = ent.seleccion_opciones(len(columnas_seleccion_multiple))
    opciones = sorted(list(set(df[columnas_seleccion_multiple[columna_elegida]])))
    for i in range(len(opciones)):
        print(f"{i+1}- {opciones[i]}")
    print()
    condicion = ent.seleccion_opciones(len(opciones))
    condicion = opciones[condicion-1]
    subDF = filtro(df,columnas_seleccion_multiple[columna_elegida],condicion)
    subDF.reset_index(inplace=True,drop=True)
    print(subDF)
    print("\nEscoja el rango: ")
    inf = ent.entrada_indice(0,len(subDF),"Ingrese el limite inferior: ")
    sup =ent.entrada_indice(inf,len(subDF),"Ingrese el limite superior: ")
    print(subDF.iloc[inf:sup+1])
