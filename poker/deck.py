from dataclasses import dataclass, field
import random
from PokerCard2 import PokerCard2
from enums import CardSuit, Color
@dataclass
class Deck:
    deck: list[PokerCard2] = field(default_factory=list)

    def create_deck(self):
        self.deck = []
        for suit in [CardSuit.DIAMONDS, CardSuit.HEARTS, CardSuit.CLUBS, CardSuit.SPADES]:
            for number in range(1, 14):
                self.deck.append(PokerCard2(number, suit))
        
    def generate_random_number(self) -> int:
        numero = random.randint(0, len(self.deck)-2)
        return numero
    
    def move_card_to_last(self, index):
        card = self.deck.pop(index)     
        self.deck.append(card)

    def shuffle_deck(self):
        if len(self.deck) < 2:
            return
        for i in range (1000):
            index = self.generate_random_number()
            self.move_card_to_last(index)

    def deal_card(self):
        if len(self.deck) > 0:
            index = len(self.deck)-1
            card = self.deck.pop(index)
            return card
        

    