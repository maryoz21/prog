from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from enum import Enum
from MatchesService import *
from board import Board

class Color(Enum):
    WHITE = 1
    BLACK = 2

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

    def get_color(self):
        return self.__color
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def can_i_move(self, x, y, board):
        if board.is_in_bounds(x,y):
            posible_moves = self.movimientos_posibles()
            for move in posible_moves:
                mov_x, mov_y = move
                if mov_x == x and mov_y == y:
                    return True
        return False    

    @abstractmethod
    def movimientos_posibles(self, board: Board) -> list[tuple[int, int]]:
        pass

    def get_type_of_piece(self) -> PieceType:
        return self.__piece_type

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.PAWN)    
        
    
    def coronar(self) -> bool:
        if self.get_color() == Color.BLACK:
            if self.get_y() == 1:
                return True
        if self.get_color() == Color.WHITE:
            if self.get_y() == 8:
                return True
        return False

    def is_pawn_in_start_position(self):
        if self.get_color() == Color.BLACK:
            if self.get_y() == 7:
                return True
        if self.get_color() == Color.WHITE:
            if self.get_y() == 2:
                return True
        return False  

    def movimientos_posibles(self, board) -> list[tuple[int, int]]:
        movement_list =[]
        x = self.get_x()
        y = self.get_y()
        color = self.get_color()

        direction = 1
        if color == Color.BLACK:
            direction = -1
        
        next_y = y + direction

        if board.is_in_bounds(x, next_y):
            piece_at_front = board.get_piece_at(x, next_y)
            if piece_at_front is None:
                movement_list.append((x, next_y))

                if self.is_pawn_in_start_position():
                    y_doble = y + (2 * direction)
                    if board.is_in_bounds(x, y_doble):
                        if board.get_piece_at(x, y_doble) is None:
                            movement_list.append((x, y_doble))

        diagonal_x = [x - 1, x + 1]
        for x_diag in diagonal_x:
            if board.is_in_bounds(x_diag, next_y):
                aimed_piece = board.get_piece_at(x_diag, next_y)

                if aimed_piece is not None:
                    if aimed_piece.get_color() != color:
                        movement_list.append((x_diag, next_y))
        return movement_list
                         



class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.ROOK)
    

    def enroque(self):
        pass

    def movimientos_posibles(self, board):
        movement_list =[]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            x_actual = self.get_x() + dx
            y_actual = self.get_y() + dy

        while board.is_in_bounds(x_actual, y_actual):
            piece_at_square = board.get_piece_at(x_actual, y_actual)
            if piece_at_square is None: 
                movement_list.append((x_actual, y_actual))
            else:
                if piece_at_square.get_color() != self.get_color():
                    movement_list.append((x_actual, y_actual))
                    break
            x_actual += dx
            y_actual += dy

        return movement_list


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.KNIGHT)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.BISHOP)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.QUEEN)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, PieceType.KING)
    
    def movimientos_posibles(self, board):
        return super().movimientos_posibles(board)
    
    def enroque(self):
        pass
