#with abre el archivo y cierra el archivo automaticamente
#asi with lla al metodo __enter__ y __exit__

with open("prueba.txt","r", encoding="utf8") as archivo:
    print(archivo.read())



