from entradas import *
from data import *

def main_menu():
    menu = {
        1 : "Un solo documento",
        2 : "Multiples documentos",
        3 : "Salir"
    }
    acciones = {
        1 : seleccion_unica,
        2 : seleccion_multiple,
        3 : "lalala"
    }
    for key,value in menu.items():
        print(f"{key}- {value}")
    seleccion = seleccion_opciones(3)
    acciones[seleccion]()
    
    
def seleccion_unica():
    columnas = {
    1 : "rut",
    2 : "nombre_completo"
    }
    print("uwu")


def seleccion_multiple():
    pass



main_menu()

df = get_database("db_personas.db")

columnas_seleccion_unica = {
    1 : "rut",
    2 : "nombre_completo"
}
columnas_seleccion_multiple = {
    1 : "profesion",
    2 : "nacionalidad",
    3 : "Rol"
}

print("1- Un solo documento\n2- Multiples documentos")
seleccion_numero_documentos = seleccion_opciones(2)

if seleccion_numero_documentos == 1:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_unica.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas_seleccion_unica))
    subDF = filtro(df,columnas_seleccion_unica[columna_elegida])
    print(subDF)
    print()
    condicion = entrada_indice(0,len(subDF),"Ingrese el indice del dato deseado: ")
    subDF = df[df.index == condicion]
    print(subDF)
    subDF.reset_index(inplace=True)
    singular_data_to_contract(subDF,0)


else:
    print("Escoja un criterio por el que buscar:")
    for key,value in columnas_seleccion_multiple.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas_seleccion_multiple))
    opciones = sorted(list(set(df[columnas_seleccion_multiple[columna_elegida]])))
    for i in range(len(opciones)):
        print(f"{i+1}- {opciones[i]}")
    print()
    condicion = seleccion_opciones(len(opciones))
    condicion = opciones[condicion-1]
    subDF = filtro(df,columnas_seleccion_multiple[columna_elegida],condicion)
    subDF.reset_index(inplace=True,drop=True)
    print(subDF)
    print("\nEscoja el rango: ")
    inf = entrada_indice(0,len(subDF),"Ingrese el limite inferior: ")
    sup = entrada_indice(inf,len(subDF),"Ingrese el limite superior: ")
    subDF = subDF.iloc[inf:sup+1]
    subDF.reset_index(inplace=True)
    print(subDF)
    for i in range(len(subDF)):
        singular_data_to_contract(subDF,i)