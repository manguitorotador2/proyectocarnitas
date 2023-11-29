
def main_mostrar(catalogo): 

    print("---------------Mostrar autobuses--------------------")
    print("""1. Mostrar todoos los autobuses
2. Motrar autobuses por su ruta
3. Mostrar autobuses por su estado de servicio 
4. Mostrar autobuses por su kilometraje
5. Cancelar operación""")
    
    opcion = int(input("Ingresa tu selección"))
    
    if opcion == 1:
        pass
    elif opcion == 2:
        mostrar_p_ruta(catalogo)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        access = False
    else: 
        print("Ingresa un valor válido")

def mostrar_p_ruta(catalogo):
    print("------------ Mostrar autobuses por ruta ------------")
    print("""---------------Rutas--------------------
    1. Cd Obregón - Puebla
    2. Cd Obregón - Los Mochis
    3. Cd Obregón - Guadalajara
    4. Cd Obregón - Durango 
    5. Hermosillo - Ciudad Juárez
    6. Hermosillo - Cancún""")

main_mostrar(37)



