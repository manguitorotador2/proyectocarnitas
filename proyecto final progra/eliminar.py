
def baja(catalogo): 
    access = True
    from funciones_apoyo import buscar, imprimir_registrados
    while access: 
        
        imprimir_registrados()
        print("\n")
        numero = input("Ingrese el número de autobus a ingresar: ")
        index = buscar(numero, catalogo)

        if index == "empanadasdepiña13": 
            print("El número de autobus no existe en el catálogo")
            access = False
        else: 
            imprimir_registrados(index, catalogo)
            confirmation = input("¿Realmente desea eliminar el autobús y todos sus datos? (S/N) ").capitalize()
            if confirmation == "S":
                catalogo.pop(index)
                print("El autobus se ha dado de baja correctamente")
                imprimir_registrados()

                status = input("¿Desea eliminar otro autobus? (S/N)").capitalize()
                if status == "N":
                    access = False
                    

