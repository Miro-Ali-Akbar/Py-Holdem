import random

Färg = ["Hjärter", "Spader", "Klöver", "Ruter"]
Valör = list(range(2, 11)) + ["Ess", "Knekt", "Dam", "Kung"]

def make_deck():
    deck = []
    for färg in Färg:
        for valör in Valör:
            deck.append((färg,str(valör)))
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck