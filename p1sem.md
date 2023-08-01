# Practica 1

# Seminario de Análisis de Movimiento

# 2023A

# 1. Objetivos

# 2. Desarrollo

## 2.1. Bases de python y numpy

Comenzaremos con un ejemplo de como se puede utilizar python para realizar operaciones matemáticas. Para ello, se importa la librería numpy, la cual contiene funciones matemáticas y operaciones de álgebra lineal.

```python
import numpy as np
```

Una vez importada la librería, se puede utilizar para realizar operaciones matemáticas. Por ejemplo, se puede calcular el seno de un ángulo.

```python
np.sin(4)
```

```python
-0.7568024953079282
```

También se puede calcular el coseno de un ángulo.

```python
np.cos(4)
```

```python
-0.6536436208636119
```

Podemos calcular otro tipo de operaciones matemáticas, como la raíz cuadrada de un número.

```python
np.sqrt(4)
```

```python
2.0
```

También podemos calcular la potencia de un número.

```python
np.power(4,2)
```

```python
16.0
```

También podemos calcular la exponencial de un número.

```python
np.exp(4)
```

```python
54.598150033144236
```

También podemos calcular el logaritmo de un número.

```python
np.log(4)
```

```python
1.3862943611198906
```

Esta libreria también nos permite realizar operaciones de álgebra lineal. Por ejemplo, podemos calcular la inversa de una matriz.

```python
A = np.array([[1,2],[3,4]])
A_inv = np.linalg.inv(A)
A_inv
```

```python
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
```

Entonces como pueden ver en el ejemplo anterior, se puede utilizar python para realizar operaciones matemáticas y de álgebra lineal. Siendo una herramienta muy útil para realizar cálculos numéricos.

Ahora en nuestra materia uno de los temas que mas vamos a estudiar es el trabajo con señales EMG, por lo que es importante que sepan como trabajar con estas señales. Para ello, se utilizará la librería matplotlib, la cual nos permite graficar señales.
Para poder graficar una señal necesitamos dos vectores, uno con los valores de la señal y otro con los valores del tiempo. Por ejemplo, si tenemos una señal de 10 segundos con una frecuencia de muestreo de 1000 Hz, entonces tendremos 10000 muestras(porque tenemos 1000 muestras por segundo). Por lo que tendremos dos vectores, uno con 10000 muestras y otro con 10000 muestras.
Numpy nos permite crear vectores de manera muy sencilla. Por ejemplo, si queremos crear un vector de tiempo de 10 segundos con una frecuencia de muestreo de 1000 Hz, entonces podemos hacer lo siguiente.

```python
import numpy as np
t = np.arange(0,10,0.001)
```

```python
array([0.000e+00, 1.000e-03, 2.000e-03, ..., 9.997e+00, 9.998e+00,
       9.999e+00])
```

Como pueden ver, numpy nos permite crear vectores de manera muy sencilla. Ahora, para poder crear un vector con los valores de la señal, necesitamos crear una función que nos permita calcular los valores de la señal. Por ejemplo, si queremos crear una señal senoidal, entonces podemos hacer lo siguiente.

```python
import numpy as np
f = 10 # Frecuencia de la señal
A = 2 # Amplitud de la señal
fs = 1000 # Frecuencia de muestreo
t = np.arange(0,10,1/fs) # Vector de tiempo
s = A*np.sin(2*np.pi*f*t) # Vector de la señal
```

```python
array([ 0.00000000e+00,  1.99983383e-01,  3.99866647e-01, ...,
       -3.99866647e-01, -1.99983383e-01, -2.44929360e-16])
```

Ahora que ya tenemos los vectores de tiempo y de la señal, podemos graficar la señal. Para ello, se importa la librería matplotlib.

```python
import matplotlib.pyplot as plt
```

Ahora, para poder graficar la señal, se utiliza la función plot de matplotlib.

```python
plt.figure()
plt.plot(t,s)
plt.show()
```

Y aquí podríamos ver la señal senoidal que creamos.(Les toca a ustedes hacerlo)
Una vez que ya pueden graficar señales pueden guardarlas como imagenes. Para ello, se utiliza la función savefig de matplotlib.

```python
plt.figure()
plt.plot(t,s)
plt.savefig('senoidal.png')
```

y la imagen se guardará en la misma carpeta donde se encuentra el archivo de python.

Es posible cambiar los detalles de la visualizacion de la grafica como el tamaño de la grafica, el color de la linea, el grosor de la linea, el titulo de la grafica, el titulo de los ejes, etc. Para ello, se utiliza la función figure de matplotlib.

```python
plt.figure(figsize=(10,5))
plt.plot(t,s,color='red',linewidth=2,linestyle='--')#Tamaño de la grafica, color de la linea, grosor de la linea, estilo de la linea
plt.title('Señal senoidal')#Titulo de la grafica
plt.xlabel('Tiempo (s)')#Titulo del eje x
plt.ylabel('Amplitud (V)')#Titulo del eje y
plt.savefig('senoidal.png')#Guardar la imagen
```

Este codigo crearía una grafica de tamaño 10x5, con una linea roja de grosor 2 y estilo guiones, con un titulo de la grafica, un titulo de los ejes y guardaria la imagen en la misma carpeta donde se encuentra el archivo de python.

## Ejercicio

1. Crear una grafica de una señal senoidal con una frecuencia que seleccionen ustedes y una amplitud de 2 unidades. Guardar la imagen de la grafica como senoidal.png
2. Crear una figura con 4 graficas, de señales senoidales con diferentes frecuencias y amplitudes. Guardar la imagen de la grafica como senoidales.png
3. Crear una figura con 1 grafica pero 4 señales senoidales con diferentes frecuencias y amplitudes sobrepuestas. Guardar la imagen de la grafica como senoidales2.png
