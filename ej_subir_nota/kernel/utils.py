from image import *

def saturate_image(image: Image):
    result = image
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            c_sat = saturate(c)
            result.set_pixel(x, y, c_sat)
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
            valor = kernel[index]
            if valor is None:
                valor = 0
            c = image.get_pixel(x,y)
            result = result + c * valor
            index += 1
    result.a = 1.0
    return result
    