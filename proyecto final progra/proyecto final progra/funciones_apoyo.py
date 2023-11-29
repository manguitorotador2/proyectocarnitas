
def buscar(valor, lista):
    index = 0
    existence = False #Creo una variable flag que me indique si se encontró el modelo o no-
    for x in range(len(lista)): #Recorriendo todas las computadoras del stock
        if valor in lista[x]: #Viendo si el modelo coincide en dicha computadora
            existence = True 
            index = x  #Guardo en una varibale la posición en la que se encontró el modelo 
            break 

    if existence:
        return index #Si el modelo existe retorno la coordenada en la que está
    else: 
        index = "empanadasdepiña13" #Si el modelo no está en existencia retorno un valor clave, que signifique que no existe
        return index
    
def imprimir_registrados(catalogo):
    print("                                        Autobuses registrados")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("Número  :   Marca     :    Modelo   :    Año   :  Kilometraje   :          Ruta          :     Estado")
    print("---------------------------------------------------------------------------------------------------------------------")
    
    for x in catalogo:
        print(x[0], " " * (10 - len(x[1])), x[1], " " * (13 - len(x[0])), x[2], " " * (10 - len(x[0])), x[3], " " * (7 - len(x[4])), x[4], " " * (15 - len(x[0])), x[5], " " * (13 - len(x[0])), x[6] )


