import random
from Worth_of_card import *

playerNmbr = 3
master = {}
burnPile = []

'''
-----------
Game start:
-----------
Bestäm antal spelare gör make_money_dictionary och gör lista på antal spelare med _make_player_list

----------
RoundStart
----------
Make deck with getdeck()
vinstpengar = 0
________
Startbet: 
alla startpengar dras från dictionarin med pengar läggs i vinstpengar
__________________________________________________________
Deal 2 cards to all players player_1 to player_playerNmber:
pop kort i deck
____________
Betting time
_____________________
Deal 3 cards to board
pop kort i deck
____________
Betting time
______________________________________
One more card to board to a total of 4
pop kort i deck
____________
Betting time
______________________________________
One more card to board to a total of 5
pop kort i deck
____________
Betting time

Händer jämförs och spelaren med vinnarens hand får vinstpengar via best_hand

__________
Round over

Om bara en sperare har pengar vinner den

----------------------------------------
____________
Betting time

Alla går runt och bettar via ordern rotate_order lista där första spelaren väljer summa pengar att betta.

summan kontorleras att finnas i listan -spelaren har råd att betta

(går till nästa samma mänsika som får välja att calla, maxbet, höja maxbet eller fold)*playerNmbr

när alla har callat maxbet eller fold så går spelet vidare

_____
Extra

om en spelare har mindre pengar än startbet så förlorar den och pengar sätts till 0.

om maxbet är över Player_x pengar kan hen call ändå. - call behövs inte kontrolleras om player har tillräckligt med pengar. Bara med att höja maxbet

'''

# spelare står som Player_tal eg Player_1, Player_2
# total antal spelare står som playerNmbr (2-10)

# gör en dictionary som har {Player_1 : money_max, ... till Player_playerNmbr : money_max}
def make_money_dictionary(playerNmber, money_max):
    list_of_money = {}
    for x in range (1, playerNmber+1):
        player = "Player_" +str(x)
        list_of_money[player] = money_max
    return list_of_money

# gör en lista av alla spelare
def make_player_list(playerNmber):
    player_list = []
    for x in range (1, playerNmber+1):
        player = "Player_" +str(x)
        player_list.append(player)
    return player_list
    
# ändar värdet på money för key, player från dictionarien
def change_money(list_of_money, player, money):
    temp_money = list_of_money[player]
    list_of_money[player] = temp_money + money

# Roterar en lista för att gå runt i betting
def rotate_order_list(player_list):
    player_list.append(player_list.pop(0))

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

dealCard(list(master.keys())[0])