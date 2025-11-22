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
# Aumentamos el límite de recursión para la función recursiva 'pintar_manchas_vecinas'
sys.setrecursionlimit(20000) 

from image import Image
from Table2D import Table2D
from utils import (
    cambiar_a_blanco_o_negro, 
    contraer_x_veces, 
    dilatar_x_veces, 
    convert_image_to_table2d, 
    get_number_of_blobs,
    contar_tamaño_manchas,
    BlobStats  # Importamos la clase para usar sus métodos estáticos
)

def main():
    print("=== INICIANDO PROCESAMIENTO COMPLETO ===")

    # ---------------------------------------------------------
    # 1. CARGA Y PREPROCESAMIENTO DE IMAGEN
    # ---------------------------------------------------------
    img = Image()
    try:
        # Ruta corregida: se asume que la imagen está en la misma carpeta
        img.load_from("pastillas.tga") 
        print("[OK] Imagen 'pastillas.tga' cargada.")
    except Exception as e:
        print(f"[ERROR] No se pudo cargar la imagen: {e}")
        return

    # 2. Binarizar (blanco y negro)
    img_bin = cambiar_a_blanco_o_negro(img, 0.5)
    
    # 3. Operaciones morfológicas (Contraer y Dilatar) para limpiar ruido
    # Ajusta los números de iteraciones según cuán pegadas estén las manchas
    print("Aplicando contracción (limpiar ruido)...")
    img_procesada = contraer_x_veces(img_bin, 10)

    print("Aplicando dilatación (restaurar forma)...")
    img_final = dilatar_x_veces(img_procesada, 5)
    
    # Guardamos el resultado visual intermedio
    img_final.save_to("pastillas_procesada.tga")
    print("[OK] Imagen procesada guardada como 'pastillas_procesada.tga'.")

    # ---------------------------------------------------------
    # 2. CONVERSIÓN Y ETIQUETADO (LABELING)
    # ---------------------------------------------------------
    print("\n=== ANÁLISIS DE BLOBS ===")
    
    # Crear la tabla con las dimensiones de la imagen
    tabla = Table2D(img_final.width, img_final.height)
    # Convertir píxeles a celdas (0 y 1)
    convert_image_to_table2d(tabla, img_final)

    try:
        # Esto etiqueta la tabla internamente (flood fill recursivo)
        # Los 1 se convierten en ids: 2, 3, 4... etc.
        num_blobs = get_number_of_blobs(tabla)
        print(f"Total de blobs detectados inicialmente: {num_blobs}")
    except RecursionError:
        print("[FATAL] Error de recursividad. Aumenta sys.setrecursionlimit o reduce el tamaño de la imagen.")
        return

    # ---------------------------------------------------------
    # 3. PRUEBA DE FUNCIONES DE ESTADÍSTICA DE 'utils.py'
    # ---------------------------------------------------------
    
    # A) Función: contar_tamaño_manchas
    # Devuelve una lista donde el índice es el ID del blob y el valor es la cantidad de píxeles
    print("\n--- Estadísticas Básicas (contar_tamaño_manchas) ---")
    lista_tamaños = contar_tamaño_manchas(tabla)
    
    # Mostramos algunos ejemplos
    blobs_mostrados = 0
    for id_blob, tamaño in enumerate(lista_tamaños):
        if tamaño > 0: # Solo mostramos IDs que existen (ignora el fondo o vacíos)
            print(f"  Blob ID {id_blob}: {tamaño} píxeles")
            blobs_mostrados += 1
            if blobs_mostrados >= 5:
                print("  ... (resto oculto) ...")
                break

    # ---------------------------------------------------------
    # 4. PRUEBA DE LA CLASE BlobStats (Bounding Boxes y Filtros)
    # ---------------------------------------------------------
    print("\n--- Análisis Avanzado con BlobStats ---")

    # B) Obtener objetos BlobStats (cajas delimitadoras)
    # Se llama usando la clase: BlobStats.get_bounding_boxes(tabla)
    lista_blobs = BlobStats.get_bounding_boxes(tabla)
    print(f"Objetos BlobStats creados: {len(lista_blobs)}")

    if len(lista_blobs) > 0:
        # Mostramos datos del primer blob encontrado como ejemplo
        b = lista_blobs[0]
        print(f"  Ejemplo Blob ID {b.id}: Ancho={b.get_ancho()}, Alto={b.get_alto()}, Píxeles={b.pixel_count}")

    # C) Filtrar por Píxeles (Ej: eliminar ruido menor a 50 px)
    min_px = 50
    max_px = 10000
    blobs_filtrados_tam = BlobStats.filtrar_por_pixeles(lista_blobs, min_px, max_px)
    print(f"Blobs tras filtrar por píxeles [{min_px}-{max_px}]: {len(blobs_filtrados_tam)}")

    # D) Filtrar por Dimensiones (Ej: eliminar objetos muy pequeños o muy grandes)
    min_w, max_w = 10, 200
    min_h, max_h = 10, 200
    blobs_finales = BlobStats.filtrar_por_dimensiones(blobs_filtrados_tam, min_w, max_w, min_h, max_h)
    print(f"Blobs tras filtrar por dimensiones [W:{min_w}-{max_w}, H:{min_h}-{max_h}]: {len(blobs_finales)}")

    print("\n=== PROCESO FINALIZADO CON ÉXITO ===")

if __name__ == "__main__":
    main()