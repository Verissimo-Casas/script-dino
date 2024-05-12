import os
""" Este script se usa para eliminar la ultima columna de los archivos .txt de kitti exportado desde CVAT"""
# Ruta al directorio que contiene tus archivos .txt
directorio = '/home/getter/repositorio/data/mantenimiento/train/labels'

# Lista todos los archivos en el directorio
archivos = os.listdir(directorio)

# Itera sobre cada archivo en el directorio
for archivo in archivos:
    if archivo.endswith('.txt'):
        ruta_archivo = os.path.join(directorio, archivo)
        
        # Lee el contenido del archivo
        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()

        # Procesa cada línea y elimina la última columna
        for i in range(len(lineas)):
            partes = lineas[i].split()
            nueva_linea = ' '.join(partes[:-1]) + '\n'
            lineas[i] = nueva_linea

        # Escribe el contenido modificado de vuelta al archivo
        with open(ruta_archivo, 'w') as file:
            file.writelines(lineas)

print("Proceso completado.")

