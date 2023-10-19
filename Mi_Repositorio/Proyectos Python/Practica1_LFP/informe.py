from cargarInventario import ubicaciones 
#from cargarMov import productos 
def generar_reporte():
    contador = 1230

    with open("resultado"+str(contador)+".txt", "w", encoding="utf-8") as file:
        file.write("Informe de inventario\n")
        file.write("Producto        cantidad        Precio Unitario         Valor Total          Ubicación\n")
        file.write("_" *100 + "\n")
        
        for ubicacion, productos in ubicaciones.items():
            #se accederá a la ubicacion y los productos en ella
            #y atraves de .items se recorrera el diccionario
            for  producto, info in productos.items():
                #ya en productos se tomara info para recorrer este diccioanrio 
                #tomando el valor de la cantidad y precio y con ello se genere un valor total
                cantidad = info["cantidad"]
                precio = info["precio"]
                valorTotal = cantidad*precio
                
                line = "{:<10} {:>15} {:>15} {:>20} {:>20}\n".format(producto, "{:.2f}".format(cantidad),
                "${:.2f}".format(precio),"${:.2f}".format(valorTotal), ubicacion  )
                #escritura de cada valor recorrido en columnas con ayuda de .format
                file.write(line)
    print("Informe creado con exito....")            


# Llamar a la función para generar el reporte

"""
 ubicacion = info["ubicacion"]
                valorTotal = precio* cantidad

                file.write("                  ")
                file.write(ubicacion)
                file.write("                  ")
                file.write(str(valorTotal))"""