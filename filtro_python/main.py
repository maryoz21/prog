import sys
from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
sys.setrecursionlimit(500000)
from Tabla2D import Table2D

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


def contar_manchas(tabla: Table2D):
    contador = 2
    for alto in range(tabla.get_alto()):
        for ancho in range(tabla.get_ancho()):
            if tabla.get_cell(ancho, alto) == 1:
                pintar_mancha(tabla, ancho, alto, contador)
                contador += 1
    return contador

def get_num_of_blobs(tabla: Table2D):
    return contar_manchas(tabla) - 2

def pintar_mancha(tabla: Table2D, ancho, alto, numero_mancha):
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

    pintar_mancha(tabla, ancho, alto - 1, numero_mancha)
    pintar_mancha(tabla, ancho, alto + 1, numero_mancha)
    pintar_mancha(tabla, ancho - 1, alto, numero_mancha)
    pintar_mancha(tabla, ancho + 1, alto, numero_mancha)

def contar_tamaño_mancha(tabla: Table2D, pixeles_minimo):
    contador = 0
    for y in range(tabla.get_alto()):
        for x in range(tabla.get_ancho()):
            valor = tabla.get_cell(x, y)
            if valor > contador:
                contador = valor
    lista_manchas = [0] * (contador + 1)
    for y in range(tabla.get_alto()):
        for x in range(tabla.get_ancho()):
            valor = tabla.get_cell(x, y)
            if valor > 1:
                lista_manchas[valor] += 1
    return lista_manchas

def eliminar_mancha_pequeña(tabla: Table2D, pixeles_minimo):
    contador = contar_tamaño_mancha(tabla, pixeles_minimo)
    for y in range(tabla.get_alto()): 
        for x in range(tabla.get_ancho()):
            valor = tabla.get_cell(x, y)
            if valor > 1:
                if valor < len(contador):
                    tamaño_mancha = contador[valor]
                    if tamaño_mancha < pixeles_minimo:
                        tabla.set_cell(x, y, 0)
    return contador


       
img = Image()
img.load_from("pastillas_binalizado_pequeña.tga")  # o .tga, .ppm, .png, .jpg
tabla: Table2D = Table2D(img.width, img.height)
convert_image_to_table2d(tabla, img)
print(get_num_of_blobs(tabla))
