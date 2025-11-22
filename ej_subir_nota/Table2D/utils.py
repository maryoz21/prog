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


def convert_image_to_table2d(table: Table2D, image: Image,):
    table.set_ancho(image.width) 
    table.set_alto(image.height)
    for y in range(image.height):
        for x in range( image.width): 
            c = image.get_pixel(x, y)
            if c.r < 0.5: 
                table.set_cell(x, y, 0) 
            else: 
                table.set_cell(x, y, 1) 
                
def get_number_of_blobs(table: Table2D):
    num_of_blobs = identificar_blobs(table)
    return num_of_blobs - 2



def contar_tamaño_manchas(table: Table2D):
    contador = identificar_blobs(table)
    lista_manchas = [0] * (contador + 1)
    for y in range(table.get_alto()):
        for x in range(table.get_ancho()):
            valor = table.get_cell(x, y)
            if valor > 1:
                lista_manchas[valor] += 1
    return lista_manchas

def identificar_blobs(table: Table2D):
    contador = 2
    for alto in range(table.get_alto()):
        for ancho in range(table.get_ancho()):
            if table.get_cell(ancho, alto) == 1:
                pintar_manchas_vecinas(table, ancho, alto, contador)
                contador += 1
    return contador

def pintar_manchas_vecinas(table: Table2D, ancho, alto, numero_mancha):
    if alto < 0:
        return
    if alto >= table.get_alto():
        return
    if ancho < 0:
        return
    if ancho >= table.get_ancho():
        return
    if table.get_cell(ancho, alto) != 1:
        return
    table.set_cell(ancho, alto, numero_mancha)

    pintar_manchas_vecinas(table, ancho, alto - 1, numero_mancha)
    pintar_manchas_vecinas(table, ancho, alto + 1, numero_mancha)
    pintar_manchas_vecinas(table, ancho - 1, alto, numero_mancha)
    pintar_manchas_vecinas(table, ancho + 1, alto, numero_mancha)

def get_max_id(table: Table2D):
    max_id = 0
    for y in range(table.get_alto()):
        for x in range(table.get_ancho()):
            valor = table.get_cell(x, y)
            if valor > max_id:
                max_id = valor
    return max_id

class BlobStats:
    def __init__(self, id: int, pixel_count: int = 0, x_min: int = -1, x_max: int = -1, y_min: int = -1, y_max: int = -1):
        self.id = id
        self.pixel_count = pixel_count
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def get_ancho(self) -> int:
        if self.x_min == -1:
            return 0
        return self.x_max - self.x_min + 1
    
    def get_alto(self) -> int:
        if self.y_min == -1:
            return 0
        return self.y_max - self.y_min + 1

    def add_pixel(self, x, y):
        self.pixel_count += 1
        if self.x_min == -1:
            self.x_min = x
            self.y_min = y
            self.x_max = x
            self.y_max = y
        else:
            if x < self.x_min:
                self.x_min = x
            if y < self.y_min:
                self.y_min = y
            if x > self.x_max:
                self.x_max = x
            if y > self.y_max:
                self.y_max = y

    def get_bounding_boxes(table: Table2D):
        max_id = get_max_id(table)

        if max_id < 2:
            return []
        lista_blobs = [None] * (max_id + 1)
        for y in range(table.get_alto()):
            for x in range(table.get_ancho()):
                blob_id = table.get_cell(x, y)
                if blob_id > 1:
                    if lista_blobs[blob_id] is None:
                        lista_blobs[blob_id] = BlobStats(blob_id)
                    blob = lista_blobs[blob_id]
                    blob.add_pixel(x,y)
        result = []
        for blob in lista_blobs:
            if blob is not None:
                result.append(blob)
        return result

        

    def filtrar_por_pixeles(lista_blobs, min_pixels, max_pixels):
        result = []
        for blob in lista_blobs:
            if blob is not None:
                if min_pixels <= blob.pixel_count <= max_pixels:
                    result.append(blob)
        return result
    
    def filtrar_por_dimensiones(lista_blobs, min_ancho, max_ancho, min_alto, max_alto):
        result = []
        for blob in lista_blobs:
            if blob is not None:
                ancho = blob.get_ancho()
                alto = blob.get_alto()
                if min_ancho <= ancho <= max_ancho:
                   if min_alto <= alto <= max_ancho:
                       result.append(blob)
        return result