from dataclasses import dataclass
##########################
# Types of value
#-------------------------
# 1: Diamonds
# 2: Hearts
# 3: Clubs
# 4: Spades
@dataclass(frozen=True)
class PokerCard2:
    number: int
    type: int

    def get_number(self) -> int:
        return self.number
    
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
