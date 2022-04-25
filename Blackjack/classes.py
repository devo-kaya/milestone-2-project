import random

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight":8,
    "Nine": 9, "Ten": 10, "Jack": 10, "Queen":10, "King": 10, "Ace": 11
}

class State():
    
    def __init__(self,chips):
        
        self.chips = chips
        
    def __str__(self):
        return "Player has " + self.chips + " left"

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