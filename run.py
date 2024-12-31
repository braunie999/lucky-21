import random # Imported Module needed for for shuffling Deck
import os # Imported Module to clear terminal


 # Represents a single playing card. 
class Card :
    '''
    Defines the Card class as well as initialises the card function
    '''
    def __init__(self, name, suit, value):
        '''
         Represents a single playing card and designed to create 
         instances of playing cards, each with a name, suit, and value.
         Self refers to the current instance of the class, allowing access to its properties.
        '''
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        '''
        In this __str__ method, it returns a formatted string with the object's 
        name and suit attributes using an f-string: f"{self.name} of {self.suit}".
        '''
        return f"{self.name} of {self.suit}"

    def print_card(self):
        '''
        The print_card method displays a simple representation of a playing card in the console, 
        showing its suit and name in a structured format.
        '''
        print("+---+")
        print(f"|{self.suit}  |")
        print(f"| {self.name} |")
        print(f"|  {self.suit}|")
        print("+---+")


 # Represents a full deck of cards 
class Deck: 
    def __init__(self):
        '''
        The Deck class has an initializer that creates an empty list to hold cards
        and calls a reset method to populate that list.
        This sets up the deck for further use in a card-related application. 
        '''
        self.cards = []
        self.reset()

    def reset(self):
        ''' Resets the deck by creating a new set of 52 cards (13 cards in each suit).'''
        self.cards.clear()
        values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]

        for i in range(len(values)):
            '''Loops through every suit and card value, creating a new Card and adding it to the deck.'''
            for suit in suits:
                self.cards.append(Card(names[i], suit, values[i]))

        self.shuffle()

    def shuffle(self):
        '''Shuffles the deck to randomize the order of the cards.'''
        random.shuffle(self.cards)

    def draw(self):
        '''Draws (removes) one card from the top of the deck.'''
        return self.cards.pop()


class Player:
    '''
    Represents a player in the game (you or the dealer).
    '''
    def __init__(self,name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        '''
        Adds a card to the player's hand.
        '''
        self.hand.append(card)

    def hand_value(self):
        '''
        Calculates the total value of the player's hand.
        Special Rule for Aces: If the total goes over 21 and 
        the player has an Ace, the Ace's value is reduced from 11 to 1.
        '''
        value = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.name == "A")

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value
    
    def is_busted(self):
        '''Checks if the player's total exceeds 21 (they "bust").'''
        return self.hand_value() > 21




