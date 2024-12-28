import random # Imported Module needed for for shuffling Deck
import os # Imported Module to clear terminal


class Card : # indicates the start of a new class named Card.
    def __init__(self, name, suit, value):
        '''
         Represents a single playing card and designed to create 
         instances of playing cards, each with a name, suit, and value.
         self refers to the current instance of the class, allowing access to its properties.
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
        print("+---+")
        print(f"|{self.suit}  |")
        print(f"| {self.name} |")
        print(f"|  {self.suit}|")
        print("+---+")


