from cargarInventario import ubicaciones 
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Informe de inventario\n")
    file.write("Producto        cantidad        Precio Unitario         Valor Total          Ubicación\n")
    file.write("______________________________________________________________________________________\n")
    