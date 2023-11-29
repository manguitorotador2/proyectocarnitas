
def alta(catalogo):
    from funciones_apoyo import buscar, imprimir_registrados

    print("\n--------------- Registro de autobus --------------------")
    autobus = []
    numero = input("Ingrese el número del autobus: ")
    index = buscar(numero, catalogo) #convoco a la función buscar, dándole como argumentos el número a validar y la lista que se va a anlizar

    if index == "empanadasdepiña13": #empanadasdepiña13 es la clave en la función buscar que significa que no se encontró el valor en la lista específicada, si es cualquiero otro valor, es un index y existe en la lista
        print("\n---------------Datos Adicionales--------------------")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año de fabricación: ")
        kilometros = input("Kilometros recorridos: ")
        print("""---------------Rutas--------------------
        1. Cd Obregón - Puebla
        2. Cd Obregón - Los Mochis
        3. Cd Obregón - Guadalajara
        4. Cd Obregón - Durango 
        5. Hermosillo - Ciudad Juárez
        6. Hermosillo - Cancún
                    """) #Muestro las rutas como datos fijos con su respectivo número
        ruta = int(input("Ingresa el número de ruta: "))
        if ruta == 1: #asigno la ruta según su código
            ruta = "Cd Obregón - Puebla"
        elif ruta == 2:
            ruta = "Cd Obregón - Los Mochis"
        elif ruta == 3:
            ruta = "Cd Obregón - Guadalajara"
        elif ruta == 4:
            ruta = "Cd Obregón - Durango"
        elif ruta == 5:
            ruta = "Hermosillo - Ciudad Juárez"
        elif ruta == 6:
            ruta = "Hermosillo - Cancún"
        else:
            print("Ingresa un número de ruta válido")
            ruta = "nope"


        if ruta != "nope":
            autobus.append(numero) 
            autobus.append(marca)
            autobus.append(modelo)
            autobus.append(año)
            autobus.append(kilometros)
            autobus.append(ruta)
            autobus.append("Sin servicio")
            confirmation = input("¿Confirmar el registro? (S/N)").capitalize()
            if confirmation == "S":   #confirmación si realmente se quiere registrar el autobus
                catalogo.append(autobus)
                print("La unidad se ha registrado correctamente\n")
                imprimir_registrados(catalogo)
        else:
            print("Ruta no válida")
            #le doy formato a la lista autobus con sus respectivas propiedades
    
    else:
        print("Este autobus ya se encuentra registrado o el número no es valido") #cualquier otro valor a fuerzas es un index, por lo que si existe
        


