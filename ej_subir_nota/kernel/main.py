from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
from codec import *
from image import Image
from utils import *


img = Image()
img.load_from("pastillas.tga") 

kernel = [
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1
]

img2 = convolution(img, kernel)

img2.save_to("pastillas_convolucion.tga")

print("Proceso terminado.")