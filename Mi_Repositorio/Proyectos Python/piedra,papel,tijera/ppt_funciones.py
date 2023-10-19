import tkinter as tkr
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import tkinter.simpledialog

jugador = ""
pc = ""




# Funciones para la creación de imágenes
def crearImagen(path, canvas, imagen):
    canvas.create_image(150, 100, anchor=tkr.CENTER, image=imagen)
    #el canva donde se coloca, la imagen que se coloca 

def piedraJugador(event):
    global jugador
    crearImagen(imagen_tkPiedra, canvasJg, imagen_tkPiedra) #llamando la funcion encargada de crear el canva
    jugador = "piedra"
    opcionPc()

def tijeraJugador(event):
    global jugador
    crearImagen(imagen_tkTijera, canvasJg, imagen_tkTijera)
    jugador = "tijera"
    opcionPc()

def papelJugador(event):
    global jugador
    crearImagen(imagen_tkPapel, canvasJg, imagen_tkPapel)
    jugador = "papel"
    opcionPc()

def papelPc():
    crearImagenPc(imagen_tkPapelpc)

def tijeraPc():
    crearImagenPc(imagen_tkTijerapc)

def piedraPc():
    crearImagenPc(imagen_tkPiedrapc)

# Funciones para actualización de puntos
def actualizarPuntos(jugador, pc):
    global puntos_jugador_str
    global puntos_pc_str

    if (jugador == "piedra" and pc == "papel") or (jugador == "papel" and pc == "tijera") or (jugador == "tijera" and pc == "piedra"):
        messagebox.showinfo("Ganador","Ha ganado el Computador")
        puntos_pc_str.set(str(int(puntos_pc_str.get()) + 1))

    elif (jugador == "papel" and pc == "piedra") or (jugador == "tijera" and pc == "papel") or (jugador == "piedra" and pc == "tijera"):
        messagebox.showinfo("Ganador","Ha ganado el Jugador")
        puntos_jugador_str.set(str(int(puntos_jugador_str.get()) + 1))

    elif (jugador == "papel" and pc == "papel") or (jugador == "tijera" and pc == "tijera") or (jugador == "piedra" and pc == "piedra"):
        messagebox.showinfo("Ganador","Empate")

# Otras funciones
def opcionPc():
    global pc

    options = ("piedra", "papel", "tijera")
    pc = random.choice(options)  #eleccion de la pc
    if pc == "piedra":
        piedraPc()
        actualizarPuntos(jugador, pc)

    elif pc == "papel":
        papelPc()
        actualizarPuntos(jugador, pc)
    elif pc == "tijera":
        tijeraPc()
        actualizarPuntos(jugador, pc)



#creacion de la ventana
ventana = tkr.Tk()
ventana.geometry("900x600")
ventana.configure(bg="#21DCAF")  

def crearImagenPc(imagen):
    canvasPc.create_image(150, 100, anchor=tkr.CENTER, image=imagen)


#puntos________________________________________________________
puntos_jugador_str = tkr.StringVar()
puntos_pc_str = tkr.StringVar()

# Antes de entrar al bucle principal, configura los textos iniciales.
puntos_jugador_str.set(str("0"))
puntos_pc_str.set(str("0"))



# Jugador
puntosJugador = tkr.Label(ventana, textvariable=puntos_jugador_str, font=("Comic Sans Ms", 18), bg="white", width=4)
puntosJugador.place(x=390, y=50)

# Computadora
puntosPc = tkr.Label(ventana, textvariable=puntos_pc_str, font=("Comic Sans Ms", 18), bg="white", width=4)
puntosPc.place(x=440, y=50)


#creacion de widgets 



#imagenes necesarias_____________________________________
# Convertir a formato PhotoImage de Tkinter Jugador
imagen_tkPiedra = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rpiedra.png"))
imagen_tkTijera = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rtijera.png"))
imagen_tkPapel = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rpapel.png"))
# Convertir a formato PhotoImage de Tkinter Pc
imagen_tkPiedrapc = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rpiedrapc.png"))
imagen_tkTijerapc = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rtijerapc.png"))
imagen_tkPapelpc = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/rpapelpc.png"))
#inicial
imagenInicial = ImageTk.PhotoImage(Image.open("C:/Users/Jenny/Desktop/trabajo/proyectos/piedra,papel,tijera/imagenes/load.png"))



def titulos(): 
# Antes de entrar al bucle principal, pide el nombre del usuario
    nombre_usuario = tkr.simpledialog.askstring("Nombre", "Por favor ingresa tu nombre:")
    # Verifica si el usuario canceló el diálogo
    if nombre_usuario is not None:
        # Jugador
        tituloJugador = tkr.Label(ventana,text=f"{nombre_usuario}", font=("Comic Sans Ms", 20), bg="#21DCAF")
        tituloJugador.place(x=150,y=100)
        #titulos ________________________________________________
        tituloComputador = tkr.Label(ventana,text="COMPUTADOR", font=("Comic Sans Ms", 20), bg="#21DCAF")
        tituloComputador.place(x=575,y=100)
    else:
        nombre_usuario = tkr.simpledialog.askstring("Nombre", "Por favor ingresa tu nombre:")
        tituloJugador = tkr.Label(ventana,text=f"{nombre_usuario}", font=("Comic Sans Ms", 20), bg="#21DCAF")
        tituloJugador.place(x=150,y=100)
        #titulos ________________________________________________
        tituloComputador = tkr.Label(ventana,text="COMPUTADOR", font=("Comic Sans Ms", 20), bg="#21DCAF")
        tituloComputador.place(x=575,y=100)

#canvas para mostrar las imagenes necesarias__________________________________________________________
#canvajugador
canvasJg = tkr.Canvas(ventana, width=300, height=200,background="#21DCAF", borderwidth=0, highlightthickness=0)
canvasJg.place(x=50,y=200)
canvasJg.create_image(150, 100, anchor=tkr.CENTER, image=imagenInicial)
#canva pc
canvasPc = tkr.Canvas(ventana, width=300, height=200,background="#21DCAF", borderwidth=0, highlightthickness=0)
canvasPc.place(x=550,y=200)
#inicial
canvasPc.create_image(150, 100, anchor=tkr.CENTER, image=imagenInicial)




#botones________________________
piedra = tkr.Button(ventana, text="Piedra", bg="gray",font=("Arial",17),width=10,height=2, activebackground="black",activeforeground="white")
piedra.place(x=380,y=250)
piedra.bind("<Button-1>", piedraJugador)

papel = tkr.Button(ventana, text="Papel", bg="gray",font=("Arial",17),width=10,height=2,activebackground="black",activeforeground="white")
papel.place(x=380,y=350)
papel.bind("<Button-1>", papelJugador)

tijera = tkr.Button(ventana, text="Tijera", bg="gray",font=("Arial",17),width=10,height=2,activebackground="black",activeforeground="white")
tijera.place(x=380,y=450)
tijera.bind("<Button-1>", tijeraJugador)



titulos()
ventana.mainloop()