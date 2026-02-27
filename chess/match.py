from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from board import Board
from board_impl import BoardImpl
from pieces import *

class Match:
    def __init__(self, id, player1: str, player2: str):
        self.__id: int = id
        self.__board: BoardImpl = BoardImpl()
        self.turn: Color = Color.WHITE
        
    def get_board(self) -> BoardImpl:
        return self.__board
    def finish_match(self) -> None:
        pass

    def get_match_id(self) -> int:
        return self.__id

    

    def switch_turn(self):
        if self.turn == Color.WHITE:
            self.turn = Color.BLACK
        else:
            self.turn = Color.WHITE

    