# MAIN SCRIPT for BLACK JACK GAME
from classes import Deck, Hand, Chips
from functions import takeBet, hit, show_all, show_some, player_busts, player_wins, dealer_busts, dealer_wins, push

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
    

# Game Logic

#Set up the player's chips
## if you don't do this outside of the while loop then the total chips gets reset when you play another round
player_chips = Chips()
playing = True

while True:
    # Print an opening statement
    print("Welcome to Black Jack\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11")
    
    # Create & shuffle the deck deal two cards
    deck = Deck()
    deck.shuffle()
    
    #Create player
    player_hand = Hand()
    #Give player two cards from the get go
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    #Create dealer
    dealer_hand = Hand()
    
    #Give dealer two cards from the get go
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #Ask player input for placing a bet
    takeBet(player_chips)
    
    #Show cards
    show_some(player_hand,dealer_hand)
    
    while playing: #recall this variable from our hit_or_stand function
        #Prompt player to hit or stand
        hit_or_stand(deck,player_hand)
        
        #Show cards but keep dealer hidden
        show_some(player_hand,dealer_hand)
        
        #if player's hand exceeds 21, run player_busts and break loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            
            break
        # if player not busted, play dealers hand until reaching 17
        show_all(player_hand,dealer_hand)
        
        #All different scenario's
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)      
            
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if player_chips.total <= 0:
        print("You don't have chips anymore! Thanks for playing!")
        break
    elif new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break