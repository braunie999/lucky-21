'''
Modules needed to run Lucky 21 blackjack game
'''
import random 
import os 


# Global variables to keep track of scores  
player_wins = 0  
dealer_wins = 0  

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
        '''
        Resets the deck by creating a new set of 52 cards (13 cards in each suit).
        The use of the letter "T" is to indiate the card suit and  value of 10 without 
        disrupting the visual print out of the card in the terminal.  
        Original code from TokyoEdTech
        https://pastebin.com/WvmEtZDg
        '''
        self.cards.clear()
        values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]

        for i in range(len(values)):
            '''
            Loops through every suit and card value, creating a new Card and adding it to the deck.
            '''
            for suit in suits:
                self.cards.append(Card(names[i], suit, values[i]))

        self.shuffle()

    def shuffle(self):
        '''
        Shuffles the deck to randomize the order of the cards.
        '''
        random.shuffle(self.cards)

    def draw(self):
        '''
        Draws (removes) one card from the top of the deck.
        '''
        return self.cards.pop()


# Calculates and prints cards in hand 
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
    
    def print_hand(self):
        '''
        This function will visually mimic a hand of cards by creating borders 
        and displaying the suits and names in a structured format, making it 
        easy to understand what cards are held.
        '''
        print("\n" + " ".join(["+---+" for _ in self.hand]))
        print(" ".join([f"|{card.suit}  |" for card in self.hand]))
        print(" ".join([f"| {card.name} |" for card in self.hand]))
        print(" ".join([f"|  {card.suit}|" for card in self.hand]))
        print(" ".join(["+---+" for _ in self.hand]))

    def is_busted(self):
        '''Checks if the player's total exceeds 21 (they "bust").'''
        return self.hand_value() > 21


# Game layout in mock terminal
def print_game_state(player, dealer, hide_dealer_card=True):
    ''' 
    Clears the screen and displays the game status.
    If hide_dealer_card is True, one of the dealer's cards is hidden.
    '''
    os.system('clear')
    print("***********************************************")
    print("*** ♣ ♠ ♥ ♦ ~Welcome to Lucky 21 !~ ♦ ♥ ♠ ♣ ***")
    print("***********************************************")
    '''
    This code is responsible for displaying the hands and scores of both a dealer 
    and a player in the card game. It conditionally shows the dealer's card based 
    on whether it should be hidden, while always showing the player's hand and score.
    The use of methods like print_hand() and hand_value() implies that both the dealer 
    and player have card management and value calculation functionalities encapsulated 
    in their respective classes.
    '''
    print(f"\n--- {dealer.name}'s Hand ---")
    if hide_dealer_card:
        print("[Hidden Card]")
        dealer.hand[1].print_card()
    else:
        dealer.print_hand()
        print(f"{dealer.name}'s Score: {dealer.hand_value()}")

    print(f"\n--- {player.name}'s Hand ---")
    player.print_hand()
    print(f"{player.name}'s Score: {player.hand_value()}")


def print_scoreboard(player_name):  
    '''Displays the current scoreboard.'''  
    print(f"\nScoreboard - {player_name}: {player_wins} | Dealer: {dealer_wins}")  


def lucky_21(player_name):
    '''
    This is the main logic that runs the game.
    Creates a Deck, A new deck of cards is created and shuffled.
    Deals Cards, both the player and dealer get two cards.
    Player's Turn, the player decides whether to hit (draw another card) or stand (keep their hand).
    Dealer's Turn, the dealer must keep drawing cards until their total is 17 or higher.
    '''
    global player_wins, dealer_wins

    os.system("clear")
    deck = Deck()
    player = Player(name=player_name)
    dealer = Player(name="Dealer")


    # Initial deal 
    for _ in range(2):
        player.add_card(deck.draw())
        dealer.add_card(deck.draw())

    # Check for Blackjack immediately after the initial deal
    if player.hand_value() == 21:
        print_game_state(player, dealer, hide_dealer_card=False)
        print(f"{player.name} hits Blackjack! {player.name} wins!")
        player_wins += 1  # Update player wins  
        print_scoreboard(player_name) 
        return
    if dealer.hand_value() == 21:
        print_game_state(player, dealer, hide_dealer_card=False)
        print("Dealer hits Blackjack! Dealer wins!")
        dealer_wins += 1  # Update dealer wins  
        print_scoreboard(player_name)
        return

    # Players turn 
    while True:
        print_game_state(player, dealer)
        if player.is_busted():
            print(f"{player.name} busts! Dealer wins.")
            dealer_wins += 1
            print_scoreboard(player_name)
            return

        while True:
            choice = input("Would you like to [H]it or [S]tand ?:\n").lower()
            if choice in ['h', 's', 'q']:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Input invalid. Please enter 'H' to hit or 'S' to stand.")

        if choice == 'h':
            player.add_card(deck.draw())
        else:
            break


    # Dealer's turn
    '''
    The dealer logic uses a while True loop for better readability, 
    checking the dealer's hand value just once per iteration to determine 
    whether to hit. By separating the conditions for drawing cards, it 
    clarifies the rules and enhances the performance of the dealer's 
    turn in the game.
    '''
    while True:
        dealer_hand_value = dealer.hand_value()
        if dealer_hand_value < 17:
            dealer.add_card(deck.draw())
        elif dealer_hand_value == 17 and any(card.name == 'A' for card in dealer.hand):
            dealer.add_card(deck.draw())
        else:
            break
        
    print_game_state(player, dealer, hide_dealer_card=False)

    # Determine the winner of round
    if dealer.is_busted():
        print(f"Dealer busts! {player.name} wins!")
        player_wins += 1
    elif player.hand_value() > dealer.hand_value():
        print(f"{player.name} wins!")
        player_wins += 1
    elif dealer.hand_value() > player.hand_value():
        print("Dealer wins!")
        dealer_wins += 1
    elif player.hand_value() == dealer.hand_value():
        if len(player.hand) < len(dealer.hand):
            print(f"{player.name} wins with fewer cards!")
            player_wins += 1 
        else:
            print("It's a tie!")

    print_scoreboard(player_name)

# Game insructions
def show_instructions():
    os.system("clear")
    print("""
    **************************************************
    *              HOW TO PLAY LUCKY 21              *
    **************************************************
    - The goal is to get as close to 21 as possible without exceeding it.
    - Face cards (K, Q, J) are worth 10, as well as T cards.
    - Aces are worth 11 or 1, depending on what benefits you.
    - Type 'H' to Hit (draw a card).
    - Type 'S' to Stand (keep your current hand).
    - The dealer must draw until reaching at least 17.
    **************************************************
    """)
    input("Press Enter to continue...\n")


# Main Game loop
if __name__ == "__main__":
    os.system("clear")
    show_instructions() 
    while True:
        player_name = input("Enter your name to play:\n").strip()
        if player_name:
            player_name = player_name.capitalize()
            break
        else:
            print("Name cannot be empty. Please enter your name.")

    # Play the game, but don't show instructions again
    while True:
        lucky_21(player_name)  
        play_again = input("Press ENTER to continue or type 'Q' to quit.").upper()
        if play_again == 'Q':
            print(f"Thanks for playing, {player_name}!".upper())
            break