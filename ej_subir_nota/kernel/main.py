from image import Image
from utils import *

# Detección de Bordes
kernel = (
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1
)

# Desenfoque 
# kernel = (
#     1/9, 1/9, 1/9,
#     1/9, 1/9, 1/9,
#     1/9, 1/9, 1/9
# )


# Relieve 
# kernel = (
#     -2, -1,  0,
#     -1,  1,  1,
#      0,  1,  2
# )

img = Image()
img.load_from("coche.tga") 
img2 = convolution(img, kernel)
img2 = saturate_image(img2)
img2.save_to("coche_convolucion.tga")