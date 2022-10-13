import random

Färg = ["Hjärter", "Spader", "Klöver", "Ruter"]
Valör = list(range(1, 14))

def make_deck():
    deck = []
    for färg in Färg:
        for valör in Valör:
            deck.append((färg,str(valör)))
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def get_deck():
    return shuffle(make_deck)


# sätta i hopp alla kort till en lista
def get_all_cards(player_hand, board):
    temp_list = player_hand + board
    return temp_list

# returnerar lista med alla siffror från en hand
def numbers_hand_list(temp_list):
    hand_list = []
    for x in range (0,len(temp_list)):
        hand_list.append(temp_list[x][1])
    return hand_list

# räknar antal samma kort i handen
def count_hand(hand_list):
    card_list = 13*[0]
    for x in range (0, len(hand_list)):
        card_list[hand_list[x]-1] += 1
    return card_list

# sätter ihopp alla de övre funtionerna, tar in listorna handen och board returnar lista med antal av varje värde
def get_counted_hand(player_hand, board):
    return count_hand(numbers_hand_list(get_all_cards(player_hand, board)))

# returnerar lista med alla färger från en hand
def numbers_color_list(temp_list):
    hand_list = []
    for x in range (0,len(temp_list)):
        hand_list.append(temp_list[x][0])
    return hand_list

# räknar alla färger
# returnerar en lista med antal av varje färg [Hjärter, Spader, Klöver, Ruter]
def color_hand(hand_list):
    card_list = 4*[0]
    for x in hand_list:
        if x == "Hjärter":
            card_list[0] += 1
        elif x == "Spader":
            card_list[1] += 1
        elif x == "Klöver":
            card_list[2] += 1
        elif x == "Ruter":
            card_list[3] += 1
    return card_list

# sätter ihopp alla de övre funtionerna, tar in listorna handen och board returnar lista med antal av varje färg
def get_color_hand(player_hand, board):
    return color_hand(numbers_color_list(get_all_cards(player_hand, board)))

#kollar om handen har fyrtal, kåk, triss eller par
def multiple_cards(player_hand, board):
    temp_list = get_counted_hand(player_hand, board)
    for x in range (0, len(temp_list)):
        if temp_list[x] == 4:
            return "fyrtal"
    for x in range (0, len(temp_list)):
        if temp_list[x] == 3:
            for x in range (0, len(temp_list)):
                if temp_list[x] == 2:
                    return "kåk"
            return "triss"
    for x in range (0, len(temp_list)):
        if temp_list[x] == 2:
            return "par"

# Tar två händer som båda har fyrtal, kåk, triss eller par och bestämmer vem som har bäst
# returnerar true om hand 1 är en bättre hand än två
def if_same_amount(hand1, hand2, board):
    first_player = get_counted_hand(hand1, board)
    second_player = get_counted_hand(hand2, board)
# första handens värde
    hand = multiple_cards(hand1, board)
    if hand == "fyrtal":
        best_hand1 = first_player.index(4)
    elif hand == "kåk":
        best_hand1 = first_player.index(3)
    elif hand == "triss":
        best_hand1 = first_player.index(3)
    elif hand == "par":
        best_hand1 = first_player.index(2)
# andra handens bästa värde
    second_hand = multiple_cards(hand2, board)
    if second_hand == "fyrtal":
        best_hand2 = second_player.index(4)
    elif second_hand == "kåk":
        best_hand2 = second_player.index(3)
    elif second_hand == "triss":
        best_hand2 = second_player.index(3)
    elif second_hand == "par":
        best_hand2 = second_player.index(2)
# får vilken valör som var högst för varje hand
    if best_hand1 == 0:
        return True
    elif best_hand2 == 0:
        return False
    elif best_hand1 > best_hand2:
        return True
    else:
        return False
'''
# Rolyal flush returnerar True om det är en Royal flush
def is_royal_flush(hand,board):
    all_color = False
    all_cards = True
    royal_flush = False
    right_color = 4
    temp_list_color = (get_color_hand(hand, board))
# lista med färger
    temp_list_number = (get_counted_hand(hand, board))
    temp_list_number.append(temp_list_number.pop(0))
# lista med siffror varav ess är sist
    for x in temp_list_color:
        if x == 5:
            all_color = True
            right_color = templist[x]
    if all_color == True:
        for x in range (9, 13):
            if temp_list_number[x] != 1 :
                all_cards = False
    return royal_flush
'''
# returnerar högsta valören som handen har om den inte har något annat
def highest_card(hand, board):
    temp_hand = get_counted_hand(hand, board)
    temp_tal = temp_hand.pop(0)
    temp_hand.append(temp_tal)
    for x in range (len(temp_hand)-1, 0, -1):
        if temp_hand[x] == 1:
            return x+2


hand = [("Hjärter", 1), ("Spader", 1), ("Spader", 2), ("Klöver", 2), ("Ruter", 2), ("Ruter", 2)]
hand2 =[("Spader", 3), ("Hjärter", 3), ("Klöver", 2), ("Hjärter", 2),("Ruter", 2), ("Klöver", 3), ("Ruter", 3)]
board = [("Hjärter", 1)]
print(get_counted_hand(hand, board))
print(multiple_cards(hand, board))
print(get_counted_hand(hand2, board))
print(multiple_cards(hand2, board))
print(get_color_hand(hand, board))
print(numbers_color_list(hand))