from dataclasses import dataclass
##########################
# Types of value
#-------------------------
# 1: Diamonds
# 2: Hearts
# 3: Clubs
# 4: Spades
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
    
    def set_type(self, number):
        if number is None:
            return
        if number < 1:
            return
        if number > 4:
            return
        self.type = number
    
    def get_type(self) -> int:
        return self.type

    def get_type_as_string(self) -> str:
        if self.type == 1:
            return "Diamonds"
        if self.type == 2:
            return "Hearts"
        if self.type == 3:
            return "Clubs"
        if self.type == 4:
            return "Spades"
        return ""


    def to_string(self) -> str:
        return f"{self.get_number()} {self.get_type_as_string()}"
