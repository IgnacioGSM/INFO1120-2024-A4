import matplotlib.pyplot as plt
from entradas import *
from data import *
from numpy import mean

def main_menu():
    menu = {
        1 : "Un solo documento",
        2 : "Multiples documentos",
        3 : "Gráficos",
        4 : "Salir"
    }
    acciones = {
        1 : seleccion_unica,
        2 : seleccion_multiple,
        3 : graficos
    }
    for key,value in menu.items():
        print(f"{key}- {value}")
    seleccion = seleccion_opciones(3)
    if seleccion == 4:
        return
    else:
        acciones[seleccion]()
    
    
def seleccion_unica():
    columnas = {
    1 : "rut",
    2 : "nombre_completo"
    }

    print("\nEscoja un criterio por el que buscar:")
    for key,value in columnas.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas))
    print()
    subDF = filtro(df,columnas[columna_elegida])
    print(subDF)
    print()
    condicion = entrada_indice(0,len(subDF),"Ingrese el indice del dato deseado: ")
    subDF = df[df.index == condicion]
    print(subDF)
    subDF.reset_index(inplace=True)
    singular_data_to_contract(subDF,0)

    print("Se ha generado el contrato, escriba 1 para volver al menú o escriba 2 para salir del programa")
    regreso = seleccion_opciones(2,"")
    if regreso == 1:
        main_menu()
    elif regreso == 2:
        return


def seleccion_multiple():
    columnas = {
    1 : "profesion",
    2 : "nacionalidad",
    3 : "Rol"
    }

    print("\nEscoja un criterio por el que buscar:")
    for key,value in columnas.items():
        print(f"{key}- {value}")
    columna_elegida = seleccion_opciones(len(columnas))
    print()

    opciones = sorted(list(set(df[columnas[columna_elegida]])))
    for i in range(len(opciones)):
        print(f"{i+1}- {opciones[i]}")
    print()

    condicion = seleccion_opciones(len(opciones))
    condicion = opciones[condicion-1]
    subDF = filtro(df,columnas[columna_elegida],condicion)
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
    
    print("Se han generado los contratos, escriba 1 para volver al menú o escriba 2 para salir del programa")
    regreso = seleccion_opciones(2,"")
    if regreso == 1:
        main_menu()
    elif regreso == 2:
        return






def graficos():
    print()
    menu = {
        1 : "Gráfico de barras, promedio de los sueldos para cada profesión",
        2 : "Volver al menú",
        3 : "Salir del programa"
    }
    acciones = {
        1 : barras_promedio_sueldos,
        2 : main_menu
    }
    for key,value in menu.items():
        print(f"{key}- {value}")
    seleccion = seleccion_opciones(3)
    if seleccion == 3:
        return
    else:
        acciones[seleccion]()

def menu_post_grafico(grafico):
    menu = {
        1 : "Mostrar gráfico otra vez",
        2 : "Volver a la selección de gráficos",
        3 : "Volver al menú inicial",
        4 : "Salir"
    }
    acciones = {
        1 : grafico,
        2 : graficos,
        3 : main_menu
    }
    for key,value in menu.items():
        print(f"{key}- {value}")
    seleccion = seleccion_opciones(4)
    if seleccion == 4:
        return
    else:
        acciones[seleccion]()


def barras_promedio_sueldos(): 
    print()
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
    
    menu_post_grafico(barras_promedio_sueldos)


df = get_database("db_personas.db")

main_menu()