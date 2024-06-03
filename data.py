import pandas as pd
from sqlite3 import connect

def get_database(file):
    conexion = connect(file)

    db = pd.read_sql("SELECT * from Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol",conexion)
    return db

def filtro_singular(dataframe="df",columna="rut", condicion="11316802-1"):
    dato = dataframe[dataframe[columna] == condicion]
    return dato

df = get_database("db_personas.db")


hola = filtro_singular(df,"rut","1518146-K")

print(hola)