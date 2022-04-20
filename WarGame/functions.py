

#Splitting the deck equally to both players
def splitDeck(deck,pl1,pl2):
    middle_index = 26
    list_one = deck.all_cards[:middle_index]
    list_two = deck.all_cards[middle_index:]
    
    #Add the splitted deck to each player
    pl1.add_cards(list_one)
    pl2.add_cards(list_two)
    
# Function to check whether someone has lost already. 0 Cards left   
def checkPlayerDeck(player1,player2):
    if len(player1.all_cards) == 0:
        return True and print(f"{player1.name} has 0 cards left! {player2.name} Wins!")
    elif len(player2.all_cards) == 0:
        return True and print(f"{player2.name} has 0 cards left! {player1.name} Wins!")
    
def checkWarDeck(player1,player2):
    if len(player1.all_cards) < 5:
        return True and print(f"{player1.name} cannot go to war! {player2.name} Wins!")
    elif len(player2.all_cards) < 5:
        return True and print(f"{player2.name} cannot go to war! {player1.name} Wins!")
    else:
        return False
    
def addThreeCards(player):
    three_cards = [1,2,3]
    list1 = []
    
    for card in three_cards:
        list1 = player.remove_one(card)
        
    return list1

def pullCardfromDeck(player):
    card =  player.remove_one()
    return card
    
# Function to check which card has a higher ranking
def checkRanking(pl1, pl2, list1,list2):
    
    list1.append(pl1.remove_one())
    list2.append(pl2.remove_one())
    
    if list1[-1].value > list2[-1].value:
        pl1.add_cards(list1)
        pl1.add_cards(list2)
        return True        
    elif list2[-1].value > list1[-1].value:
        pl2.add_cards(list1)
        pl2.add_cards(list2)
        return True    
