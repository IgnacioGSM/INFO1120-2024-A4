import matplotlib.pyplot as plt
from data import get_database

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

distribucion = []
for pro in profesiones:
    distribucion.append(len(df[df["profesion"] == pro]))
print(distribucion)