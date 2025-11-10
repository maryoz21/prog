from image import *


img = Image()
img.load_from("coche.tga")  # o .tga, .ppm, .png, .jpg



for y in range(img.height):
    for x in range(img.width):
        c = img.get_pixel(x, y)
        hsl = c.to_hsl()
        hsl.rotate(-0.25)
        c = hsl.to_rgb()
        img.set_pixel(x, y, c)



img.save_to("salida.tga")  # guarda en formato texto PPM
