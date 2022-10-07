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
    
hand = [("dum", 1), ("hell", 1), ("james", 2), ("james", 2), ("james", 2), ("jefferson", 2)]
hand2 =[("dum", 3), ("hell", 3), ("james", 2), ("jefferson", 2),("james", 2), ("hell", 3), ("hell", 3)]
board = [("hello", 1)]
print(get_counted_hand(hand, board))
print(if_same_amount(hand, hand2, board))