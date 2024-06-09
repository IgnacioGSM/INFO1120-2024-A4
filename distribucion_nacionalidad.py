import matplotlib.pyplot as plt
from data import get_database

df = get_database("db_personas.db")

nacionalidades = sorted(list(set(df["nacionalidad"])))

cantidad = []
for nac in nacionalidades:
    cantidad.append(len(df[df["nacionalidad"] == nac]))
