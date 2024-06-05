import pandas as pd
from sqlite3 import connect

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

def seleccion_opciones(x, mensaje="Elige una opcion: "):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, escriba un número en las opciones de arriba.")
        else:
            if entrada in range(1,x+1):
                return entrada
            else: print("No hay una opción con ese número, intente otro")


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
seleccion_numero_documentos = seleccion_opciones(2)

if seleccion_numero_documentos == 1:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_unica.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas_seleccion_unica))
    subDF = filtro(df,columnas_seleccion_unica[columna_elegida])
    print(subDF)
    print()
    while True:
        condicion = int(input("Seleccione una fila: "))
        if condicion > 0 and condicion < len(subDF):
            break
        print("ERRORRR")
    
    subDF = df.iloc[condicion]
    print(subDF)


else:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_multiple.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas_seleccion_multiple))
    opciones = sorted(list(set(df[columnas_seleccion_multiple[columna_elegida]])))
    for i in range(len(opciones)):
        print(f"{i+1}- {opciones[i]}")
    print()
    condicion = seleccion_opciones(len(opciones))
    condicion = opciones[condicion-1]
    subDF = filtro(df,columnas_seleccion_multiple[columna_elegida],condicion)
    subDF.reset_index(inplace=True,drop=True)
    print(subDF)