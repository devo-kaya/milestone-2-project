from posixpath import split
from functions import checkWarDeck, splitDeck, checkPlayerDeck, addThreeCards, pullCardfromDeck, checkRanking
from classes import  Deck, Player

# Game Logic

#Create new instance of card deck
deck_of_cards = Deck()
deck_of_cards.shuffle()
len(deck_of_cards.all_cards)

# Create new player instances
Player_One = Player("Barbara")
Player_Two = Player("Artjom")


# Split the deck equally    
splitDeck(deck_of_cards,Player_One,Player_Two)
    

round_num = 0
game_on = True

'''Start while loop'''

while game_on:

    round_num += 1
    print(f"round {round_num}")
    
# Define the card on the deck per player
    player1_list = []
    player2_list = []

    if round_num > 1000:
        print("The game goes on for too long! It is a draw!")
        game_on = False
#Check if any player is out of cards completely
    if checkPlayerDeck(Player_One,Player_Two) == True:
        game_on = False
    else:
        at_war = True
        
        while at_war:
            
            if checkRanking(Player_One, Player_Two, player1_list, player2_list) == True:
                at_war = False
            else:
                print("IT. IS. WAR!!!")    
                if checkWarDeck(Player_One,Player_Two) == True:
                    
                    game_on = False
                    
                else:
                    for num in range(5):
                        try:
                            player1_list.append(Player_One.remove_one())
                            player2_list.append(Player_Two.remove_one())
                        except:
                            print("The game is over!")