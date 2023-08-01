# Proyecto Final

## Procesamiento de Archivos 3D

### Parte 1

Lectura de archivos `.c3d` y visualización de los datos. Para esta parte deberan cargar los archivos `.c3d` que les fueron proporcionados y deberan analizar los datos que contienen. Deberan responder las siguientes preguntas:

1. ¿Qué tipo de datos contiene el archivo?
2. ¿Qué tipo de movimiento representa?
3. ¿Cuántos marcadores contiene el archivo?
4. ¿Cuántos frames contiene el archivo?

<mark>Para la carga de estos archivos será el único momento en que se podrá utilizar la librería `ktk`[^1]  

[^1]:https://kineticstoolkit.uqam.ca/doc/index.php "Kinetics Toolkit"

Una vez cargados los archivos les recomiendo utilizar la librería `pandas`[^2] para visualizar los datos.

[^2]:https://pandas.pydata.org/ "Pandas"

### Parte 2

Una vez que se ha cargado el archivo `.c3d` y se ha visualizado la información, se deberá realizar un procesamiento de los datos para obtener la posición de los marcadores en cada frame. Estos deberán ser preparados para graficarse en un entorno 3D.

### Parte 3

Una vez que se han obtenido las posiciones de los marcadores en cada frame, se deberá crear un entorno 3D en el cual se visualice el movimiento.

### Parte 4

Una vez que se ha creado el entorno 3D, se deberá crear una animación del movimiento.

Para esto les recomiendo utilizar la librería `matplotlib`[^2] con su módulo `animation`[^3].

[^2]:https://matplotlib.org/ "Matplotlib"
[^3]:https://matplotlib.org/api/animation_api.html "Matplotlib Animation"

### Parte 5

Una vez que se ha terminado con el entorno 3D, se deberá crear guardar el movimiento en un archivo `.gif` o `.mp4`.

Para esto les recomiendo utilizar la libreria `FFmpeg`[^4].

[^4]:https://ffmpeg.org/ "FFmpeg"

### Parte 6

Entregar por último en un cuaderno de jupyter los resultados obtenidos, las conclusiones y su opinión sobre el proyecto y el semestre.
