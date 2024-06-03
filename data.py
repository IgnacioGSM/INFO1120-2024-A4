import pandas as pd
from sqlite3 import connect

def get_database(file):
    conexion = connect(file)

    db = pd.read_sql("SELECT * from Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol",conexion)
    return db

def filtro(dataframe="df",columna="rut", condicion="11316802-1"):
    dato = dataframe[dataframe[columna] == condicion]
    return dato



df = get_database("db_personas.db")


hola = filtro(df,"rut","1518146-K")

multiples = filtro(df,"nacionalidad","Chilena")

for i in multiples.index.values:
    print(df.iloc[i])
    print()

#print(df.iloc[hola.index.values[0]])     # devuelve los datos de una sola fila