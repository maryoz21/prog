import codec


import struct
import struct
from typing import Union

Number = Union[int, float]

# ======================================================
# Clase HSL
# ======================================================
class HSL:
    """Representa un color en el espacio HSL normalizado [0, 1]."""
    __slots__ = ('h', 's', 'l')

    def __init__(self, h: float, s: float, l: float) -> None:
        self.h = float(h) % 1.0
        self.s = max(0.0, min(1.0, float(s)))
        self.l = max(0.0, min(1.0, float(l)))

    def __repr__(self) -> str:
        return f"HSL(h={self.h:.3f}, s={self.s:.3f}, l={self.l:.3f})"

    def rotate(self, rotation: float) -> 'HSL':
        """Rota el tono (hue) de forma circular en [0, 1]."""
        self.h = (self.h + rotation) % 1.0
        return self

    def to_rgb(self) -> 'Color':
        """Convierte el color HSL a RGB (rango 0–1) y devuelve un Color."""
        h, s, l = self.h, self.s, self.l

        if s == 0:
            r = g = b = l
        else:
            def hue_to_rgb(p, q, t):
                if t < 0: t += 1
                if t > 1: t -= 1
                if t < 1/6: return p + (q - p) * 6 * t
                if t < 1/2: return q
                if t < 2/3: return p + (q - p) * (2/3 - t) * 6
                return p

            q = l + s - l * s if l >= 0.5 else l * (1 + s)
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1/3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1/3)

        return Color(r, g, b, 1.0)



class Color:
    """Color RGBA con componentes reales (sin limitar)."""
    __slots__ = ('r', 'g', 'b', 'a')

    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0) -> None:
        # Se permite cualquier tipo convertible a float
        self.r: float = float(r)
        self.g: float = float(g)
        self.b: float = float(b)
        self.a: float = float(a)

    def __repr__(self) -> str:
        return f"Color(r={self.r:.3f}, g={self.g:.3f}, b={self.b:.3f}, a={self.a:.3f})"

    # ======================================================
    # Conversión a HSL
    # ======================================================
    def to_hsl(self) -> HSL:
        """Convierte este Color RGB a un objeto HSL (rango 0–1)."""
        r, g, b = self.r, self.g, self.b
        c_max = max(r, g, b)
        c_min = min(r, g, b)
        delta = c_max - c_min

        l = (c_max + c_min) / 2.0

        if delta == 0:
            h = 0.0
            s = 0.0
        else:
            s = delta / (1 - abs(2 * l - 1))
            if c_max == r:
                h = ((g - b) / delta) % 6
            elif c_max == g:
                h = ((b - r) / delta) + 2
            else:
                h = ((r - g) / delta) + 4
            h /= 6.0

        return HSL(h, s, l)
    
    # ======================================================
    # Operaciones aritméticas
    # ======================================================
    def __add__(self, other: Union['Color', Number]) -> 'Color':
        if isinstance(other, Color):
            return Color(self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a)
        elif isinstance(other, (int, float)):
            return Color(self.r + other, self.g + other, self.b + other, self.a)
        return NotImplemented

    def __sub__(self, other: Union['Color', Number]) -> 'Color':
        if isinstance(other, Color):
            return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.a - other.a)
        elif isinstance(other, (int, float)):
            return Color(self.r - other, self.g - other, self.b - other, self.a)
        return NotImplemented

    def __mul__(self, other: Union['Color', Number]) -> 'Color':
        if isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b, self.a * other.a)
        elif isinstance(other, (int, float)):
            return Color(self.r * other, self.g * other, self.b * other, self.a)
        return NotImplemented

    def __truediv__(self, other: Union['Color', Number]) -> 'Color':
        if isinstance(other, Color):
            return Color(
                self.r / other.r if other.r != 0 else 0.0,
                self.g / other.g if other.g != 0 else 0.0,
                self.b / other.b if other.b != 0 else 0.0,
                self.a / other.a if other.a != 0 else 0.0
            )
        elif isinstance(other, (int, float)):
            return Color(
                self.r / other if other != 0 else 0.0,
                self.g / other if other != 0 else 0.0,
                self.b / other if other != 0 else 0.0,
                self.a
            )
        return NotImplemented

    __radd__ = __add__
    __rsub__ = lambda self, other: Color(other - self.r, other - self.g, other - self.b, self.a)
    __rmul__ = __mul__

    def __rtruediv__(self, other: Number) -> 'Color':
        if isinstance(other, (int, float)):
            return Color(
                other / self.r if self.r != 0 else 0.0,
                other / self.g if self.g != 0 else 0.0,
                other / self.b if self.b != 0 else 0.0,
                self.a
            )
        return NotImplemented

    # ======================================================
    # Métodos internos (para codec)
    # ======================================================
    def _to_bytes(self, with_alpha: bool = False) -> bytes:
        """Convierte el color a bytes BGR(A) según el modo."""
        c: Color = saturate(self)
        R, G, B = int(c.r * 255), int(c.g * 255), int(c.b * 255)
        if with_alpha:
            A: int = int(c.a * 255)
            return struct.pack('BBBB', B, G, R, A)
        return struct.pack('BBB', B, G, R)

    @staticmethod
    def _from_bytes(b: int, g: int, r: int, a: int | None = None) -> 'Color':
        """Crea un Color a partir de bytes (BGR o BGRA)."""
        if a is None:
            return Color(r / 255.0, g / 255.0, b / 255.0)
        return Color(r / 255.0, g / 255.0, b / 255.0, a / 255.0)


# ======================================================
# Funciones tipo GLSL
# ======================================================

def saturate(color: Color) -> Color:
    """Limita todos los componentes al rango [0, 1]."""
    return Color(
        min(max(color.r, 0.0), 1.0),
        min(max(color.g, 0.0), 1.0),
        min(max(color.b, 0.0), 1.0),
        min(max(color.a, 0.0), 1.0)
    )


def clamp(x: Union[Color, Number], min_val: Number = 0.0, max_val: Number = 1.0) -> Union[Color, Number]:
    """Clampa cada componente (como GLSL clamp)."""
    if isinstance(x, Color):
        return Color(
            min(max(x.r, min_val), max_val),
            min(max(x.g, min_val), max_val),
            min(max(x.b, min_val), max_val),
            min(max(x.a, min_val), max_val),
        )
    return min(max(x, min_val), max_val)


def mix(x: Color, y: Color, a: Number) -> Color:
    """Interpolación lineal: mix(x, y, a) = x*(1-a) + y*a"""
    return x * (1 - a) + y * a


def step(edge: Number, x: Union[Color, Number]) -> Union[Color, Number]:
    """step(edge, x) = 0 si x < edge, 1 si x >= edge"""
    if isinstance(x, Color):
        return Color(
            0.0 if x.r < edge else 1.0,
            0.0 if x.g < edge else 1.0,
            0.0 if x.b < edge else 1.0,
            0.0 if x.a < edge else 1.0,
        )
    return 0.0 if x < edge else 1.0


def smoothstep(edge0: Number, edge1: Number, x: Union[Color, Number]) -> Union[Color, Number]:
    """Versión suave del step."""
    def _f(val: float) -> float:
        t = clamp((val - edge0) / (edge1 - edge0), 0.0, 1.0)
        return t * t * (3 - 2 * t)

    if isinstance(x, Color):
        return Color(_f(x.r), _f(x.g), _f(x.b), _f(x.a))
    return _f(x)


def min_color(a: Union[Color, Number], b: Union[Color, Number]) -> Color:
    """Devuelve el mínimo componente a componente."""
    if isinstance(a, (int, float)):
        a = Color(a, a, a, a)
    if isinstance(b, (int, float)):
        b = Color(b, b, b, b)
    return Color(min(a.r, b.r), min(a.g, b.g), min(a.b, b.b), min(a.a, b.a))


def max_color(a: Union[Color, Number], b: Union[Color, Number]) -> Color:
    """Devuelve el máximo componente a componente."""
    if isinstance(a, (int, float)):
        a = Color(a, a, a, a)
    if isinstance(b, (int, float)):
        b = Color(b, b, b, b)
    return Color(max(a.r, b.r), max(a.g, b.g), max(a.b, b.b), max(a.a, b.a))


def dot(a: Color, b: Color) -> float:
    """Producto punto de los canales RGB (ignora alfa)."""
    return a.r * b.r + a.g * b.g + a.b * b.b


def length(color: Color) -> float:
    """Magnitud euclídea de (r, g, b, a)."""
    return (color.r**2 + color.g**2 + color.b**2 + color.a**2) ** 0.5


def length_rgb(color: Color) -> float:
    """Magnitud euclídea de (r, g, b)."""
    return (color.r**2 + color.g**2 + color.b**2) ** 0.5


def normalize(color: Color) -> Color:
    """Normaliza RGBA completo."""
    mag = length(color)
    if mag == 0:
        return Color(0, 0, 0, 0)
    return color / mag


def normalize_rgb(color: Color) -> Color:
    """Normaliza solo RGB, deja alfa intacto."""
    mag = length_rgb(color)
    if mag == 0:
        return Color(0, 0, 0, color.a)
    return Color(color.r / mag, color.g / mag, color.b / mag, color.a)






















class Image:
    """Representa una imagen con acceso por píxeles."""
    __slots__ = ('_width', '_height', 'pixels')

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        self.pixels = [
            [Color(0.0, 0.0, 0.0, 1.0) for _ in range(width)] for _ in range(height)
        ]

    # Propiedades de solo lectura
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    # Carga y guardado delegados a codec.py
    def load_from(self, path):
        w, h, px = codec.load_image(path)
        self._width, self._height = w, h
        self.pixels = [[Color(r, g, b, a) for (r, g, b, a) in fila] for fila in px]

    def save_to(self, path):
        px = [[(c.r, c.g, c.b, c.a) for c in fila] for fila in self.pixels]
        codec.save_image(path, self._width, self._height, px)

    # Acceso a píxeles
    def get_pixel(self, x, y):
        if 0 <= x < self._width and 0 <= y < self._height:
            return self.pixels[y][x]
        raise IndexError("Coordenadas fuera de rango.")

    def set_pixel(self, x, y, color):
        if 0 <= x < self._width and 0 <= y < self._height:
            self.pixels[y][x] = color
        else:
            raise IndexError("Coordenadas fuera de rango.")
