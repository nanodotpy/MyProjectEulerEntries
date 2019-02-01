with open('Problem 54.txt') as file:                                   #Hard coded way too much but it perfectly works in ALL cases uWu
    player1 = [x.strip()[:14] for x in file]
   
with open('Problem 54.txt') as file:
    player2 = [x.strip()[15:] for x in file]
 
player1 = [[a.split(' ')] for a in player1]
player2 = [[a.split(' ')] for a in player2]
 
cardsentities = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['D', 'H', 'C', 'S']
 
#-------------------------------------------------------------------------------------------------------------------
 
def sortcards(liste):
    entities = [liste[0][a] for a in range(5)]
    entities = [str(card[0]) for card in entities]
    n = len(entities)
    for i in range(n):
        for j in range(n-i-1):
            if cardsentities.index(entities[j]) > cardsentities.index(entities[j+1]):
                entities[j], entities[j+1] = entities[j+1], entities[j]
    return entities
 
#--------------------------------------------------------------------------------------------------------------------
 
def pairs(liste):
    entities = sortcards(liste)
    lespairs = set()
    for number in entities:
        if entities.count("{}".format(number)) == 2:
            lespairs.add(number)
   
    return list(lespairs)
 
def three(liste):
    entities = sortcards(liste)
    lesthree = set()
    for number in entities:
        if entities.count("{}".format(number)) == 3:
            lesthree.add(number)
    if lesthree != set():
        return list(lesthree)
 
def straight(liste):
    entities = sortcards(liste)
    index0 = cardsentities.index(entities[0]) 
    if entities == ['2', '3', '4', '5', 'A'] :
        return True
    try:
        for a in range(1,len(entities)):
            if not entities[a] == cardsentities[index0 + a]:
                break
        else:
            return True
    except (ValueError, IndexError):
        return None
   
def flush(liste):
    entitiessuits = [liste[0][a][1] for a in range(5)]
    for a in range(5):
        if not entitiessuits[a] == entitiessuits[a-1]:
            break
    else :
        return True
 
def full_house(liste):
    try :
        if len(pairs(liste)) == 1 and len(three(liste)) == 1 :
            return True
    except :
        pass
   
def four_of_kind(liste):
    entities = sortcards(liste)
    four = set()
    for number in entities:
        if entities.count("{}".format(number)) == 4:
            four.add(number)
    if four != set():
        for a in four:
            return a
   
def straight_flush(liste):
    if straight(liste) and flush(liste):
        return True
 
def royal_flush(liste):
    if flush(liste):
        entities = sortcards(liste)
        royal = ['T', 'J', 'Q', 'K', 'A']
        for card in entities:
            if card not in royal:
                break
        else:
            return True
       
#---------------------------------------------------------------------------------------------------------------
 
def win_rf(hand1,hand2):
    if royal_flush(hand1) and not royal_flush(hand2):
        return 1  
    elif royal_flush(hand2) and not royal_flush(hand1):
        return 2
    elif royal_flush(hand1) and royal_flush(hand2):
        return 3
   
def win_sf(hand1,hand2):
    if straight_flush(hand1) and not straight_flush(hand2):
        return 1
    elif straight_flush(hand2) and not straight_flush(hand1):
        return 2
    elif straight_flush(hand2) and straight_flush(hand1) :
        return 3
       
def win_four_of_kind(hand1,hand2):
    if four_of_kind(hand1) is not None and four_of_kind(hand2) is None:
        return 1
    if four_of_kind(hand2) is not None and four_of_kind(hand1) is None :
        return 2
    if four_of_kind(hand1) is not None and four_of_kind(hand2) is not None:
        if cardsentities.index(four_of_kind(hand1)) > cardsentities.index(four_of_kind(hand2)):
            return 1
        elif cardsentities.index(four_of_kind(hand1)) < cardsentities.index(four_of_kind(hand2)):
            return 2
        else :
            return 3
 
def win_full_house(hand1,hand2):
   
    if full_house(hand1) and not full_house(hand2):
        return 1
    elif full_house(hand2) and not full_house(hand1):
        return 2
    elif full_house(hand2) and full_house(hand1):
        if cardsentities.index(pairs(hand1)[-1]) > cardsentities.index(pairs(hand2)[-1]):
            return 1
        elif cardsentities.index(pairs(hand2)[-1]) > cardsentities.index(pairs(hand1)[-1]):
            return 2
        elif pairs(hand2)[-1] == pairs(hand1)[-1] :
            return 3
       
def win_flush(hand1,hand2):
    if flush(hand1) and not flush(hand2):
        return 1
    elif flush(hand2) and not flush(hand1):
        return 2
    elif flush(hand1) and flush(hand2):
        return 3
 
def win_straight(hand1,hand2):
    if straight(hand1) and not straight(hand2):
        return 1
    elif straight(hand2) and not straight(hand1):
        return 2
    elif straight(hand1) and straight(hand2):
        return 3
 
def win_three(hand1,hand2):
    if three(hand1) is not None and three(hand2) is None :
        return 1
    if three(hand2) is not None and three(hand1) is None :
        return 2
    if three(hand2) is not None and three(hand1) is not None :
        if cardsentities.index(three(hand1)[-1]) > cardsentities.index(three(hand2)[-1]):
            return 1
        elif cardsentities.index(three(hand1)[-1]) < cardsentities.index(three(hand2)[-1]):
            return 2
        else :
            return 3
       
def win_pairs(hand1,hand2):
    if len(pairs(hand1)) == 0 and len(pairs(hand2)) ==  0:
        return None
   
    if len(pairs(hand1)) != 0 and len(pairs(hand2)) == 0:
        return 1
    elif len(pairs(hand2)) != 0 and len(pairs(hand1)) == 0:
        return 2
    elif len(pairs(hand1)) > len(pairs(hand2)):
        return 1
    elif len(pairs(hand2)) > len(pairs(hand1)):
        return 2
    elif cardsentities.index(pairs(hand1)[-1]) > cardsentities.index(pairs(hand2)[-1]):
        return 1
    elif cardsentities.index(pairs(hand1)[-1]) < cardsentities.index(pairs(hand2)[-1]):
        return 2
    try :
        if cardsentities.index(pairs(hand1)[-2]) < cardsentities.index(pairs(hand2)[-2]):
            return 2
        if cardsentities.index(pairs(hand1)[-2]) > cardsentities.index(pairs(hand2)[-2]):
            return 1
    except:
        if cardsentities.index(pairs(hand1)[-1]) ==  cardsentities.index(pairs(hand2)[-1]) :
            return 3
        if cardsentities.index(pairs(hand1)[-1]) ==  cardsentities.index(pairs(hand2)[-1]) and cardsentities.index(pairs(hand1)[-2]) ==  cardsentities.index(pairs(hand2)[-2]) :
            return 3
       
def win_high_card(hand1,hand2):
    for a in range(4,-1,-1):
        if cardsentities.index(sortcards(hand1)[a]) >  cardsentities.index(sortcards(hand2)[a]):
            return 1
        elif cardsentities.index(sortcards(hand1)[a]) < cardsentities.index(sortcards(hand2)[a]):
            return 2
 
def winner(hand1,hand2):
   
    if win_rf(hand1,hand2) is not None :
        if win_rf(hand1,hand2) == 3 :
            return win_high_card(hand1,hand2)
        else :
            return win_rf(hand1,hand2)
    if win_sf(hand1,hand2) is not None :
        if win_sf(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_sf(hand1,hand2)
    if win_four_of_kind(hand1,hand2) is not None :
        if win_four_of_kind(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_four_of_kind(hand1,hand2)
    if win_full_house(hand1,hand2) is not None:
        if win_full_house(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_full_house(hand1,hand2)
    if win_flush(hand1,hand2) is not None :
        if win_flush(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_flush(hand1,hand2)
    if win_straight(hand1,hand2) is not None :
        if win_straight(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_straight(hand1,hand2)
    if win_three(hand1,hand2) is not None :
        if win_three(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_three(hand1,hand2)
    if win_pairs(hand1,hand2) is not None :
        if win_pairs(hand1,hand2) == 3:
            return win_high_card(hand1,hand2)
        else :
            return win_pairs(hand1,hand2)
       
    return win_high_card(hand1,hand2)
 
total = 0


for a in range(len(player1)) :
    if winner(player1[a],player2[a]) == 1 :
        total += 1
           
print(total)


