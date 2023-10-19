from cargarInventario import ubicaciones
def movDoc():
    while True:
        archivo = input("Ingrese el nombre del archivo: ")
        try:
            with open(archivo + ".mov", encoding="utf-8") as file:
                #con esto se leera el archivo solicitado
                for linea in file:
                    instruccion, resto = linea.strip().split(" ")  # Separar la instrucción del resto
                    valores = resto.split(";")  # Separar los valores usando ;
                    if len(valores) == 3:  # Asegurarse de que hay exactamente 4 valores en la línea
                        producto, cantidad, ubicacion = valores
                    #de esta manera se dividirá la instruccion agregar o vender
                    # y el resto de la info
                    #con la primera parte se podra valuar que es lo que se desea hacer
                        if instruccion == "agregar_stock":
            #los mensajes de error si en caso no es posible concretar la opcion
                            if ubicacion  not in ubicaciones :
                                print("Esa ubicacion no existe  ",linea )
                                continue
                            if producto not in ubicaciones[ubicacion]:
                                print("La ubicacion no coincide  " ,linea)
                                continue
                            ubicaciones[ubicacion][producto]["cantidad"] += float(cantidad)
                            #valor1= ubicaciones[ubicacion][producto]["cantidad"]
                            #valor2 = cantidad
                            #print(str(valor1)+" eso se sumrara" + str(valor2), linea)
                            #si no hay problema entonces accesara en cantidad y sumara la nueva cantidad
                        elif instruccion == "vender_producto":
                            if ubicacion not in ubicaciones:
                                print("Esa ubicacion no existe ",linea)
                                continue
                            if producto not in ubicaciones[ubicacion]:
                                print("Este producto no existe en esta ubicacion  ",linea)
                                continue
                            if ubicaciones[ubicacion][producto]["cantidad"] < float(cantidad):
                                print("No es posible ya que las existencias son limitadas  ",linea)
                                continue
                            else:
                                ubicaciones[ubicacion][producto]["cantidad"] -= float(cantidad) 
                                #valor1= ubicaciones[ubicacion][producto]["cantidad"]
                                #valor2 = cantidad
                                #print(str(valor1)+" eso se restara" + str(valor2),linea )
                    #si no hay problema con cantidades erroneas (menores) entonces restara lo indicado
                    else:
                        print("Error en la operacion, formato incorrecto ")
                    
            print("...Carga exitosa...")
            print("-------------------")
        except FileNotFoundError:
            print("El documento no existe o fue escritó incorrectamente")
        break   

"""line = [] #lista de partes
products = [] #lista con cada parte determinada por su dato
def readDoc(): #se buscará el documento y se leerá
    with open("datos.inv", encoding = "utf-8") as file:
        return file.readlines()
    
def convertir_tipo(dato): #Esta funcion ayudara a valuar haciendo el cambio que se requiera
            try:
                return int(dato)  # Intentamos convertir a int
            except ValueError:
                try:
                    return float(dato)# Si falla, intentamos convertir a float
                except ValueError:
                    return dato # Si ninguna conversión funciona, mantenemos el dato como string        

def movDoc():
    line = readDoc() #a la lista line se le otorgan los datos del archivo dado
    for element in line:
        split = element.split(";") # con este metodo se divide  por ';'
        #haciendo cada parte separada   
        partes_convertidas = list(map(convertir_tipo, split))
        #gracias a map aplicamos la funcion anterior a cada parte separada y eso lo guardo en esta variable

        products.append(partes_convertidas) #cada parte ahora forma una lista nueva

        for elements in products:  #gracias a esta nueva lista se identificaran sus partes 
            nombre = elements[0]
            cantidad = elements[1]     
            ubicacion = elements[3]
        
        
        while True:
            mov = input("¿Qué desea hacer? Inserte agregar o vender  ") #estas son las opciones que tendra
            if mov == "agregar":
                print("ok agregare")
                item = input("ingrese el nombre del producto: ")
                ubication = input("Ingrese su ubicacion: ")
                newCantidad = 0
                if item in nombre and ubication in ubicacion:
                    newCantidad = cantidad + 1
                    elements[1] = newCantidad 
                    print("aca puedes ver que si se actualizo la cantidad: ", newCantidad)
                    print(elements)
                    break  # si se desea agregar entonces pedira su nombre y la ubicacion
                else:
                    print("Lo siento este producto no existe")
                    break

            elif mov == "vender":
                print("ok vender")
                item = input("ingrese el nombre del producto: ")
                ubication = input("Ingrese su ubicacion: ")
                newCantidad = 0
                if item in nombre and ubication in ubicacion:
                    newCantidad = cantidad -1
                    elements[1] = newCantidad
                    print("Aca puedes ver si se vio afectado el dato anterior", cantidad)
                    print(elements)
                    break
            else:
                
                "Inserte una opcion valida"
        break





        

        # Imprimimos los resultados
        #print(partes_convertidas)
        #print(products)
"""






        #join = " ".join(partes_convertidas)
        #print(split)
        #print(join)
