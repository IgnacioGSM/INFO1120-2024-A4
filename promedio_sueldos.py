import matplotlib.pyplot as mpl
from data import get_database, filtro

df = get_database("db_personas.db")

profesiones = sorted(list(set(df["profesion"])))

print(profesiones)