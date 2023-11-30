catalogo = [["00025", "Volvo", "Comfort", "2005", 3000, "Cd Obregón - Puebla", "Sin servicio"], ["34", "chupepa", "Comfort", "2005", 3000, "Cd Obregón - Puebla", "Sin servicio"]]

def main_mostrar(catalogo): 

    from funciones_apoyo import imprimir_registrados

    print("---------------Mostrar autobuses--------------------")
    print("""1. Mostrar todoos los autobuses
2. Motrar autobuses por su ruta
3. Mostrar autobuses por su estado de servicio 
4. Mostrar autobuses por su kilometraje
5. Cancelar operación""")
    
    opcion = input("Ingresa tu selección: ")
    
    if opcion == "1":
        imprimir_registrados(catalogo)
    elif opcion == "2":
        mostrar_p_ruta(catalogo)
    elif opcion == "3":
        mostrar_p_estado
    elif opcion == "4":
        pass
    elif opcion == "5":
        print("Operación cancelada")
    else: 
        print("Ingresa un valor válido")

def imprimir_registrados(catalogo):
    for x in range(len(catalogo)):
        print(x)  # falta formato de impresión

def mostrar_p_ruta(catalogo):
    
    from funciones_apoyo import buscar, buscarimprimir
    autobuses = 0

    print(type(catalogo))

    print("------------ Mostrar autobuses por ruta ------------")
    print("""---------------Rutas--------------------
    1. Cd Obregón - Puebla
    2. Cd Obregón - Los Mochis
    3. Cd Obregón - Guadalajara
    4. Cd Obregón - Durango 
    5. Hermosillo - Ciudad Juárez
    6. Hermosillo - Cancún""")
    ruta = input("Ingresa la opción de tu ruta: ") # Try
    
    if ruta == "1":
        rutastr = "Cd Obregón - Puebla"
    elif ruta == "2":
        rutastr = "Cd Obregón - Los Mochis"
    elif ruta == "3":
        rutastr = "Cd Obregón - Guadalajara"
    elif ruta == "4":
        rutastr = "Cd Obregón - Durango"
    elif ruta == "5":
        rutastr = "Hermosillo - Ciudad Juárez"
    elif ruta == "6":
        rutastr = "Cd Obregón - Cancún"
    else:
        rutastr = "fritoschorizo45" #Valor clave de rutastr que significa que no existe ninguna ruta válida

    if rutastr == "fritoschorizo45":
        print("Ingresa un valor valido")
    else:
        print("---------------------------------------------------------------------------------------------------------------------")
        print("Número  :   Marca     :    Modelo   :    Año   :  Kilometraje   :          Ruta          :     Estado")
        print("---------------------------------------------------------------------------------------------------------------------")

        


def mostrar_p_estado(catalogo):
    from funciones_apoyo import buscarimprimir

    print("------------ Mostrar autobuses por estado de servicio ------------")
    print("1. Sin servicio\n", "2. Proximo a servicio\n", "3. Servicio programado\n", "4. En Servicio")
    estado = int(input("Ingresa una opción de estado: ")) #try

    if estado == "1":
        estadostr = "Sin servicio"
    elif estado == "2":
        estadostr = "Proximo a servicio"
    elif estado == "3":
        estadostr = "Servicio programado"
    elif estado == "4":
        estadostr = "En servicio"
    else:
        estadostr = "fritoschorizo45"

    if estadostr == "fritoschorizo45":
        print("Ingresa un valor válido")
    else: 
        print("---------------------------------------------------------------------------------------------------------------------")
        print("Número  :   Marca     :    Modelo   :    Año   :  Kilometraje   :          Ruta          :     Estado")
        print("---------------------------------------------------------------------------------------------------------------------")
        buscarimprimir(estadostr, catalogo)

def mostrar_p_km(catalogo):
    access = True
    maxx = 0
    minn = 0
    autobuses = 0

    while access:
        try:
            minn = int(input("Ingresa el kilometraje mínimo: "))
            maxx = int(input("Ingresa el kilometrake máximo: "))
            access = False
        except: 
            print("Ingresa números enteros")
            selec = input("¿Desear cancelar la oepración? (S/N)").capitalize()
            
            if selec == "S":
                access = False

    for x in range(len(catalogo)):
        if maxx >= catalogo[x][4] >= minn:
            print(catalogo[x]) #falta formato de impresión 
            autobuses += 1 

    if autobuses == 0: 
        print("No hay autobuses en este rango de kilometrake")

mostrar_p_km(catalogo)






    


