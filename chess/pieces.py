from abc import ABC, abstractmethod
from enum import Enum

class Color(Enum):
    BLANCO = 1
    NEGRO = 2

class Piece(ABC):
    def __init__(self, color: Color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y

    @abstractmethod
    def can_i_move(self, x: int, y: int, tablero: Tablero) -> bool:
        pass

class Tablero(ABC):


