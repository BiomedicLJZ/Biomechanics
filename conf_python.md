# Configuración de Python usando Mamba

## Python
Como ya se explicó Python es un lenguaje interpretado de alto nivel de codigo abierto y multiplataforma. En este curso se usará la versión 3.8. y para instalarlo se utilizara el gestor de mamba el cual es un gestor de paquetes y entornos virtuales para Python basado en Anaconda y Conda.

## Entorno 
Un entorno es un directorio que contiene una colección de paquetes de Python específicos para un proyecto. Los entornos aislados son una característica importante de Python que permite que los proyectos se ejecuten en diferentes versiones de Python y diferentes conjuntos de paquetes sin interferir entre sí. Así si un proyecto requiere una versión específica de un paquete, no se verá afectado por la instalación de una versión diferente en otro proyecto.

## Anaconda 
Anaconda es una distribución de Python que incluye más de 1.500 paquetes de código abierto populares. Anaconda simplifica la gestión de paquetes y entornos. Anaconda incluye el gestor de paquetes y entornos Conda. el cual está basado en el gestor de paquetes de Python y el administrador de entornos virtual pip. utilizando su propia base de datos de paquetes. Conda puede instalar paquetes de Python de la propia base de datos de Conda, de repositorios de Python o de repositorios de terceros. Conda también puede crear y administrar entornos virtuales. 
## Mamba 
Mamba es un gestor de paquetes para python basado en Anaconda el cual se caracteriza por una mejor gestion de paquetes y una mayor velocidad de instalación. así como de mayor claridad en los mensajes del gestor, errores y advertencias. Por esto es que fue el gestor de paquetes elegido para este curso.
Para la instalacion de mamba y la configuracion de python se debe seguir los siguientes pasos:
* Descargar el instalador de mamba desde el siguiente link: [Mamba PYPY3](https://github.com/conda-forge/miniforge#mambaforge) recuerden descargar la version con PYPY3 correspondiente a su sistema operativo (La mayoria de los casos es windows 64 bits)
* Una vez descargado el instalador ejecutarlo y seguir los pasos de instalacion. recordando instalarlo en una ruta sin espacios y sin caracteres especiales. en la selección de instalacion ![image](mamba1.png)
* Una vez seleccionada la opcion de añadir al path (*Si se que el mismo instalador dice que no es algo recomendado está bien*) pueden sar siguiente y proceder con la instalacion. 
* Una vez terminada la instalacion deberían ver una ventana como la siguiente ![image](mamba2.png)
### Configuración de Python
Una vez instalado mamba podemos proceder a configurar python. Para esto abrimos la terminal de windows, cmd o powershell y escribimos el siguiente comando:
```bash
mamba -h
```
Esto nos debería mostrar una lista de comandos que podemos usar con mamba. En este caso nos interesa el comando create el cual nos permite crear un entorno virtual. Para crear un entorno virtual escribimos el siguiente comando:
```bash
mamba create -n nombre_entorno python=3.8
```
Esto nos creará un entorno virtual con el nombre que le hayamos puesto y con la versión de python que le hayamos indicado. Para activar el entorno virtual escribimos el siguiente comando:
```bash
mamba activate nombre_entorno
```
Para verificar que el entorno virtual se ha activado correctamente debemos ver que el nombre del entorno virtual aparece entre paréntesis al inicio de la linea de comandos. ![image](mamba3.png)
Ahora que el entorno está activado podemos instalar los paquetes que necesitemos para trabajar en nuestro proyecto. Para instalar un paquete escribimos el siguiente comando:
```bash
mamba install nombre_paquete
```
algunos de los paquetes mas conocidos de python y que veremos en este curso son: 
* Numpy
* Jupyter
* Pandas
* Matplotlib
* Scipy
Estos paquetes cumplen las siguientes funciones:
Numpy es un paquete que nos permite trabajar con arreglos multidimensionales y matrices. Pandas es un paquete que nos permite trabajar con datos estructurados. Matplotlib es un paquete que nos permite crear gráficos. Scipy es un paquete que nos permite trabajar con funciones matemáticas y estadísticas. Jupyter es un paquete que nos permite crear notebooks de python en los cuales podemos escribir código, texto y gráficos así como tambien gestiona kernels de python interactivos.
Para desactivar el entorno virtual una vez terminemos de trabajar escribimos el siguiente comando:
```bash
mamba deactivate
```
Para eliminar un entorno virtual escribimos el siguiente comando:
```bash
mamba remove -n nombre_entorno --all
```
# Vscode
Visual Studio Code es un Entorno de Desarrollo Integrado IDE por sus siglas en inglés que permite el desarrollo de software en muchos lengajes de programación. Es un software de código abierto desarrollado por Microsoft para Windows, Linux y macOS. Es multiplataforma y multi lenguaje. Es un editor de código fuente ligero pero potente que incluye soporte para depuración, control de versiones Git integrado, resaltado de sintaxis, finalización inteligente de código, snippets y refactoring. Todo esto lo hace un IDE muy potente y fácil de usar. Para descargarlo pueden ir al siguiente link: [Vscode](https://code.visualstudio.com/download)
Una vez descargado e instalado podemos proceder a instalar los siguientes plugins:
* Python
* Jupyter
* Jupyter powertoys (Recomendado mas no obligatorio)

Para instalar los plugins podemos ir a la pestaña de extensiones y buscar los plugins que queremos instalar. ![image](vscode1.png)
Una vez instalados los plugins podemos proceder a crear un proyecto de python. Para esto podemos ir a la pestaña de archivos y abrir una carpeta en la cual almacenaremos nuestro proyecto. ![image](vscode2.png)
Una vez aquí creamos un archivo con extensión .py y escribimos el siguiente código:
```python
print("Hola Mundo")
```
Para ejecutar el código podemos ir a la pestaña de terminal y escribir el siguiente comando:
```bash
python nombre_archivo.py
```
Esto nos debería mostrar el siguiente mensaje en la terminal: ![image](vscode3.png)

Ahora, esta no es la manera en la que vamos a trabajar nuestros scripts de python durante este curso. Para este curso usaremos la herramienta de ventanas interactivas de python que está encluida en las extensiones de jupyter. Para abrir esta herramienta daremos click derecho sobre nuestro codigo y seleccionaremos la opcion *Run Current File in Interactive Window*. lo que nos debería mostrar una ventana como la siguiente: ![image](vscode4.png) En caso de requerir hacer descargas para poder ejecutar el codigo como es debido el IDE nos lo notificará como vieron en la figura y podran ejecutarlo sin problemas. 
Una vez que la ventana Interactiva se abre podremos ejecutar la linea de codigo que escribimos anteriormente y veremos el resultado en la ventana interactiva. ![image](vscode5.png)
Estas ventanas interactivas son muy útiles para poder ejecutar codigo de python y ver los resultados de manera interactiva. En este curso usaremos estas ventanas interactivas para ejecutar los scripts de python que veremos en cada clase. Además de simplificar mucho los procesos para ver los resultados de nuestros scripts de python sin tener que ejecutarlos en la terminal de comandos o en la consola de python.
Nota importante: Si no se ejecuta el codigo de manera correcta es posible que sea necesario seleccionar el kernel de python correspondiente a nuestro entorno virtual. Para esto podemos seleccionarlo usando la paleta de comandos de vscode. Para abrir la paleta de comandos podemos usar el atajo de teclado *Ctrl + Shift + P* o podemos ir a la pestaña de *View* y seleccionar la opcion *Command Palette*. Una vez abierta la paleta de comandos escribimos el siguiente comando:
```bash
Python: Select Interpreter
```
Con esto nos debería aparecer una lista de kernels de python disponibles. ![image](vscode6.png)
Seleccionamos el kernel de python correspondiente a nuestro entorno virtual y listo. Ahora podemos ejecutar nuestro codigo sin problemas.
### Una vez hecho esto están listos para comenzar el curso.