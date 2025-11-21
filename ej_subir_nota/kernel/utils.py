from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
from image import *
from codec import *

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
    