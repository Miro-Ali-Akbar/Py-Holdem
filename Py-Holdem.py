import random
from Worth_of_card import *

Färg = ["Hjärter", "Spader", "Klöver", "Ruter"]
Valör = list(range(1, 14))


def make_deck():
    deck = []
    for färg in Färg:
        for valör in Valör:
            deck.append((färg, str(valör)))
    return deck


def shuffle(deck):
    random.shuffle(deck)
    return deck


def get_deck():
    return shuffle(make_deck)


hand = [("Klöver", 9), ("Klöver", 2), ("Hjärter", 5), ("Hjärter", 7), ("Hjärter", 10)]
hand2 = [("Spader", 6), ("Hjärter", 13), ("Klöver", 2), ("Hjärter", 1), ("Ruter", 5), ("Klöver", 9), ("Ruter", 12)]
board = [("Klöver", 8)]
print(get_counted_hand(hand, board))
print(multiple_cards(hand, board))
print(get_counted_hand(hand2, board))
print(multiple_cards(hand2, board))
print(get_color_hand(hand, board))
print(numbers_color_list(hand))
print(is_straight(hand, board))
print(hand_worth(hand, board))
print(hand_worth(hand2, board))
print(best_hand(hand, hand2, board))
