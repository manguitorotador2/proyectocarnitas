materiales = ()
servicios = []
catalogo = []

def main():
    from registrar import alta
    from eliminar import baja
    from mostrar import main_mostrar
    access = True

    print("Bienvenidos a nuestro sistema")
    while access: 
        print("""\n--------------- Menu --------------------
1. Agregar un nuevo autobús al catálogo
2. Dar de baja un autobús del catálogo
3. Actualizar los datos de un autobús
4. Mostrar el listado de autobuses en el catálogo
5. Programar un servicio para un autobús
6. Eliminar un Servicio programado
7. Actualizar datos de servicio (fecha y cantidad de materiales)
8. Mostrar el listado de servicios programados
9. Mostrar los materiales disponibles
10. Actualizar estatus del servicio
11. Cerrar sistema\n""")
        
        selection = int(input("Ingresa el número de tu opción: "))

        if selection == 1:
            alta(catalogo)            
        elif selection == 2:
            baja(catalogo)
        elif selection == 3:
            pass
        elif selection == 4:
            main_mostrar(catalogo)
        elif selection == 5:
            pass
        elif selection == 6:
            pass
        elif selection == 7:
            pass
        elif selection == 8:
            pass
        elif selection == 9:
            pass
        elif selection == 10:
            pass
        elif selection == 11:
            access = False
        else: 
            print("Ingresa un valor válido\n")

if __name__ == "__main__":
    main()



