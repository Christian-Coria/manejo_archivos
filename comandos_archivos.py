# leer el archivo

archivo = open("prueba.txt","r",encoding="utf8") 
print(archivo.read())
# r es de read
# a append anexa info a un archivo que ya contiene informacion y crea el archivo si no existe
# w escribir o crear
# x crea el archivo pero devuelve error si no existe el archivo

# se puede especificar el archivo a crear t es texto... b es binario imagenes video pdf etc
# se puede combinar ej w+r   escribir y leer
# si agregamos despues de "r", encoding="utf8" se podran poner acentos y caracteres de ese tipo
# si ponemos print(archivo.read(5)) y dentrp el 5 x ej solo se leeran 5 caracteres unicam.
# print (archivo.readline())   lee lineas completas de a una
# si trabajamos con direccion de windows seria open("c:\\cursos\\python\\prueba,txt") x ej 
               # y lleva 2 \\ para que no tome el salto de linealo lee como una sola \
#iterar el archivo recorre cada linea del texto     for linea in archivo:
                                                          #print(linea)
#print(archivo.readlines())      nos regresa una lista() con las lineas
# para acceder a una linea en particular     print(archivo.readlines()[2])      mostraria la linea 2
# para abrir un nuevo archivo "a" ( anexar informacion seria)

archivo2 = open("copia.txt", "a")      #si no existe lo crea, si existe anexa informacion al existente
archivo2.write(archivo.read())   #asi lee el archivo 1 y lo copia en el 2

archivo.close()
archivo.close()


