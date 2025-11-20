import sys
from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
sys.setrecursionlimit(500000)


from image import *


class Table2D:
    def __init__(self, ancho: int = 0, alto: int = 0):
        self._ancho = ancho
        self._alto = alto
        self._lista = [0] * (ancho * alto)
    
    def __str__(self):
        rows = []
        width = self._ancho
        
        for y in range(self._alto):
            # 1. Calculamos dónde empieza y acaba la fila actual en la lista única
            start = y * width
            end = start + width
            
            # 2. Obtenemos el trozo de lista (slice) de esa fila
            row_data = self._lista[start:end]
            
            # 3. Convertimos los números a texto y los unimos con espacios
            # map(str, row_data) convierte [0, 1, 0] en ["0", "1", "0"] rápidamente
            row_str = " ".join(map(str, row_data))
            
            rows.append(row_str)
            
        # 4. Unimos todas las filas con saltos de línea
        return "\n".join(rows)
    
    def get_ancho(self) -> int:
        return self._ancho
    
    def get_alto(self) -> int:
        return self._alto
    
    def get_lista(self) -> list[int]:
        return self._lista.copy

    def get_cell(self, x, y) -> int:
        index = y * self._ancho + x
        return self._lista[index]
    
    def set_cell(self, x, y, value):
        index = y * self._ancho + x
        self._lista[index] = value

    def set_ancho(self, ancho):
        self._ancho = ancho

    def set_alto(self, alto):
        self._alto = alto

    def convert_image_to_table2d(self, image: Image,):
        self._ancho = image.width
        self._alto = image.height
        for y in range(image.height):
            for x in range( image.width): 
                index = y * self._ancho + x
                c = image.get_pixel(x, y)
                if c.r < 0.5: 
                    self._lista[index] = 0
                else: 
                    self._lista[index] = 1


    def encontrar_manchas(self):
        contador = 2
        for alto in range(self._alto):
            for ancho in range(self._ancho):
                if self.get_cell(ancho, alto) == 1:
                    self.pintar_mancha(ancho, alto, contador)
                    contador += 1

    def pintar_mancha(self, ancho, alto, numero_mancha):
        if alto < 0:
            return
        if alto >= self._alto:
            return
        if ancho < 0:
            return
        if ancho >= self._ancho:
            return
        if self.get_cell(ancho, alto) != 1:
            return
        self.set_cell(ancho, alto, numero_mancha)

        self.pintar_mancha(ancho, alto - 1, numero_mancha)
        self.pintar_mancha(ancho, alto + 1, numero_mancha)
        self.pintar_mancha(ancho - 1, alto, numero_mancha)
        self.pintar_mancha(ancho + 1, alto, numero_mancha)

    def contar_tamaño_manchas(self) -> list[int]:
        contador = 0
        for y in range(self._alto):
            for x in range(self._ancho):
                valor = self.get_cell(x, y)
                if valor > contador:
                    contador = valor
        lista_manchas = [0] * (contador + 1)
        for y in range(self._alto):
            for x in range(self._ancho):
                valor = self.get_cell(x, y)
                if valor > 1:
                    lista_manchas[valor] += 1
        return lista_manchas
    
    def eliminar_manchas_menores_a(self, pixeles_minimo) -> list[int]:
        contador = self.contar_tamaño_manchas()
        for y in range(self._alto): 
            for x in range(self._ancho):
                valor = self.get_cell(x, y)
                if valor > 1:
                    if valor < len(contador):
                        tamaño_mancha = contador[valor]

                    if tamaño_mancha < pixeles_minimo:
                        self.set_cell(x, y, 0)
    
    def get_lista_manchas_mayores_a(self, pixeles_minimos):
        copia_lista = self.contar_tamaño_manchas()
        resultado = []
        for tamaño in copia_lista:
            if tamaño >= pixeles_minimos:
                resultado.append(tamaño)
        return resultado


img = Image()
img.load_from("pastillas_binalizado.tga")  # o .tga, .ppm, .png, .jpg
tabla: Table2D = Table2D(img.width, img.height)
tabla.convert_image_to_table2d(img)
tabla.encontrar_manchas()
print(tabla.get_lista_manchas_mayores_a(50))