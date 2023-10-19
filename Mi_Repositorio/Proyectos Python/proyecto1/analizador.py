from expresiones.trigonometricas import ExpresionTrigonometrica
from expresiones.aritmeticas import ExpresionAritmetica
from collections import namedtuple
from graficas.Arbol import *

Token = namedtuple("Token", ["value", "line", "col"])


line = 1
col = 1

tokens = [] 
errores = []


configuracion = {
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}


#identificador de cadenas por medio de las comillas
def tokenize_string(input_str, i):
    token = ""
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("String no cerrado", token)


#identificador de digitos (numero)
def tokenize_number(input_str, i):
    token = ""
    isDecimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == ".":
            token += char
            i += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(token), i]
    return [int(token), i]



#analizador de cada uno de los casos
def tokenize_input(input_str):
    
    numero = 0
    global line, col, tokens
    i = 0
    while i < len(input_str):
        char = input_str[i]
        #espacios en blanco
        if char.isspace():
            if char == "\n":
                line += 1
                col = 1
            elif char == "\t":
                col += 4
            # si es un espacio
            else:
                col += 1
            # incrementar el indice
            i += 1
            #cadenas de texto con doble comilla
        elif char == '"':
            string, pos = tokenize_string(input_str[i + 1:], i)
            col += len(string) + 1
            i = pos + 2
            token = Token(string, line, col)
            tokens.append(token)
            #simbolos como parentesis, llaves etc
        elif char in ["{", "}", "[", "]", ",", ":"]:
            col += 1
            i += 1
            token = Token(char, line, col)
            tokens.append(token)
            #numeros
        elif char.isdigit():
            number, pos = tokenize_number(input_str[i:], i)
            col += pos - i
            i = pos
            token = Token(number, line, col)
            tokens.append(token)
        else:
            numero = len(errores) + 1
            error = {  #diccionario para los errores
                "numero": str(numero),
                "descripcion": { #diccionario anidado
                    "lexema": char,
                    "tipo": "error lexico",
                    "columna": col,
                    "fila": line,
                },
            }
            errores.append(error)
            i += 1
            col += 1 





# crear las instrucciones a partir de los tokens
def get_instruccion():
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        #print("VALUE: ", token)
        if token.value == "operacion":
            # eliminar el :
            tokens.pop(0)
            operacion = tokens.pop(0).value
        elif token.value == "valor1":
            # eliminar el :
            tokens.pop(0)
            value1 = tokens.pop(0).value
            if value1 == "[":
                value1 = get_instruccion()
        elif token.value == "valor2":
            # eliminar el :
            tokens.pop(0)
            value2 = tokens.pop(0).value
            if value2 == "[":
                value2 = get_instruccion()
        elif token.value in ["texto", "fondo", "fuente", "forma"]:
            tokens.pop(0)
            configuracion[token.value] = tokens.pop(0).value
        else:
            #depurar que si se este tomando lo que se necesita y no los demas tokens
            print("\033[1;31;40m Error: token desconocido:", token, "\033[0m")


        if operacion and value1 and value2:
            return ExpresionAritmetica(operacion, value1, value2, line, col)
        if operacion and operacion in ["seno"] and value1:
            return ExpresionTrigonometrica(operacion, value1, line, col)
        if operacion and operacion in ["coseno"] and value1:
            return ExpresionTrigonometrica(operacion, value1, line, col)
        if operacion and operacion in ["tangente"] and value1:
            return ExpresionTrigonometrica(operacion, value1, line, col)


    return None



def create_instructions():
    global tokens
    global arbol
    instrucciones = []
    while tokens:
        instruccion = get_instruccion()
        if instruccion:
            instrucciones.append(instruccion)
    arbol.agregarConfiguracion(configuracion)
    return instrucciones


def analizar(entrada):
    tokenize_input(entrada)
    #arbol.dot.clear()
    with open("graficas/Arbol.dot", "w") as f:
        pass  # Esto abre el archivo y lo vacía, ya que no hay nada en el bloque

    
    arbol.agregarConfiguracion(configuracion)
    instrucciones = create_instructions() 
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpretar())

    return arbol

#conexion con el analizador
def mostrar_elementos():
    resultados = []
    for i in tokens:
        resultados.append(str(i))
    return '\n'.join(resultados)



#conexion con los errores
def mostrar_errores():
    return {"errores": errores}
