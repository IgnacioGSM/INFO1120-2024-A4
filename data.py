import pandas as pd
from sqlite3 import connect

def get_database(file):
    conexion = connect(file)

    db = pd.read_sql("SELECT * from Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol",conexion)
    return db

hola = get_database("db_personas.db")

print(hola)