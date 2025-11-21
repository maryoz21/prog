from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
from Table2D import Table2D
from image import *
from codec import *
from utils import *

img = Image()
img.load_from("pastillas_binalizado_pequeña.tga")  # o .tga, .ppm, .png, .jpg
tabla: Table2D = Table2D(img.width, img.height)
convert_image_to_table2d(tabla, img)
print(get_num_of_blobs(tabla))