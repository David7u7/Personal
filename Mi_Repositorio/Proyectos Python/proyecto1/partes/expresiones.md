## Expresiones

Es aca en donde se crearan los objetos expresion aritmetica o expresion trigonometrica, las cuales identifican las operaciones a realizar en el archivo provisto.
### Trigonometricas

En el modulo trigonometricas, se tiene la funcion en cargada de ser el metodo constructor  tomando como atributos el valor, el tipo, la linea y columna.


```python
def __init__(self, tipo, valor, linea, columna):
```


Se tiene tambien la funcion: 

```python
 def interpretar(self):
```
En la cual se verificara que haya una instancia de la clase y si lo es la interpretara, efectuando la ooperacion, sino lo tomara como un numero.

Luego se presentaran los posibles casos de tipo que serian, senos, cosenos o tangentes.

Procederá a graficar los nodos con su respectiva arista y retornara el resultado de la operacion con 2 decimales.

### Aritmeticas 

```python
def __init__(self, tipo, valor1, valor2, linea, columna):
```
Se crea el metodo constructor de la clase la cual sera necesaria para procesar las operaciones y determinar si es una operacion aritmetica, funciona de la misma manera que la clase trigonometricas, sin embargo aca se validaran dos valores, verificando que sean una instanci a para interpretarla. Se declaran asi mismo las operaciones validas en esta instancia y de no ser una de estas, se retornará un error en consola.

Se grafica tambien el respectivo arbol con sus aristas y nodos correspondientes tomando en cuenta que se necesitan por lo menos dos valores 

## Expresion
Se encarga de establecer la plantilla para uso de clase abstracta

### Navegacion
- [Ir a la Sección de analizador](../partes/analizador.pdf)

- [Ir a la Sección de graficas](../partes/grafo.pdf)

- [Ir a la Sección de la interfaz](../partes/interfaz.pdf)