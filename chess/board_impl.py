from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from MatchesService import *
from pieces import *
from board import Board

class BoardImpl(Board):
    def __init__(self):
        self.__pieces = dict[tuple[int, int], Piece]
        self.__size: int = 8

    
    def get_piece_at(self, x: int, y: int):
        return self.__pieces.get((x, y))
    
    def get_size(self):
        return self.__size
    
    def is_in_bounds(self, x: int, y: int) -> bool:
        if x is None or y is None:
            return False
        size = self.get_size()
        if x <= size and x > 0:
            if y <= size and y > 0:
                return True
        return False
    
    # Preguntar a Iker
    def visit_squares(self):
        pass

    def add_piece(self, piece: Piece):
        if piece is None:
            return
        
        x = piece.get_x()
        y = piece.get_y()

        if self.is_in_bounds(x, y):
            self.__pieces[(x, y)] = piece

    def delete_piece(self, piece: Piece):
        if piece is None:
            return
        x = piece.get_x()
        y = piece.get_y()

        self.__pieces.pop((x, y), None)
        
        


    def move_piece(self, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        piece = self.__pieces.get((from_x, from_y))
        if piece is None:
            return False
        if self.is_in_bounds(to_x, to_y):
            self.delete_piece(piece)
            piece.set_x(to_x)
            piece.set_y(to_y)

            self.add_piece(piece)

            return True
        return False

    