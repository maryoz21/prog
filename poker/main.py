from PokerCard2 import PokerCard2
from deck import Deck
from enums import CardSuit, Color


card1 = PokerCard2(10, CardSuit.HEARTS)


print(card1.to_string())