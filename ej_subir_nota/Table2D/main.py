from turtle import color, width
from unittest import result
from wsgiref.handlers import CGIHandler
from Table2D import Table2D
from image import Image
from codec import *
from utils import *

# img = Image()
# img.load_from("pastillas.tga")  # o .tga, .ppm, .png, .jpg
# img.cambiar_a_blanco_o_negro
# tabla: Table2D = Table2D(img.width, img.height)
# convert_image_to_table2d(tabla, img)

import sys
# Aumentamos el límite de recursión por seguridad si no cambiaste a la versión iterativa
sys.setrecursionlimit(5000) 

from image import Image
from Table2D import Table2D
from utils import (
    cambiar_a_blanco_o_negro, 
    contraer_x_veces, 
    dilatar_x_veces, 
    convert_image_to_table2d, 
    get_number_of_blobs
)

def main():
    print("Iniciando procesamiento...")

    # 1. Cargar la imagen original
    img = Image()
    try:
        img.load_from("pastillas.tga")
        print("Imagen 'pastillas.tga' cargada correctamente.")
    except FileNotFoundError:
        print("ERROR: No se encuentra 'pastillas.tga'.")
        return

    # 2. Binarizar (blanco y negro)
    img_bin = cambiar_a_blanco_o_negro(img, 0.5)
    img_bin.save_to("pastillas_binarizada.tga")
    print("Guardada paso intermedio: 'pastillas_binarizada.tga'.")

    # 3. Contraer 20 veces (eliminar ruido/separar)
    print("Contrayendo 15 veces...")
    img_procesada = contraer_x_veces(img_bin, 10)

    # 4. Dilatar 10 veces (recuperar forma)
    print("Dilatando 5 veces...")
    img_final = dilatar_x_veces(img_procesada, 5)
    
    # 5. Guardar la imagen final visual
    img_final.save_to("pastillas2.tga")
    print("Imagen procesada guardada como 'pastillas2.tga'.")

    # ========================================================
    # NUEVO: CONTAR MANCHAS
    # ========================================================
    print("Analizando blobs (manchas)...")

    # 6. Crear la Tabla con las dimensiones de la imagen final
    # Es CRÍTICO pasar el ancho y alto aquí para que se cree la lista interna
    tabla = Table2D(img_final.width, img_final.height)
    
    # 7. Convertir la imagen (píxeles) a Tabla (0s y 1s)
    convert_image_to_table2d(tabla, img_final)

    # 8. Obtener el número de blobs
    try:
        numero_de_blobs = get_number_of_blobs(tabla)
        print("------------------------------------------------")
        print(f"RESULTADO: Se han detectado {numero_de_blobs} blobs (pastillas).")
        print("------------------------------------------------")
    except RecursionError:
        print("ERROR: Se superó el límite de recursividad.")
        print("Solución: Usa la versión iterativa (con pila/stack) de 'pintar_manchas_vecinas' en utils.py")

if __name__ == "__main__":
    main()