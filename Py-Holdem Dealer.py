import random
playerNmbr = 3
master = {}
burnPile = []



def make_deck():
    Färg = ["Hjärter", "Spader", "Klöver", "Ruter"]
    Valör = list(range(1, 14))
    deck = []

    for färg in Färg:
        for valör in Valör:
            deck.append((färg,str(valör)))
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck



def gameLobby():
    notStarted = True
    while notStarted:
        pass



def emptyHands(playerNmbr):
    master["Board"] = []
    for i in range(playerNmbr):
        master[f"Player {i+1}"] = []
    return master



def dealCardsToPlayers(playerNmbr, dict):
    for i in range(playerNmbr):
        dealCard(list(dict.keys())[i+1])



def dealCard(hand):
    master[hand].append(deck.pop(0))



#Test + debugging
deck = shuffle(make_deck())
master = emptyHands(playerNmbr)
for _ in range(2):
    dealCardsToPlayers(playerNmbr, master)



input("")

for _ in range(3):
    dealCard(list(master.keys())[0])

print(master)

dealCard(list(master.keys())[0])

print(master)

dealcard(list(master.keys())[0])