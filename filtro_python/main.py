from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler

from numpy import imag
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


def multiplicar_pixeles_por_x(image, num):
    index = 0
    for valor in lista_pix:
        valor = valor * valores(index)
    return lista_pix

def kernel_con_tupla(image: Image, valores: tuple):
    result = Image(image.width, image.height)
    lista_pix: list = []
    for y in range(image.width):
        for x in range(image.height):
            c = image.get_pixel(x,y)
            lista_pix.append(c)
    
            



img = Image()
img.load_from("coche.tga")  # o .tga, .ppm, .png, .jpg
res2 = kernel_con_la_media(img, (1/9, 1/9, 1/9))
res2.save_to("coche2.tga")  # guarda en formato texto PPM

