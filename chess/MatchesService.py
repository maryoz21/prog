from __future__ import annotations
from typing import *
from match import Match
from pieces import *
from board_impl import BoardImpl

class MatchesService:
    def __init__(self):
        self.matches: list[Match] = []
    
    def move(self, match_id: int, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        match = None
        for m in self.matches:
            if m.get_match_id() == match_id:
                match = m
                break
        if match is None:
            return False
        
        board = match.get_board()

        piece = board.get_piece_at(from_x, from_y)

        if piece is None:
            return False
        
        if piece.get_color() != match.turn:
            return False
        
        movimento_exitoso = board.move_piece(from_x, from_y, to_x, to_y)

        if movimento_exitoso:
            match.switch_turn()
            return True
        return False

    def add_match(self, match: Match):
        pass
    
    def create_match(self, match_id: int):
        pass

    def delete_match(self, match_id: int):
        pass

    def clear(self):
        pass

    def start_position(self, match_id: int):
        match = None
        for m in self.matches:
            if m.get_match_id() == match_id:
                match = m
                break
        
        if match is None:
            return
        
        board = match.get_board()

        self.__add_pawns(board)
        self.__add_rooks(board)
        self.__add_knights(board)
        self.__add_bishops(board)
        self.__add_queens(board)
        self.__add_kings(board)

    def __add_pawns(self, board: BoardImpl):
        for x in range(1, 9):
            board.add_piece(Pawn(Color.WHITE, x, 2))
            board.add_piece(Pawn(Color.BLACK, x, 7))

    def __add_rooks(self, board: BoardImpl):
        board.add_piece(Rook(Color.WHITE, 1, 1))
        board.add_piece(Rook(Color.WHITE, 8, 1))
        board.add_piece(Rook(Color.BLACK, 1, 8))
        board.add_piece(Rook(Color.BLACK, 8, 8))

    def __add_knights(self, board: BoardImpl):
        board.add_piece(Knight(Color.WHITE,2, 1))
        board.add_piece(Knight(Color.WHITE,7, 1))
        board.add_piece(Knight(Color.BLACK,2, 8))
        board.add_piece(Knight(Color.BLACK,7, 8))

    def __add_bishops(self, board: BoardImpl):
        board.add_piece(Bishop(Color.WHITE, 3, 1))
        board.add_piece(Bishop(Color.WHITE, 6, 1))
        board.add_piece(Bishop(Color.BLACK, 3, 8))
        board.add_piece(Bishop(Color.BLACK, 6, 8))

    def __add_queens(self, board: BoardImpl):
        board.add_piece(Queen(Color.WHITE, 4, 1))
        board.add_piece(Queen(Color.BLACK, 4, 8))

    def __add_kings(self, board: BoardImpl):
        board.add_piece(King(Color.WHITE, 5, 1))
        board.add_piece(King(Color.BLACK, 5, 8))


    def get_status(self, match_id: int) -> str:
        pass

    def who_turn(self, match_id: int) -> Color:
        pass


