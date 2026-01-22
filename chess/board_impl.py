from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from MatchesService import *
from pieces import *
from board import Board

class BoardImpl(Board):
    def __init__(self):
        self.__pieces = dict[tuple[int, int], Piece]
        self.size: int = 8

    def is_a_piece_in_the_way(self, from_x, from_y, to_x, to_y):
        return super().is_a_piece_in_the_way(from_x, from_y, to_x, to_y)
    
    def get_piece_at(self, x, y):
        return super().get_piece_at(x, y)
    
    def get_size(self):
        return super().get_size()
    
    def is_in_bounds(self, x, y):
        return super().is_in_bounds(x, y)
    
    # Preguntar a Iker
    def visit_squares(self):
        pass

    def add_piece(self, piece: Piece):
        pass

    def move_piece(self, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        pass

    