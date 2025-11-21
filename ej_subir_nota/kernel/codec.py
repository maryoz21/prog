import struct
import importlib


# ================================================================
# === TGA sin compresión (24 o 32 bits) ==========================
# ================================================================
def load_tga(path):
    with open(path, 'rb') as f:
        header = f.read(18)
        id_length = header[0]
        image_type = header[2]
        width, height, bpp = struct.unpack('<HHB', header[12:17])
        descriptor = header[17]
        origin_top = bool(descriptor & 0x20)  # bit 5 = 1 → origen arriba

        if image_type != 2 or bpp not in (24, 32):
            raise ValueError("Solo se admiten TGA RGB(A) sin compresión (24 o 32 bits).")

        if id_length:
            f.read(id_length)

        bytes_per_pixel = bpp // 8
        data = f.read(width * height * bytes_per_pixel)
        pixels, i = [], 0
        for y in range(height):
            fila = []
            for x in range(width):
                if bpp == 24:
                    b, g, r = data[i:i+3]
                    fila.append((r/255.0, g/255.0, b/255.0, 1.0))
                    i += 3
                else:
                    b, g, r, a = data[i:i+4]
                    fila.append((r/255.0, g/255.0, b/255.0, a/255.0))
                    i += 4
            pixels.append(fila)

        # Solo invertir si el origen está abajo
        if not origin_top:
            pixels.reverse()

        return width, height, pixels


def save_tga(path, width, height, pixels):
    has_alpha = any(abs(p[3]-1.0) > 1e-6 for fila in pixels for p in fila)
    bpp = 32 if has_alpha else 24
    header = bytearray(18)
    header[2] = 2  # tipo: sin compresión
    struct.pack_into('<HHB', header, 12, width, height, bpp)

    # bit 5 = 1 → origen arriba
    header[17] = 0x20

    with open(path, 'wb') as f:
        f.write(header)
        for fila in pixels:  # no invertimos manualmente
            for r, g, b, a in fila:
                if has_alpha:
                    f.write(struct.pack('BBBB', int(b*255), int(g*255), int(r*255), int(a*255)))
                else:
                    f.write(struct.pack('BBB', int(b*255), int(g*255), int(r*255)))


# ================================================================
# === BMP sin compresión (24 bits) ===============================
# ================================================================
def load_bmp(path):
    with open(path, 'rb') as f:
        header = f.read(54)
        if header[0:2] != b'BM':
            raise ValueError("No es un archivo BMP válido.")

        width, height = struct.unpack('<ii', header[18:26])
        bpp = struct.unpack('<H', header[28:30])[0]
        if bpp != 24:
            raise ValueError("Solo se admiten BMP de 24 bits sin compresión.")

        row_padded = (width * 3 + 3) & ~3
        pixels = []
        for _ in range(height):
            row = f.read(row_padded)
            fila = []
            for x in range(width):
                b, g, r = row[x*3:x*3+3]
                fila.append((r/255.0, g/255.0, b/255.0, 1.0))
            pixels.append(fila)

        pixels.reverse()  # origen arriba
        return width, height, pixels


def save_bmp(path, width, height, pixels):
    row_padded = (width * 3 + 3) & ~3
    filesize = 54 + row_padded * height
    header = bytearray(54)
    struct.pack_into('<2sIHHI', header, 0, b'BM', filesize, 0, 0, 54)
    struct.pack_into('<IIIHHIIIIII', header, 14, 40, width, height, 1, 24, 0,
                     row_padded * height, 2835, 2835, 0, 0)

    with open(path, 'wb') as f:
        f.write(header)
        for fila in reversed(pixels):  # guardar de abajo a arriba
            row_bytes = b''.join(struct.pack('BBB', int(b*255), int(g*255), int(r*255)) for r, g, b, a in fila)
            padding = b'\x00' * (row_padded - width * 3)
            f.write(row_bytes + padding)


# ================================================================
# === PPM (P3 / P6) =============================================
# ================================================================
def load_ppm(path):
    with open(path, 'rb') as f:
        magic = f.readline().strip()
        if magic not in (b'P3', b'P6'):
            raise ValueError("Solo se admiten PPM P3 (texto) o P6 (binario).")

        def next_line():
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()
            return line

        dims = next_line().split()
        width, height = int(dims[0]), int(dims[1])
        maxval = int(next_line())
        pixels = []

        if magic == b'P3':
            values = []
            for line in f:
                if not line.startswith(b'#'):
                    values += [int(x) for x in line.split()]
            i = 0
            for y in range(height):
                fila = []
                for x in range(width):
                    r, g, b = values[i:i+3]
                    fila.append((r/maxval, g/maxval, b/maxval, 1.0))
                    i += 3
                pixels.append(fila)
        else:
            data = f.read(width * height * 3)
            i = 0
            for y in range(height):
                fila = []
                for x in range(width):
                    r, g, b = data[i:i+3]
                    fila.append((r/maxval, g/maxval, b/maxval, 1.0))
                    i += 3
                pixels.append(fila)

        return width, height, pixels


def save_ppm(path, width, height, pixels, binary=True):
    if binary:
        with open(path, 'wb') as f:
            f.write(b'P6\n')
            f.write(f"{width} {height}\n255\n".encode())
            for fila in pixels:
                for r, g, b, a in fila:
                    f.write(struct.pack('BBB', int(r*255), int(g*255), int(b*255)))
    else:
        with open(path, 'w') as f:
            f.write("P3\n")
            f.write(f"{width} {height}\n255\n")
            for fila in pixels:
                for r, g, b, a in fila:
                    f.write(f"{int(r*255)} {int(g*255)} {int(b*255)} ")
                f.write("\n")


# ================================================================
# === PNG / JPG (solo si hay Pillow) =============================
# ================================================================
def load_with_pillow(path):
    img = PILImage.open(path).convert("RGBA")
    width, height = img.size
    data = list(img.getdata())
    pixels, i = [], 0
    for y in range(height):
        fila = []
        for x in range(width):
            r, g, b, a = data[i]
            fila.append((r/255.0, g/255.0, b/255.0, a/255.0))
            i += 1
        pixels.append(fila)
    return width, height, pixels


def save_with_pillow(path, width, height, pixels):
    flat = []
    for fila in pixels:
        for r, g, b, a in fila:
            flat.append((int(r*255), int(g*255), int(b*255), int(a*255)))
    img = PILImage.new("RGBA", (width, height))
    img.putdata(flat)
    img.save(path)


# ================================================================
# === Interfaz unificada =========================================
# ================================================================
def load_image(path):
    path_lower = path.lower()
    if path_lower.endswith(".tga"):
        return load_tga(path)
    if path_lower.endswith(".bmp"):
        return load_bmp(path)
    if path_lower.endswith(".ppm"):
        return load_ppm(path)
    if _pil is not None and path_lower.endswith((".png", ".jpg", ".jpeg")):
        return load_with_pillow(path)
    raise ValueError(f"Formato no soportado o librería ausente: {path}")


def save_image(path, width, height, pixels):
    path_lower = path.lower()
    if path_lower.endswith(".tga"):
        return save_tga(path, width, height, pixels)
    if path_lower.endswith(".bmp"):
        return save_bmp(path, width, height, pixels)
    if path_lower.endswith(".ppm"):
        return save_ppm(path, width, height, pixels)
    if _pil is not None and path_lower.endswith((".png", ".jpg", ".jpeg")):
        return save_with_pillow(path, width, height, pixels)
    raise ValueError(f"Formato no soportado o librería ausente: {path}")
