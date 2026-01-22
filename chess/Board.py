from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod
from MatchesService import *
from pieces import *

class Board(ABC):
    @abstractmethod
    def is_a_piece_in_the_way(self, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        pass

    @abstractmethod
    def get_piece_at(self, x: int, y: int) -> Piece:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_in_bounds(self, x: int, y: int) -> bool:
        pass

