from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from pieces import *

class Board(ABC):

    @abstractmethod
    def get_piece_at(self, x: int, y: int) -> Piece:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_in_bounds(self, x: int, y: int) -> bool:
        pass

    # En Board.py
def to_dict(self):
    # Esto debe devolver una matriz 8x8 o una lista de piezas
    # Ejemplo simplificado:
    return [
        [piece.symbol if piece else "" for piece in row] 
        for row in self.grid
    ]

