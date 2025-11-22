class Table2D:
    def __init__(self, ancho: int = 0, alto: int = 0):
        self.__ancho = ancho
        self.__alto = alto
        self.__lista = [0] * (ancho * alto)
    
    def get_ancho(self) -> int:
        return self.__ancho
    
    def get_alto(self) -> int:
        return self.__alto

    def get_cell(self, x, y) -> int:
        index = y * self._ancho + x
        return self.__lista[index] 

    def get_cell_by_index(self, index) -> int:
        return self.__lista[index]

    def set_cell(self, x, y, value):
        index = y * self.__ancho + x
        self._lista[index] = value

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def set_alto(self, alto):
        self.__alto = alto
    
    def set_lista(self, tamaño):
        self.__lista = [0] * tamaño