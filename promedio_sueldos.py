import matplotlib.pyplot as plt
from data import get_database
from numpy import mean

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

sueldo_promedio = []
for pro in profesiones:
    sueldo_promedio.append(mean(df[df["profesion"] == pro]["Sueldo"]))

plt.bar(profesiones,sueldo_promedio)
plt.ylabel("Sueldo promedio (Millones CLP)")
plt.show()