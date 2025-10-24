from PokerCard2 import PokerCard2
from deck import Deck
from enums import CardSuit, Color



deck1 = Deck()
deck1.create_deck()
deck2 = Deck()
deck2.create_deck()
deck1.shuffle_deck()
print(deck1.deal_card())
deck1.deal_card()
deck1.deal_card()
deck1.deal_card()
deck1.deal_card()
