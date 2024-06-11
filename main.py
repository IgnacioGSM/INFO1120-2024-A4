import matplotlib.pyplot as plt
from entradas import *
from data import *
from numpy import mean

def main_menu():
    print()
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
    seleccion = seleccion_opciones(len(menu))
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

    print("\nSe ha generado el contrato\nescriba 1 para volver al menú\nescriba 2 para salir del programa")
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
    
    print("\nSe han generado los contratos\nescriba 1 para volver al menú\nescriba 2 para salir del programa")
    regreso = seleccion_opciones(2,"")
    if regreso == 1:
        main_menu()
    elif regreso == 2:
        return






def graficos():
    print()
    menu = {
        1 : "Gráfico de barras, promedio de los sueldos para cada profesión",
        2 : "Grafico de tarta, distribución de profesionales por profesión",
        3 : "Gráfico de barras, distribución de profesionales por nacionalidad",
        4 : "Volver al menú",
        5 : "Salir del programa"
    }
    acciones = {
        1 : barras_promedio_sueldos,
        2 : tarta_profesiones,
        3 : barras_distribucion_nacionalidades,
        4 : main_menu
    }
    for key,value in menu.items():
        print(f"{key}- {value}")
    seleccion = seleccion_opciones(len(menu))
    if seleccion == 5:
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


def tarta_profesiones():
    print()
    profesiones = sorted(list(set(df["profesion"])))

    distribucion = []
    for pro in profesiones:
        distribucion.append(len(df[df["profesion"] == pro]))

    plt.figure(figsize=(10,5))
    plt.pie(distribucion, labels=profesiones, autopct="%1.1f%%", textprops={"size" : "small"},radius=1.25)
    plt.title("Distribución de profesiones\n")
    plt.show()

    menu_post_grafico(tarta_profesiones)


def barras_distribucion_nacionalidades():
    print()
    nacionalidades = sorted(list(set(df["nacionalidad"])))

    cantidad = []
    for nac in nacionalidades:
        cantidad.append(len(df[df["nacionalidad"] == nac]))


    plt.bar(nacionalidades,cantidad)
    plt.title("Conteo de profesionales por nacionalidad")
    plt.grid(True)
    plt.ylabel("Cantidad de profesionales")
    plt.xlabel("Nacionalidades")
    plt.show()

    menu_post_grafico(barras_distribucion_nacionalidades)


df = get_database("db_personas.db")

main_menu()