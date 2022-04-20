import random 

#Define global data
names = (
    "Two", "Three", "Four", "Five", "Six", "Seven", 
    "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"
    )
ranks = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight":8,
    "Nine": 9, "Ten": 10, "Jack": 11, "Queen":12, "King": 13, "Ace": 14
}
suits = ("Hearts","Diamonds","Clubs","Spades")

#Card class
class Card():
    # ranking ID
    def __init__(self, name, suit):
    # card name
        self.name = name
    # character
        self.suit = suit
    # ranking or card ID
        self.value = ranks[name]
    def __str__(self):
        return self.name + ' of ' + self.suit
    
#Deck class
class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for name in names:
            for suit in suits:
                    # Creating the Card object here
                created_card = Card(name, suit)
                    
                self.all_cards.append(created_card)
    # Shuffle the deck of cards            
    def shuffle(self):
        random.shuffle(self.all_cards)
    # method to deal a card to play
    def deal_one(self):
        return self.all_cards.pop()

# player Class
class Player:
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #When the player needs to add multiple cards
            self.all_cards.extend(new_cards)
        else:
            #When the player only needs to add one card
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards!'