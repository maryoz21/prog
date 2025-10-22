from dataclasses import dataclass
from enums import CardSuit, Color
@dataclass
class PokerCard:
    number: int = -1
    type: int = -1

    def set_number(self, number):
        if number is None:
            return 
        if number < 0:
            return
        if number > 13:
            return 
        self.number = number

    def get_number(self) -> int:
        return self.number
    
    def set_type(self, type):
        if type is None:
            return
        if type < 1:
            return
        if type > 4:
            return
        self.type = type
    
    def get_type(self) -> int:
        return self.type

    def get_type_as_string(self) -> str:
        if self.type == CardSuit.DIAMONDS:
            return "Diamonds"
        if self.type == CardSuit.HEARTS:
            return "Hearts"
        if self.type == CardSuit.CLUBS:
            return "Clubs"
        if self.type == CardSuit.SPADES:
            return "Spades"
        return ""

        def get_color(self):
        if self.type == CardSuit.DIAMONDS or self.type == CardSuit.HEARTS:
            return Color.RED
        return Color.BLACK


    def to_string(self) -> str:
        return f"{self.get_number()} {self.get_type_as_string()} {self.get_color()}"
