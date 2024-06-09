import matplotlib.pyplot as plt
from data import get_database

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

distribucion = []
for pro in profesiones:
    distribucion.append(len(df[df["profesion"] == pro]))

plt.figure(figsize=(10,5))
plt.pie(distribucion, labels=profesiones, autopct="%1.1f%%", textprops={"size" : "small"},radius=1.25)
plt.title("Distribución de profesiones\n")
plt.show()