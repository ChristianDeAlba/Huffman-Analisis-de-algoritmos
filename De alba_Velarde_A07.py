import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# Funcion para leer el contenido de un archivo y mostrar el numero de caracteres
def LeerArchivo(archivo):
    # Abrir el archivo en modo lectura
    with open(archivo, "r") as archivo:
        # Leer el contenido del archivo
        datos = archivo.read()
        # Contar el numero de caracteres en el archivo
        contador_caracteres = len(datos)
        # Mostrar el numero de caracteres
        contador_label.config(text=f"Caracteres en el archivo: {contador_caracteres}")
        # Imprimir el contenido del archivo
        print(datos)

# Funcion para buscar un archivo
def BuscarArchivo():
    # Abrir el cuadro de dialogo para seleccionar un archivo
    archivo = filedialog.askopenfilename()
    # Limpiar y mostrar la ruta del archivo seleccionado en el campo de entrada
    archivo_entrada.delete(0, tk.END)
    archivo_entrada.insert(0, archivo)
    # Llamar a la funcion LeerArchivo() para mostrar el contenido del archivo
    LeerArchivo(archivo)

# Funcion para la compresion de archivos 
def Comprimir():
    input_file = archivo_entrada.get()
    if not input_file:
        return

# Funcion para la descompresion de archivos 
def Descomprimir():
    input_file = archivo_entrada.get()
    if not input_file:
        return

# Crear la ventana principal de la aplicacion
root = tk.Tk()
root.title("Compresor de Archivos Huffman")
root.geometry("777x555")

# Crear un marco principal dentro de la ventana
mainframe = tk.Frame(root)
mainframe.pack(padx=8, pady=8)

# Etiqueta para mostrar el directorio del Archivo
archivo_ventana = tk.Label(mainframe, text="Archivo:")
archivo_ventana.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada para mostrar la ruta del archivo seleccionado
archivo_entrada = tk.Entry(mainframe, width=50)
archivo_entrada.grid(row=0, column=1, padx=10, pady=10)

# Botón para abrir el cuadro de diálogo y buscar un archivo
buscar_boton = tk.Button(mainframe, text="Examinar", command=BuscarArchivo)
buscar_boton.grid(row=0, column=2, padx=10, pady=10)

# Botón para iniciar la compresión de archivos
comprimir_boton = tk.Button(mainframe, text="Comprimir", command=Comprimir)
comprimir_boton.grid(row=1, column=0, columnspan=3, pady=10)

# Botón para iniciar la descompresión de archivos
descomp_boton = tk.Button(mainframe, text="Descomprimir", command=Descomprimir)
descomp_boton.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Muestra el contador de caracteres
contador_label = tk.Label(mainframe, text="")
contador_label.grid(row=3, column=0, columnspan=3)

# Inicia el bucle de la interface
root.mainloop()
