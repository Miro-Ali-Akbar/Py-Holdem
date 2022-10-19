import random
from Worth_of_card import *

# spelare står som Player_tal eg Player_1, Player_2
# total antal spelare står som playerNmbr (2-10)


Färg = ["Hjärter", "Spader", "Klöver", "Ruter"]
Valör = list(range(1, 14))

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
    player_list.append(playerlist.pop(0))

# gör en deck med alla kort
def make_deck():
    deck = []
    for färg in Färg:
        for valör in Valör:
            deck.append((färg,str(valör)))
    return deck

# tar en deck och blandar den
def shuffle(deck):
    random.shuffle(deck)
    return deck

# ger en lista som ett deck varav korten är blandade. 
def get_deck():
    return shuffle(make_deck)
hand = [("Klöver", 9), ("Klöver", 2), ("Hjärter", 5), ("Hjärter", 7), ("Hjärter", 10)]
hand2 =[("Spader", 6), ("Hjärter", 13), ("Klöver", 2), ("Hjärter", 1),("Ruter", 5), ("Klöver", 9), ("Ruter", 12)]
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