# Huffman-Analisis-de-algoritmos
Este es una actividad para la clase de Análisis de algoritmos la cual se hará un programa para comprimir y descomprimir utilizando el arbol de Huffman

Análisis de algoritmia
De Alba Velarde Christian Moises
López Arce Delgado Jorge Ernesto	 								 
Sotelo Rodríguez Moises
D01 24A
23/04/2024


Introducción

El presente reporte aborda el desarrollo de un programa en Python para la creación de un compresor de archivos utilizando el algoritmo de Huffman. El propósito de este proyecto es proporcionar una herramienta simple y efectiva para comprimir y descomprimir archivos de texto, aprovechando las ventajas de la codificación de Huffman para reducir el tamaño de los archivos.
Objetivos

El objetivo principal es implementar la funcionalidad de compresión y descompresión de archivos utilizando el algoritmo de Huffman. Así como mejorar la interfaz de usuario para proporcionar una interface intuitiva así como comprimir y descomprimir archivos grandes de manera eficiente.

Desarrollo

Funciones:
LeerArchivo(archivo): Esta función recibe la ruta de un archivo como entrada, lee su contenido y muestra el número de caracteres en el archivo. Utiliza la función open() para abrir el archivo en modo lectura y archivo.read() para leer su contenido. Luego, cuenta el número de caracteres utilizando la función len() y actualiza una etiqueta en la GUI con esta información.
BuscarArchivo(): Esta función abre un cuadro de diálogo para que el usuario pueda seleccionar un archivo. Utiliza filedialog.askopenfilename() para abrir el cuadro de diálogo y archivo_entrada.delete() y archivo_entrada.insert() para mostrar la ruta del archivo seleccionado en un campo de entrada en la GUI.
Comprimir(): Función destinada a implementar la lógica de compresión de archivos. Actualmente está definida, pero sin funcionalidad implementada.
Descomprimir(): Función destinada a implementar la lógica de descompresión de archivos. Al igual que la función Comprimir(), está definida pero sin funcionalidad implementada.
Interfaz de Usuario:
Se utiliza Tkinter para crear una interfaz simple que incluye etiquetas, campos de entrada y botones.
Se muestra la etiqueta "Archivo:" seguida de un campo de entrada donde se muestra la ruta del archivo seleccionado.
Un botón "Examinar" permite al usuario seleccionar un archivo mediante un cuadro de diálogo.
Botones adicionales para las funciones de compresión y descompresión están presentes en la GUI.


Conclusiones
Para esta primera parte lo que se entrega es la parte de interface grafica ya en esta parte se hizo todos los botones así como también se hizo un una manera mas estética mejor para un último usuario así como se agregó un contador de caracteres, en el siguiente avance de la actividad se realizaras la parte de backend la cual se utilizara árbol de huffman para poder comprimir y descomprimir los archivos seleccionados
