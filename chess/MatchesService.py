from __future__ import annotations
from typing import *
from match import Match
from pieces import *

class MatchesService:
    def __init__(self):
        self.matches: list[Match]
    
    def move(self, match_id: int, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        pass

    def add_match(self, match: Match):
        pass
    
    def create_match(self, match_id: int):
        pass

    def delete_match(self, match_id: int):
        pass

    def clear(self):
        pass

    def start_position(self, match_id: int):
        pass

    def get_status(self, match_id: int) -> str:
        pass

    def who_turn(self, match_id: int) -> Color:
        pass


