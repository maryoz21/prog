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

            result.image.set_pixel(x, y, c)
    return result

img = Image()
img.load_from("celda.tga")  # o .tga, .ppm, .png, .jpg
res = gray_filter(img)
res.save_to("salida1.tga")  # guarda en formato texto PPM
