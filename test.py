import pandas as pd
from sqlite3 import connect
conexion = connect("db_personas.db")

df = pd.read_sql('SELECT fecha_ingreso AS Fecha, Rol, residencia as Residencia, rut AS RUT, nombre_completo AS "Nombre Completo", \
                 nacionalidad AS Nacionalidad, fecha_de_nacimiento AS "Fecha de Nacimiento", profesion AS Profesion, sueldo AS Sueldo \
                 FROM Salarios AS sal \
                 INNER JOIN personas AS pe \
                 ON sal.id_salarios = pe.id_rol;',conexion)

print(df)