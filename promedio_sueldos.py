import matplotlib.pyplot as mpl
from data import get_database
from numpy import mean

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

sueldo_promedio = []
for pro in profesiones:
    sueldo_promedio.append(mean(df[df["profesion"] == pro]["Sueldo"]))

print(sueldo_promedio)