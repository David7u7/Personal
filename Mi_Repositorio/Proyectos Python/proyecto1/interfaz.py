import json
#uso en funciones
import os
import tkinter as tk
#widgets
from tkinter import (Label, PhotoImage, Tk, filedialog, messagebox,
                    scrolledtext, ttk)

from PIL import Image, ImageTk

#funciones
from analizador import (analizar, configuracion, create_instructions,
                        get_instruccion, mostrar_elementos, mostrar_errores,
                        tokenize_input)
from graficas.Arbol import *

nombre_archivo = None

#____________________FUNCIONES______________________________________________
#Las funciones del combo box
def seleccionar_opcion(event):
    opcion_seleccionada = combo.get()
    
    if opcion_seleccionada == "Salir":
        ventana.destroy()
    elif opcion_seleccionada == "Abrir":
        print("Ha seleccionado abrir el archivo")
        abrir_archivo()
    elif opcion_seleccionada == "Guardar":
        guardar()
        print("Se ha pedido guardar ")
    elif opcion_seleccionada == "Guardar Como":
        print("Se ha pedido guardar ")
        guardar_como()

#para el boton abrir
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        global nombre_archivo,contenido
        with open(archivo, "r") as f:
            contenido = f.read()
            arbol= tokenize_input(contenido)

            #implementando el arbol
            #arbol = analizar(contenido)
            #print(arbol.dot.source)

            cuadro_texto.delete(1.0, tk.END)  # Borra el contenido actual
            cuadro_texto.insert(tk.END, contenido)
        nombre_archivo = os.path.basename(archivo)
        messagebox.showinfo("Listo","Carga exitosa")
        return contenido, nombre_archivo,arbol
    
#para guardar con el mismo nombre
def guardar():
    contenido = cuadro_texto.get(1.0, tk.END)
    if contenido == "":
        messagebox.showwarning("Vacio","No hay nada que guardar")
    elif nombre_archivo is None or not isinstance(nombre_archivo, str):
        messagebox.showwarning("Nombre de archivo inválido", "Por favor, introduce un archivo antes de guardar")
    else:    
        with open(nombre_archivo,"w") as archivo:
            archivo.write(contenido)
            messagebox.showinfo("Exito","El archivo se ha guardado con éxito")

#guardar con otro nombre y ubicacion
def guardar_como():
    contenido = cuadro_texto.get("1.0", "end-1c")  # Obtiene el contenido del cuadro de texto
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
    
    if nombre_archivo:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
            messagebox.showinfo("Exito","El archivo se ha guardado con éxito")


#botones externos al combo box
#analizar y mostrar cada token y su ubicacion
def analizar_archivo():
    if nombre_archivo is None or not isinstance(nombre_archivo, str):
        messagebox.showwarning("Nombre de archivo inválido", "Por favor, introduce un archivo antes de guardar")
    else:
        dato = mostrar_elementos()
        cuadro_texto.delete(1.0, tk.END)  # Borra el contenido actual
        cuadro_texto.insert(tk.END, dato)

#errores
def crear_errores():
    error = mostrar_errores()
    json_texto = json.dumps(error, indent=4)
    cuadro_texto.delete(1.0, tk.END)  # Borra el contenido actual
    cuadro_texto.insert(tk.END, json_texto)

#reporte
def reporte():
    print("Creando grafico...")
    #arbol = analizar(contenido)


    arbol.agregarConfiguracion(configuracion)
    instrucciones = create_instructions() 
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpretar())

    arbol.dot.view()

def limpiar():
    cuadro_texto.delete(1.0,tk.END)#limpiar el cuadro de textos

#para abrir el manual
def abrir_pdf():
    # Especifica la ruta completa al archivo PDF
    ruta_pdf = os.path.join("partes", "Manual.pdf")  # "pdfs" es el nombre de la carpeta

    # Verifica si el archivo existe en la ruta especificada
    if os.path.isfile(ruta_pdf):
        os.startfile(ruta_pdf)
    else:
        print(f"El archivo {ruta_pdf} no se encuentra en la carpeta.")


#_______________________Creacion de los widgets_____________________________________
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("1200x620")  # dimensiones iniciales de la ventana
ventana.configure(bg="#2F2B2B")


#cuadro de texto
# Cuadro de texto centrado en la ventana
# Crear un Frame para contener el cuadro de texto
frame_cuadro_texto = tk.Frame(ventana)
frame_cuadro_texto.grid( row=2, column=5,  padx=10, pady=10, sticky='nsew')
frame_cuadro_texto.configure(highlightbackground="#131A3D")


# Cuadro de texto dentro del Frame
cuadro_texto = scrolledtext.ScrolledText(frame_cuadro_texto, wrap=tk.WORD, width=60, height=30)
cuadro_texto.pack(expand=True, fill='both')
cuadro_texto.configure(highlightbackground="#131A3D")


# Crear un ComboBox
combo = ttk.Combobox(ventana,width=20,height=18,values=("Abrir", "Guardar", "Guardar Como", "Salir"),state='readonly')
combo.set("Archivo")  # Texto predeterminado
combo.grid(row=0,column=0,padx=10, pady=10)
# Asociar la función al evento <<ComboboxSelected>>
combo.bind("<<ComboboxSelected>>", seleccionar_opcion)

#botones-------------------------------
#botón 1
boton_Analizar = tk.Button(ventana, text="Analizar",   command=analizar_archivo, width=10,height=2, bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
boton_Analizar.grid(row=0, column=1, padx=10, pady=10)

#botón 2
boton_Errores = tk.Button(ventana, text="Errores"  , command=crear_errores, width=10,height=2,  bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
boton_Errores.grid(row=0, column=2, padx=10, pady=10)

#botón 3
boton_Reporte = tk.Button(ventana, text="Reporte" , command=reporte, width=10,height=2, bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
boton_Reporte.grid(row=0, column=3, padx=10, pady=10)

#boton 4
boton_limpiar = tk.Button(ventana, text = "Limpiar", command=limpiar, width=20,height=3, bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
boton_limpiar.grid(row=6, column=5,padx=10, pady=10)

boton_manual = tk.Button(ventana, text = "Ayuda", command=abrir_pdf, width=20,height=2, bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
boton_manual.grid(row=0, column=6,padx=10, pady=10,  columnspan =9)


"""


#PNG___________________________________________
imagen = PhotoImage(file="analizar.png")
# Redimensionar la imagen
imagen = imagen.subsample(4, 4)  # Esto la reduce a la mitad, ajusta según sea necesario
# Crear un Label y asignarle la imagen
label_con_imagen = Label(ventana, image=imagen)
label_con_imagen.grid(row=2, column=0, columnspan=4)




def seleccionar():
    seleccion = combo.get()
    etiqueta.config(text=f'Seleccionaste: {seleccion}')

def agregar_elemento():
    nuevo_elemento = entrada.get()
    combo['values'] = (*combo['values'], nuevo_elemento)
    entrada.delete(0, tk.END)"""

"""# Crear un botón para agregar elementos
entrada = ttk.Entry(ventana)

boton_agregar = ttk.Button(ventana, text="Agregar Elemento", command=agregar_elemento)
boton_agregar.pack(pady=5)
boton_agregar.place(x=500, y=500)
"""
# Etiqueta para mostrar la selección
"""etiqueta = ttk.Label(ventana, text="")
etiqueta.pack(pady=10)
"""
ventana.mainloop()
