import sys
from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
sys.setrecursionlimit(500000)


from image import *

def gray_filter(image: Image) -> Image:
    result: Image = Image(image.width, image.height)
    for y in range (image.height):
        for x in range(image.width):
            c = image.get_pixel(x, y)

            media = (c.r + c.b + c.g) / 3.0
            c.r = media
            c.g = media
            c.b = media

            result.set_pixel(x, y, c)
    return result

def multiplicar_por_factores(image: Image, fr, fg, fb):
    result: Image = Image(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x, y)

            c.r *= fr
            c.g *= fg
            c.b *= fb
            result.set_pixel(x, y, c)
    return result

def saturate(image: Image):
    result = image
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)

            if c.r < 0:
                c.r = 0
            if c.r > 1:
                c.r = 1
            
            if c.g < 0:
                c.g = 0
            if c.g > 1:
                c.g = 1

            if c.b < 0:
                c.b = 0
            if c.b > 1:
                c.b = 1
    return result

def get_negative(image: Image):
    resultado = image
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            c.r = 1 - c.r
            c.g = 1-c.g
            c.b = 1-c.b

    return resultado

def change_hue(image: Image):
    resultado = image
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            hsl: HSL = c.to_hsl()
            hsl.h += 0.5
            c = hsl.to_rgb()
            resultado.set_pixel(x, y, c)
    return resultado

def cambiar_a_blanco_o_negro(image, num):
    result: Image = Image(image.width, image.height)
    for y in range (image.height):
        for x in range(image.width):
            c = image.get_pixel(x, y)

            media = (c.r + c.b + c.g) / 3.0
            if media > num:
                c.r = 1.0
                c.b = 1.0
                c.g = 1.0
            else: 
                c.r = 0.0
                c.b = 0.0
                c.g = 0.0
            result.set_pixel(x, y, c)
    return result


def min_of_neightbours(image: Image, pixel_x, pixel_y):
    min_c = image.get_pixel(pixel_x, pixel_y)
    for y in range(pixel_y - 1, pixel_y + 2):
        for x in range(pixel_x - 1, pixel_x + 2):
            if 0 < x < image.width and 0 < y < image.height:
                neighbour_c = image.get_pixel(x, y)
                min_c = min_color(min_c, neighbour_c)
    return min_c


def contraer(image: Image):
    result = Image(image.width, image.height)
    for y in range(1, image.height):
        for x in range(1, image.width):
            c = min_of_neightbours(image, x, y)
            result.set_pixel(x, y, c)
    return result

def contraer_x_veces(image, n):
    result = image
    contador = 0
    while contador < n:
        result = contraer(result)
        contador += 1
    return result
        
def max_of_neightbours(image: Image, pixel_x, pixel_y):
    max_c = image.get_pixel(pixel_x, pixel_y)
    for y in range(pixel_y - 1, pixel_y + 2):
        for x in range(pixel_x - 1, pixel_x + 2):
            if 0 < x < image.width and 0 < y < image.height:
                neighbour_c = image.get_pixel(x, y)
                max_c = max_color(max_c, neighbour_c)
    return max_c

def dilatar(image: Image):
    result = Image(image.width, image.height)
    for y in range(1, image.height):
        for x in range(1, image.width):
            c = max_of_neightbours(image, x, y)
            result.set_pixel(x, y, c)
    return result

def dilatar_x_veces(image, n):
    result = image
    contador = 0
    while contador < n:
        result = dilatar(result)
        contador += 1
    return result

def calcular_media(colores: list[Color]) -> Color:
    if len(colores) == 0:
        return Color(0.0, 0.0, 0.0)
    suma: Color = Color(0.0, 0.0, 0.0)
    for valor in colores:
        suma += valor
    media = suma / len(colores)
    media.a = 1.0
    return media

def is_inside_image(image, x, y) -> bool:
    return 0 < x < image.width - 1 and 0 < y < image.height - 1

def media_of_neightbours(image, pixel_x, pixel_y):
    lista = []
    for y in range(pixel_y - 1, pixel_y + 2):
        for x in range(pixel_x - 1, pixel_x + 2):
            if is_inside_image(image, x, y):
                c = image.get_pixel(x, y)
                lista.append(c)
    return calcular_media(lista)

def kernel_con_la_media(image: Image):
    result = Image(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            c = media_of_neightbours(image, x, y)
            result.set_pixel(x, y, c)
    return result


def convolution(image: Image, kernel: tuple):
    result = Image(image.width, image.height)
    for y in range(1, image.height - 1):
        for x in range(1, image.width - 1):
            c = apply_kernel(image, x, y, kernel)
            result.set_pixel(x, y, c)
    return result

def apply_kernel(image: Image,px_x, px_y, kernel: tuple):
    index = 0
    result = Color(0.0, 0.0, 0.0)
    for y in range(px_y - 1, px_y + 2):
        for x in range(px_x - 1, px_x + 2):
            c = image.get_pixel(x,y)
            result = result + c * kernel[index]
            index += 1
    result.a = 1.0
    return result
    

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