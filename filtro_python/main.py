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


img = Image()
img.load_from("coche.tga")  # o .tga, .ppm, .png, .jpg
res2 = cambiar_a_blanco_o_negro(img, 0.7)
res2.save_to("salida.tga")  # guarda en formato texto PPM
