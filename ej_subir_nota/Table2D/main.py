from Table2D import Table2D
from image import Image
from utils import *
import sys

sys.setrecursionlimit(500000) 


img = Image()
img.load_from("pastillas.tga")

img_binarizada = cambiar_a_blanco_o_negro(img, 0.5)

img_contraida = contraer_x_veces(img_binarizada, 10)
img_dilatada = dilatar_x_veces(img_contraida, 5)


tabla = Table2D(img_dilatada.width, img_dilatada.height)

convert_image_to_table2d(tabla, img_dilatada)

contar_tamaño_manchas(tabla)

blobs = BlobStats.get_bounding_boxes(tabla)

blobs_filtrados = BlobStats.filtrar_por_pixeles(blobs, 2000, 5000)
blobs_filtrados = BlobStats.filtrar_por_dimensiones(blobs_filtrados, 10, 200, 10, 200)

print(len(blobs_filtrados))