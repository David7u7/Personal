from expresiones.expresion import *
import math
from graficas.Arbol import *


class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        valor = self.valor

        # nombre de las etiquetas
        nodo = None

        # validar si es un numero o una Expresion
        if isinstance(self.valor, Expresion):
            valor = self.valor.interpretar()
            nodo = arbol.obtenerUltimoNodo()
        else:
            valor = self.valor
            nodo = arbol.agregarNodo(str(valor))

        print("`" * 20)
        print("tipo: ", self.tipo)
        print("valor: ", valor)
        resultado = None
        #los posibles casos de operaciones trigonometricas
        if self.tipo == "seno":
            resultado = math.sin(valor)
        elif self.tipo  =="coseno":
            resultado = math.cos(valor)
        elif self.tipo  =="tangente":
            resultado = math.tan(valor)
        else:
            print("Error en la operacion")
        # GRAFICAR
        raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
        arbol.agregarArista(raiz, nodo)

        return round(resultado, 2)