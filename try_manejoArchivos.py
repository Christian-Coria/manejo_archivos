#   creamos el archivo  "prueba.txt"
# la variable creada archivo recibe el comando open...

try:

    archivo = open("prueba.txt", "w",encoding="utf8") # l W es de write/ encoding... es para acentos y caracteres
#metodo open abre un arch exist o crear uno o leer o escribir un archivo
    archivo.write("agregando info...\n")
    archivo.write("seguimos agregando...\n")
    archivo.write("seguimos!!!....")

except Exception as e:
    print(e)

finally:
    archivo.close() #una vez cerrado el archivo ya no se puede agregar info
    print("fin del archivo")