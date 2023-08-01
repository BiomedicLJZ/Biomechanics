# Python 101Bases de Python

### 1.1. Variables

#### 1.1.1. Asignación de variables

La asignación de variables en Python se realiza mediante el operador de asignación `=`. Por ejemplo, para asignar el valor 5 a la variable `a` se escribe:

```python
    a = 5
```

Las variables en python no requieren de declaración previa, ni tampoco se especifica el tipo de la variable. Por ejemplo, para asignar el valor 5 a la variable`a` se escribe:

```python
    a = 5
    a = "Hola"
    a = 5.5
    a = True
    a = [1,2,3]
    a = (1,2,3)
    a = {1,2,3}
    a = {'a':1, 'b':2, 'c':3}
```

#### 1.1.2. Asignación múltiple

En Python se puede asignar el mismo valor a varias variables en una sola línea. Por ejemplo, para asignar el valor 5 a las variables `a`, `b` y `c` se escribe:

    a = b = c = 5
en el caso de asignar valores diferentes a las variables, se escribe:

    a, b, c = 1, 2, 3

#### 1.1.3. Eliminación de variables

En Python se puede eliminar una variable mediante la instrucción `del`. Por ejemplo, para eliminar la variable `a` se escribe:

    del a

### 1.2. Tipos de datos

#### 1.2.1. Números

Dentro de python existen dos tipos de números: enteros y flotantes. Los números enteros son aquellos que no tienen parte decimal, por ejemplo, 1, 2, 3, 4, 5, etc. Los números flotantes son aquellos que tienen parte decimal, por ejemplo, 1.0, 2.5, 3.1416, etc. En Python se pueden realizar las operaciones aritméticas básicas: suma, resta, multiplicación y división. Por ejemplo, para sumar 1 y 2 se escribe:

    1 + 2
Para restar 1 y 2 se escribe:

    1 - 2
Para multiplicar 1 y 2 se escribe:

    1 * 2

Para dividir 1 y 2 se escribe:

    1 / 2
Estos operadores también se pueden utilizar con variables. Por ejemplo, para sumar las variables`a` y `b` se escribe:

    a + b

#### 1.2.2. Booleanos

los valores booleanos en Python son `True` y `False`. Estos valores se utilizan para representar verdadero y falso respectivamente. Por ejemplo, para asignar el valor `True` a la variable `a` se escribe:

    a = True

#### 1.2.3. Cadenas

Una cadena es una secuencia de caracteres. En Python se pueden definir cadenas mediante comillas simples o dobles. Por ejemplo, para definir la cadena "Hola" se escribe:

    "Hola"
    'Hola'
Las cadenas también se pueden definir mediante triple comilla simple o doble. Por ejemplo, para definir la cadena "Hola" se escribe:

    """Hola"""
    '''Hola'''

Las cadenas se pueden concatenar mediante el operador `+`. Por ejemplo, para concatenar las cadenas "Hola" y "Mundo" se escribe:

    "Hola" + "Mundo"

Las cadenas se pueden multiplicar por un número entero mediante el operador `*`. Por ejemplo, para multiplicar la cadena "Hola" por 3 se escribe:

    "Hola" * 3

#### 1.2.4. Listas

Una lista es una secuencia de elementos. En Python se pueden definir listas mediante corchetes. Por ejemplo, para definir la lista `[1,2,3]` se escribe:

    [1,2,3]
Las listas pueden contener elementos de diferentes tipos. Por ejemplo, para definir la lista`[1,2,3,"Hola",True]` se escribe:

    [1,2,3,"Hola",True]
Las listas se pueden concatenar mediante el operador`+`. Por ejemplo, para concatenar las listas `[1,2,3]` y `[4,5,6]` se escribe:

    [1,2,3] + [4,5,6]

Esto une las dos listas en una sola lista. Las listas se pueden multiplicar por un número entero mediante el operador `*`. Por ejemplo, para multiplicar la lista `[1,2,3]` por 3 se escribe:

    [1,2,3] * 3

Y esto da como resultado la lista `[1,2,3,1,2,3,1,2,3]`.

### Instrucciones de control

Las estructuras de control funcionan de la misma manera que en otros lenguajes de programación. En Python se utilizan las siguientes estructuras de control:

* `if` - `elif` - `else`
* `for` - `while` - `break` - `continue`
* `match` - `case`[^1]
* `try` - `except` - `finally`

### Librerías

Las librerías en Python se importan mediante la instrucción `import`. Por ejemplo, para importar la librería `math` se escribe:

    import math
Para importar una función específica de una librería se escribe:

    from math import sin
Para importar todas las funciones de una librería se escribe:

    from math import *
Para importar una librería con un alias se escribe:

    import math as m

Cada una de estas maneras de importar librerías se puede combinar con la instrucción `as` para asignar un alias a la librería. Por ejemplo, para importar la librería `math` con el alias `m` se escribe:

    import math as m
    import math as m
    from math import sin as s
    from math import * as m

### Funciones y métodos

Las funciones en Python se definen mediante la instrucción `def`. Por ejemplo, para definir la función `suma` que recibe dos parámetros `a` y `b` y retorna la suma de estos dos parámetros se escribe:

    def suma(a,b):
        return a + b
Para llamar a la función`suma` se escribe:

    suma(1,2)

Para definir una función que no recibe parámetros se escribe:

    def hola():
            print("Hola")
Cuando llamamos una funcion perteceinte a una libreria, se le llama metodo. Por ejemplo, para llamar al método`sin` de la librería `math` se escribe:

    math.sin(1)
para llamar al metodo`sin` de la libreria `math` con el alias `m` se escribe:

    m.sin(1)

### Clases

Una clase es un tipo de dato definido por el usuario. En Python se pueden definir clases mediante la instrucción `class`. Por ejemplo, para definir la clase `Punto` que tiene dos atributos `x` e `y` se escribe:

    class Punto:
        def__init__(self,x,y):
            self.x = x
            self.y = y
En una clase empezamos por definir características de la clase mediante atributos. En este caso, la clase `Punto` tiene dos atributos `x` e `y`. Luego, definimos el método `__init__` que es el método que se ejecuta cuando se crea una instancia de la clase. En este caso, el método `__init__` recibe dos parámetros `x` e `y` y asigna estos valores a los atributos `x` e `y` de la clase. Para crear una instancia de la clase `Punto` se escribe:

    p = Punto(1,2)
Para acceder a los atributos de una instancia de una clase se escribe:

    p.x
        p.y
Para definir métodos en una clase se escribe:

    class Punto:
                def__init__(self,x,y):
                    self.x = x
                    self.y = y
                def suma(self):
                    return self.x + self.y
Un metodo es una funcion que pertenece a una clase. Para llamar a un metodo se escribe:

    p.suma()
Una clase entonces se vuelve una herramienta muy poderosa para definir tipos de datos personalizados. Por ejemplo, para definir la clase`Punto` que tiene dos atributos `x` e `y` y un método `suma` que retorna la suma de los atributos `x` e `y` se escribe:

    class Punto:
        def__init__(self,x,y):
            self.x = x
            self.y = y
        def suma(self):
            return self.x + self.y
Para crear una instancia de la clase `Punto` se escribe:

    p = Punto(1,2)
Para llamar al método`suma` de la instancia `p` se escribe:

    p.suma()

### Herencia

La herencia se define como la capacidad de una clase de heredar atributos y métodos de otra clase. En Python se puede definir herencia mediante la instrucción `class`. Por ejemplo, para definir la clase `Punto` que tiene dos atributos `x` e `y` y un método `suma` que retorna la suma de los atributos `x` e `y` y luego definir la clase `Punto3D` que hereda de la clase `Punto` y tiene un atributo `z` se escribe:

    class Punto:
        def__init__(self,x,y):
            self.x = x
            self.y = y
        def suma(self):
            return self.x + self.y
    class Punto3D(Punto):
        def __init__(self,x,y,z):
            Punto.__init__(self,x,y)
            self.z = z
En este caso, la clase `Punto3D` hereda de la clase `Punto` y tiene un atributo `z`. Para crear una instancia de la clase `Punto3D` se escribe:

    p = Punto3D(1,2,3)
Para llamar al método`suma` de la instancia `p` se escribe:

    p.suma()
Para acceder al atributo`z` de la instancia `p` se escribe:

    p.z

### Polimorfismo

El polimorfismo se define como la capacidad de una clase de tener métodos con el mismo nombre pero con diferentes comportamientos. En Python se puede definir polimorfismo mediante la herencia. Por ejemplo, para definir la clase `Punto` que tiene dos atributos `x` e `y` y un método `suma` que retorna la suma de los atributos `x` e `y` y luego definir la clase `Punto3D` que hereda de la clase `Punto` y tiene un atributo `z` y un método `suma` que retorna la suma de los atributos `x`, `y` e `z` se escribe:

    class Punto:
        def__init__(self,x,y):
            self.x = x
            self.y = y
        def suma(self):
            return self.x + self.y
    class Punto3D(Punto):
        def __init__(self,x,y,z):
            Punto.__init__(self,x,y)
            self.z = z
        def suma(self):
            return Punto.suma(self) + self.z
Si bien pareciera que el método `suma` de la clase `Punto3D` tiene el mismo nombre que el método `suma` de la clase `Punto`, en realidad tienen comportamientos distintos. Para crear una instancia de la clase `Punto3D` se escribe:

    p = Punto3D(1,2,3)
Para llamar al método`suma` de la instancia `p` se escribe:

    p.suma()

### Encapsulamiento

EL encapsulamiento se define como la capacidad de una clase de ocultar sus atributos y métodos. En Python se puede definir encapsulamiento mediante la definición de atributos y métodos privados. Por ejemplo, para definir la clase `Punto` que tiene dos atributos `x` e `y` y un método `suma` que retorna la suma de los atributos `x` e `y` y luego definir la clase `Punto3D` que hereda de la clase `Punto` y tiene un atributo `z` y un método `suma` que retorna la suma de los atributos `x`, `y` e `z` se escribe:

    class Punto:
        def__init__(self,x,y):
            self.__x = x
            self.__y = y
        def __suma(self):
            return self.__x + self.__y
    class Punto3D(Punto):
        def __init__(self,x,y,z):
            Punto.__init__(self,x,y)
            self.__z = z
        def suma(self):
            return Punto.__suma(self) + self.__z
En este caso, los atributos `x`, `y` y `z` son privados y no pueden ser accedidos desde fuera de la clase. Para crear una instancia de la clase `Punto3D` se escribe:

    p = Punto3D(1,2,3)
Para llamar al método`suma` de la instancia `p` se escribe:

    p.suma()

### Ejemplo

```python
class Punto:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def __suma(self):
        return self.__x + self.__y
class Punto3D(Punto):
    def __init__(self,x,y,z):
        Punto.__init__(self,x,y)
        self.__z = z
    def suma(self):
        return Punto.__suma(self) + self.__z
p = Punto3D(1,2,3)
```

### Principales librerias del curso

#### Documentación

La documentación de una librería es un conjunto de páginas web que contiene información sobre la librería. La documentación de una librería es muy importante para entender su funcionamiento. La documentación de una librería se puede consultar en la página web de la librería.
No todas las librerías tienen documentación tal clara, pero es importante consultarla para entender el funcionamiento de las librerías.

#### [Numpy][https://numpy.org/doc/stable/](2)

Numpy es una librería de Python que permite realizar operaciones matemáticas sobre vectores y matrices.
Esta libreria tiene dos alias comunes: `np` y `nmpy`.

 Para importar la librería se escribe:

```python
import numpy as np
```

Para crear un vector de ceros de tamaño 5 se escribe:

```python
v = np.zeros(5)
```

Para crear una matriz de ceros de tamaño 5x5 se escribe:

```python
m = np.zeros((5,5))
```

Para crear un vector de unos de tamaño 5 se escribe:

```python
v = np.ones(5)
```

Para crear una matriz de unos de tamaño 5x5 se escribe:

```python
m = np.ones((5,5))
```

Es posible crear vectores y matrices con valores aleatorios. Para crear un vector de valores aleatorios de tamaño 5 se escribe:

```python
v = np.random.rand(5)
```

Tambien pueden definir cada valor del vector de forma independiente. Para crear un vector de valores aleatorios de tamaño 5 se escribe:

```python
v = np.array([0.1,0.2,0.3,0.4,0.5])
```

Estas son algunas de las funciones que se pueden utilizar con la librería numpy. Para conocer todas las funciones que se pueden utilizar con la librería numpy se puede consultar la documentación de la librería.

#### [Matplotlib](https://matplotlib.org/stable/index.html)

Matplotlib es una librería de Python que permite realizar gráficos. Esta libreria tiene dos alias comunes: `plt` y `matplotlib`. Está basada en la librería de gráficos de Matlab. Para importar la librería se escribe:

```python
import matplotlib.pyplot as plt
```

Como matlab es recomendable crear primero una figura y luego agregar los gráficos a la figura. Para crear una figura se escribe:

```python
fig = plt.figure()
```

Para agregar un gráfico a la figura se escribe:

```python
fig.plot(x,y)
```

Donde `x` e `y` son los vectores que contienen los valores de las coordenadas `x` e `y` del gráfico. Para mostrar la figura se escribe:

```python
fig.show()
```

Estas son algunas de las funciones que se pueden utilizar con la librería matplotlib. Para conocer todas las funciones que se pueden utilizar con la librería matplotlib se puede consultar la documentación de la librería.

#### [Scipy](https://docs.scipy.org/doc/scipy/)

Scipy es una librería de Python que contiene funciones matemáticas y científicas. Esta libreria tiene dos alias comunes: `sp` y `scipy` Para importar la librería se escribe:

```python
import scipy as sp
```

Para importar una función de la librería se escribe:

```python
from scipy import function
```

Donde `function` es el nombre de la función que se quiere importar. Estas son algunas de las funciones que se pueden utilizar con la librería scipy. Para conocer todas las funciones que se pueden utilizar con la librería scipy se puede consultar la documentación de la librería.

#### [Jupyter](https://jupyter.org/)

Jupyter es una librería de Python que permite crear documentos interactivos. Esta libreria mas que una librería es un programa que se instala en el computador. Para instalar jupyter se escribe en la terminal:

```bash
pip install jupyter o mamba install jupyter
```

Esta una vez instalada nos permite trabajar cuadernos interactivos. Para crear un cuaderno interactivo se crea un archivo en vscode con la extension `.ipynb`.

Recuerden que es importante consultar la documentación de las librerías para conocer todas las funciones que se pueden utilizar con cada librería.

[^1]: Esta estructura de control solo existe a partir de python 3.10

[^2]: Recuerden que todos los titulos de las librerias son links a la documentación de la librería

