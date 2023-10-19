
ubicaciones = {}
def leerDoc(): #se buscará el documento y se leerá
    while True:
        archivo = input("Ingrese el nombre del archivo: ") #se almacena su nombre
        try:    
            with open(archivo + ".inv", encoding="utf-8") as file:
                #con esto se leera el archivo solicitado
                for linea in file:
                    valores = linea.strip().split(";") #se le quitarán las separaciones
                    if len(valores) == 4:  # Asegurarse de que hay exactamente 4 valores en la línea
                        producto, cantidad, precio, ubicacion = valores
                        inst, producto_Valido = producto.split(" ")
                        if inst == "": print("nada")  

                        if ubicacion in ubicaciones:#diccionario anidadoso
                            ubicaciones[ubicacion][producto_Valido] = {  
                                #si algo ya existe en la ubicacion
                                "cantidad": float(cantidad), #solo actualizara
                                "precio": float(precio)
                            }
                        else:
                            ubicaciones[ubicacion] = { #pero sino, debera crear un diccionario
                                #en donde guardarlo
                                producto_Valido: {"cantidad": float(cantidad), "precio": float(precio)}
                            }
                    else:
                        print("Formato de línea incorrecto:", linea)
                    #si el formato esta mal en el archivo lo demostrara
                    
            print("...Carga Exitosa...")
            print("-------------------") 
        except FileNotFoundError:
            print("El documento no existe o se escribio de manera incorrecta")
        break



        #   producto = linea.split(" ")[1].split(";")[0]
        #return file.leelinea()
    
#def Pdoc(): #Se tomará el documento y se almacenara en una lista 
#   line = leerDoc()
#  print("...Carga Exitosa...")
# for i in line:
#    split = i.split(";") # con este metodo se divide  por ';'
