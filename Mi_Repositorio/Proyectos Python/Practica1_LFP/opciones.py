#importaciones necesarias
import cargarInventario
import cargarMov
import informe 

#funcion para presentar las opciones a elegir
def escoger_opciones():
    while True:
        print("     ¿Qué desea hacer?       ")
        print(""" 
1. Cargar Inventario Inicial
2. Cargar Instrucciones de Movimientos
3. Crear Informe de Inventario
4. Salir""")
        #estas son las unicas opciones validas, de no ser asi mostraraun error
        op = ("1","2","3","4")   
        option = input("Ingrese una opcion:  ")
        if not option in op:
            print('Esa opcion no es valida')
        elif option == "1":
            print("Elegiste cargar inventario...")
            cargarInventario.leerDoc()
            #del modulo cargarInvetario se extraerá la funcion en cargada de mostrar
        elif option == "2":
            print("Elegiste movimientos")
            cargarMov.movDoc() #con este modulo se haran los movimientos en inventario
        elif option == "3":
            print("Elegiste generar informe")
            print("...Informe en proceso...")
            informe.generar_reporte()
            #se creara un archivo de texto con ayuda de este modulo
        elif option == "4":
            print("Regresa pronto")
            break


