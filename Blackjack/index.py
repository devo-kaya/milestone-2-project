# MAIN SCRIPT for BLACK JACK GAME

import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight":8,
    "Nine": 9, "Ten": 10, "Jack": 10, "Queen":10, "King": 10, "Ace": 11
}

playing = True

class Card():
    
    # ranking ID
    def __init__(self, rank, suit):
    # card name
        self.rank = rank
    # character
        self.suit = suit
    # ranking or card ID
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # Creating the Card object here
                created_card = Card(rank, suit)
                    
                self.deck.append(created_card)
    
    def __str__(self):
        deck_comp = ''
        for rank in self.deck:
            deck_comp += '\n'+ rank.__str__()    
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        # Track the aces
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def takeBet(chips):
    while True:
        try:
            chips.bet = int(input(f"You have {chips.total} chips left. Choose your bet: "))
        
        except ValueError:
            print("Your bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
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
    

#Function to show cards on the deck

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
# Functions to deal with winning or losing scenario's
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
# Game Logic

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
    
    #Set up the player's chips
    player_chips = Chips()
    
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
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break