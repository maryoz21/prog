from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
from Table2D import Table2D
from image import *
from codec import *

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


def convert_image_to_table2d(tabla: Table2D, image: Image,):
    tabla.set_ancho(image.width) 
    tabla.set_alto(image.height)
    for y in range(image.height):
        for x in range( image.width): 
            c = image.get_pixel(x, y)
            if c.r < 0.5: 
                tabla.set_cell(x, y, 0) 
            else: 
                tabla.set_cell(x, y, 1) 
                
def identificar_blobs(tabla: Table2D):
    contador = 2
    for alto in range(tabla.get_alto()):
        for ancho in range(tabla.get_ancho()):
            if tabla.get_cell(ancho, alto) == 1:
                pintar_manchas_vecinas(tabla, ancho, alto, contador)
                contador += 1
    return contador

def contar_tamaño_manchas(tabla: Table2D):
    contador = identificar_blobs(tabla)
    lista_manchas = [0] * (contador + 1)
    for y in range(tabla.get_alto()):
        for x in range(tabla.get_ancho()):
            valor = tabla.get_cell(x, y)
            if valor > 1:
                lista_manchas[valor] += 1
    return lista_manchas

def pintar_manchas_vecinas(tabla: Table2D, ancho, alto, numero_mancha):
    if alto < 0:
        return
    if alto >= tabla.get_alto():
        return
    if ancho < 0:
        return
    if ancho >= tabla.get_ancho():
        return
    if tabla.get_cell(ancho, alto) != 1:
        return
    tabla.set_cell(ancho, alto, numero_mancha)

    pintar_manchas_vecinas(tabla, ancho, alto - 1, numero_mancha)
    pintar_manchas_vecinas(tabla, ancho, alto + 1, numero_mancha)
    pintar_manchas_vecinas(tabla, ancho - 1, alto, numero_mancha)
    pintar_manchas_vecinas(tabla, ancho + 1, alto, numero_mancha)




def eliminar_manchas_menores_a(tabla: Table2D, pixeles_minimo):
    contador = contar_tamaño_manchas(tabla)
    for y in range(tabla.get_alto()): 
        for x in range(tabla.get_ancho()):
            valor = tabla.get_cell(x, y)
            if valor > 1:
                if valor < len(contador):
                    tamaño_mancha = contador[valor]
                    if tamaño_mancha < pixeles_minimo:
                        tabla.set_cell(x, y, 0)
    return contador


class BlobStats:
    def __init__(self, id: int, pixel_count: int, x_min: int, x_max: int, y_min: int, y_max: int, table: Table2D):
        self.id = id
        self.pixel_count = pixel_count
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.table = table

    def get_bounding_boxes(table: Table2D):
        valor_max = identificar_blobs(table: Table2D)
        blobs = []
