import matplotlib.pyplot as plt
from data import get_database
from numpy import mean

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

sueldo_promedio = []
for pro in profesiones:
    sueldo_promedio.append(mean(df[df["profesion"] == pro]["Sueldo"]))

plt.figure(figsize=(12,5))
plt.bar(profesiones,sueldo_promedio, 0.4)
plt.title("Promedio de sueldo por profesión")
plt.ylabel("Sueldo promedio (Millones CLP)")
plt.xticks(rotation=45)
plt.yticks(range(0,2250000,250000))
plt.subplots_adjust(bottom=0.45)
plt.grid(True)
plt.show()