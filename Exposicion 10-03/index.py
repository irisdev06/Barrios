# ----------------------------
# 1. Manejo de Archivos de Texto
# ----------------------------

print("### Manejo de Archivos de Texto ###")

# Entrada: Leer un archivo de texto
print("Leyendo archivo de texto ('entrada.txt'):")
try:
    with open("entrada.txt", "r") as archivo:  # Abrimos el archivo en modo lectura
        for linea in archivo:  # Leemos el archivo línea por línea
            print(linea.strip())  # Imprimimos cada línea eliminando los saltos de línea
except FileNotFoundError:
    print("Error: El archivo 'entrada.txt' no se encuentra.")

# Salida: Escribir en un archivo de texto
print("\nEscribiendo en archivo de texto ('salida.txt'):")
with open("salida.txt", "w") as archivo:  # Abrimos el archivo en modo escritura
    archivo.write("Hola, este es un mensaje de salida.\n")  # Escribimos en el archivo
    archivo.write("Otra línea de texto.\n")  # Otra línea de texto

print("Se han escrito los datos en 'salida.txt'.\n")


# ----------------------------
# 2. Manejo de Archivos de Texto (Ejemplo Adicional)
# ----------------------------

# Crear y leer un archivo de texto
print("### Creando y Leyendo un Archivo de Texto ###")

with open("ejemplo_texto.txt", "w") as archivo:  # Creamos un archivo de texto y escribimos en él
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Este archivo contiene texto que se puede leer.\n")

# Leer el archivo en modo texto
with open("ejemplo_texto.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo 'ejemplo_texto.txt':")
    print(contenido)

print("\n")


# ----------------------------
# 3. Manejo de Archivos Binarios
# ----------------------------

print("### Manejo de Archivos Binarios ###")

# Crear un archivo binario (por ejemplo, con algunos bytes)
datos_binarios = bytes([65, 66, 67, 68, 69])  # Los números representan los valores ASCII de 'A', 'B', 'C', 'D', 'E'

# Escribir datos binarios en un archivo
with open("ejemplo_binario.bin", "wb") as archivo:  # 'wb' significa "write binary"
    archivo.write(datos_binarios)

# Leer el archivo binario
with open("ejemplo_binario.bin", "rb") as archivo:  # 'rb' significa "read binary"
    contenido_binario = archivo.read()
    print("Contenido del archivo binario 'ejemplo_binario.bin':")
    print(contenido_binario)  # Imprimimos los bytes del archivo binario

print("\n")


# ----------------------------
# 4. Manejo de Archivos CSV
# ----------------------------

import csv  # Importamos el módulo CSV

print("### Manejo de Archivos CSV ###")

# Leer un archivo CSV
print("Leyendo archivo CSV ('datos.csv'):")
try:
    with open('datos.csv', mode='r', newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)  # Creamos el objeto lector
        for fila in lector:
            print(fila)  # Imprimimos cada fila
except FileNotFoundError:
    print("Error: El archivo 'datos.csv' no se encuentra.")

# Escribir en un archivo CSV
print("\nEscribiendo en archivo CSV ('nuevo_datos.csv'):")
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', 25, 'Madrid'],
    ['Ana', 30, 'Barcelona'],
    ['Luis', 22, 'Valencia']
]

with open('nuevo_datos.csv', mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)  # Creamos el escritor
    escritor.writerows(datos)  # Escribimos todas las filas

print("Se han escrito los datos en 'nuevo_datos.csv'.\n")


# ----------------------------
# Conclusión
# ----------------------------

print("### Conclusión ###")
print("En este código, hemos aprendido a manejar diferentes tipos de archivos en Python, incluyendo:")
print("- Archivos de texto (lectura y escritura).")
print("- Archivos binarios (lectura y escritura).")
print("- Archivos CSV (lectura y escritura).")
print("Cada uno de estos formatos es útil para diferentes propósitos y se puede usar según las necesidades de nuestra aplicación.")
