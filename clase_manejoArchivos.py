#uso del context manager
class Manejo_recurso: #no ereda de ninguna clase pero debe contener los metodos "enter" y "exit"

    def __init__(self,nombre): #nombre es el nombre del archivo a trabajar
        self._nombre = nombre

    def __enter__(self):
        print("entramos al recurso".center(50,"*"))
        self.nombre = open(self._nombre,"r",encoding="utf8")
        return self._nombre

    def __exit__(self,tipo_exepcion, valor_exepcion, traza_error):
        #debe colocarse estos parametros
        print("cerramos el recurso".center(50,"*"),)
        if self.nombre:  #se pregunta si la variable aun apunta a un objeto...lo cierre
            self.nombre.close()