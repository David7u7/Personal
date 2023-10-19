
## Interfaz
##### Es acá en donde por medio de la libreria Tkinter, se crean los diversos widgets asi como la ventana principal y cada mensaje hacia el usuario.
 
### *Widgets*
##### Se crearon:
| Botones | ScrolledText | Frame | Combobox |
|--------------|--------------|--------------|--------------|
| Cada con las funciones necesarias para procesar el archivo      | Se tomó como el cuadro de texto para mostrar el contenido y asi mismo editarlo      | Util para contener el Scrolled text      | Necesario para mostrar los metodos de almacenamiento del archivo y su apertura y asi mismo la salida del programa.      |


#### Para los botones se utilizó el metodo *.grid* con el fin de atribuir a cada uno de ellos una posicion en base a fila y columna. Como el presentado a continuacion

```python  
boton_Analizar.grid( row=0 , column=1, padx=10, pady=10)
```
#### Tambien se le atribuyó en cada creacion su respectivo color y fuente y la funcion a invocar.
```python
boton_Analizar = tk.Button(ventana, text="Analizar",   command=analizar_archivo, width=10,height=2, bg="#070D1D",fg="white",activebackground="#15307A",activeforeground="white")
```

### Funciones
- **abrir_Archivo:** a travez de un *filedialog* se podrá dar apertura al archivo y tambien lectura... invocando la funcion encargada de analizar el contenido en cada linea, se guardará su nombre y tambien se mostrará su contenido en el cuadro de texto.
```python
archivo = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
```
```python
nombre_archivo = os.path.basename(archivo)
        messagebox.showinfo("Listo","Carga exitosa")
```

- **guardar:** tomando el nombre del archivo que se abrió, se podra guardar los cambios realizados en el mismo, conservando su nombre, si no se ha seleccionado nada entonces lo hará saber al usuario.
- **guardar_como:** se abrirá un nuevo *filedialog* con el proposito de poder guardar con un nuevo nombre o bien en un nuevo lugar especifico.
- **analizar_archivo:** se encargará de hacer notorio cada token almacenado del archivo dado
- **crear_errores:** mostrará el resultado de los errores encontrados utilizando el analizador lexico. 
- **reporte:** hará un pdf en donde se podra ver una grafica mostrando las operaciones contenidas en el archivo dado.
- **limpiar:** se encargara  de limpiar el cuadro de texto.


### Navegacion 
- [Ir a la Sección de expresiones](../partes/expresiones.pdf)

- [Ir a la Sección de analizador](../partes/analizador.pdf)

- [Ir a la Sección de graficas](../partes/grafo.pdf)