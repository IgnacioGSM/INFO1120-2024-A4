def entrada_numero(mensaje="Ingrese un numero: "):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, asegurese de ingresar solo numeros enteros")
        else: return entrada

def seleccion_opciones(x, mensaje="Elige una opcion: "):
    while True:
        try: entrada = int(input(mensaje))
        except ValueError: print("Error, escriba un número en las opciones de arriba.")
        else:
            if entrada in range(1,x+1):
                return entrada
            else: print("No hay una opción con ese número, intente otro")

def entrada_indice(inferior=0,superior=1, mensaje="hola"):
    while True:
        x = entrada_numero(mensaje)
        if x < superior and x >= inferior:
            return x
        print(f"Indice erroneo, asegurese de ingresar un numero entre {inferior} y {superior-1}")