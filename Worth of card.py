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

#kollar om handen har fyrtal, kåk, triss dubbelpar eller par
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
            for y in range (0, len(temp_list)):
                if temp_list[y] == 2 and x != y:
                    return "dubbelpar"
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

# Rolyal flush returnerar True om det är en Royal flush
def is_royal_flush(hand,board):
    all_color = False
    all_cards = False
    royal_flush = False
    right_color = 4
    number_to_color = ["Hjärter", "Spader", "Klöver", "Ruter"]
    temp_list_color = (get_color_hand(hand, board))
# lista med färger
    temp_list = get_all_cards(hand, board)
# lista med alla kort
    for x in range (0, len(temp_list_color)):
        if temp_list_color[x] >= 5:
            all_color = True
            right_color = x
    if right_color < 4:
        right_color = number_to_color[right_color]
        if all_color:
            all_cards = (right_color, 1) in temp_list and (right_color, 13) in temp_list and (right_color, 12) in temp_list and (right_color, 11) in temp_list and (right_color, 10) in temp_list
    royal_flush = all_cards and all_color
    return royal_flush

# returnerar högsta valören som handen har om den inte har något annat
def highest_card(hand, board):
    temp_hand = get_counted_hand(hand, board)
    temp_tal = temp_hand.pop(0)
    temp_hand.append(temp_tal)
    for x in range (len(temp_hand)-1, 0, -1):
        if temp_hand[x] == 1:
            return x+2

# returnerar True om det är en straight flush
def is_straight_flush(hand, board):
    all_color = False
    all_cards = False
    straight_flush = False
    right_color = 4
    number_to_color = ["Hjärter", "Spader", "Klöver", "Ruter"]
    temp_list_color = (get_color_hand(hand, board))
# lista med färger
    temp_list = get_all_cards(hand, board)
# lista med alla kort
    for x in range (0, len(temp_list_color)):
        if temp_list_color[x] >= 5:
            all_color = True
            right_color = x
    if right_color < 4:
        right_color = number_to_color[right_color]
        if all_color:
            for x in range (1,10):
                if (right_color, x) in temp_list and (right_color, x+1) in temp_list and (right_color, x+2) in temp_list and (right_color, x+3) in temp_list and (right_color, x+4) in temp_list:
                    all_cards = True   
    straight_flush = all_cards and all_color
    return straight_flush

# returnerar True om det är en flush
def is_flush(hand, board):
    all_color = False
    flush = False
    temp_list_color = (get_color_hand(hand, board))
# lista med färger
    for x in range (0, len(temp_list_color)):
        if temp_list_color[x] >= 5:
            flush = True
    return flush

# returnerar True om det är en straight
def is_straight(hand, board):
    straight = False
    temp_list = numbers_hand_list(get_all_cards(hand, board))
    for x in range (1,10):
        if x in temp_list and x+1 in temp_list and x+2 in temp_list and x+3 in temp_list and x+4 in temp_list:
            straight = True
    return straight

# returnerar handens värde - lågt är bra
def hand_worth(hand, board):
    card = multiple_cards(hand, board)
    if is_royal_flush(hand,board):
        worth = 1
    elif is_straight_flush(hand, board):
        worth = 2
    elif card == "fyrtal":
        worth = 3
    elif card == "kåk":
        worth = 4
    elif is_flush(hand, board):
        worth = 5
    elif is_straight(hand, board):
        worth = 6
    elif card == "triss":
        worth = 7
    elif card == "dubbelpar":
        worth = 8
    elif card == "par":
        worth = 9
    else:
        worth = 10+highest_card(hand, board)
    return worth

# returnerar handen som är best
def best_hand(hand1, hand2, board):
    if hand_worth(hand1, board) < hand_worth(hand2, board):
        return hand1
    else:
        return hand2