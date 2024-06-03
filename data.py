import pandas as pd
from sqlite3 import connect
conexion = connect("db_personas.db")

df = pd.read_sql("SELECT * from Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol",conexion)


print(df)