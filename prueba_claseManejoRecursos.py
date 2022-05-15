from clase_manejoArchivos import Manejo_recurso

with Manejo_recurso("prueba.txt") as archivo:
    print(archivo.read())
