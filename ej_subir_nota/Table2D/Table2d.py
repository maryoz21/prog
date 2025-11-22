class Table2D:
    def __init__(self, ancho: int = 0, alto: int = 0):
        self._ancho = ancho
        self._alto = alto
        self._lista = [0] * (ancho * alto)
    
    def get_ancho(self) -> int:
        return self._ancho
    
    def get_alto(self) -> int:
        return self._alto

    def get_cell(self, x, y) -> int:
        index = y * self._ancho + x
        return self._lista[index] 

    def get_cell_by_index(self, index) -> int:
        return self._lista[index]

    def set_cell(self, x, y, value):
        index = y * self._ancho + x
        self._lista[index] = value

    def set_ancho(self, ancho):
        self._ancho = ancho

    def set_alto(self, alto):
        self._alto = alto