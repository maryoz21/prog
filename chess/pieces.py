from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from enum import Enum
from MatchesService import *
from board import Board

class Color(Enum):
    BLANCO = 1
    NEGRO = 2

class PieceType(Enum):
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6

class Piece(ABC):
    def __init__(self, color: Color, x: int, y: int, piece_type: PieceType):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__piece_type: PieceType = piece_type

    @abstractmethod
    def can_i_move(self, x: int, y: int, board: Board) -> bool:
        pass

    @abstractmethod
    def movimientos_posibles(self, board: Board) -> list[tuple[int, int]]:
        pass

    def get_type_of_piece(self) -> PieceType:
        return self.piece_type

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.PAWN)

    def can_i_move(self, x, y, board):
        pass
    
    def coronar(self):
        pass

    def salida(self):
        pass

    def movimientos_posibles(self, board):
        pass

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.ROOK)

    def can_i_move(self, x, y, board):
        return super().can_i_move(x, y, board)
    
    def enroque(self):
        pass

    def movimientos_posibles(self, board):
        pass

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.KNIGHT)

    def can_i_move(self, x, y, board):
        return super().can_i_move(x, y, board)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.BISHOP)

    def can_i_move(self, x, y, board):
        return super().can_i_move(x, y, board)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.QUEEN)

    def can_i_move(self, x, y, board):
        return super().can_i_move(x, y, board)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.KING)

    def can_i_move(self, x, y, board):
        return super().can_i_move(x, y, board)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
    def enroque(self):
        pass
