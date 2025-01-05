'''
Modules needed to run Lucky 21 blackjack game
'''
import time
import random 
import os 

# Game Constants
MAX_SCORE = 21
DEALER_STAND_SCORE = 17
 

class Card:
        '''
         Represents a single playing card and designed to 
         create instances of playing cards, each with a name,
         suit, and value. Self refers to the current instance 
         of the class, allowing access to its properties.
        '''
        def __init__(self, name, suit, value):
            self.name = name
            self.suit = suit
            self.value = value

        def __str__(self):
            '''
            In this __str__ method, it returns a formatted 
            string with the object's name and suit attributes 
            using an f-string: f"{self.name} of {self.suit}".
            '''
            return f"{self.name} of {self.suit}"

        def print_card(self):
            """Displays the card in a simple visual format."""
            print("+---+")
            print(f"|{self.suit}  |")
            print(f"| {self.name} |")
            print(f"|  {self.suit}|")
            print("+---+")


class Deck: 
    '''
    The Deck class has an initializer that creates 
    an empty list to hold cards and calls a reset 
    method to populate that list.
    '''
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        '''
        Resets the deck by creating a new set of 52 cards .
        The use of the letter "T" is the face value for 10.  
        Original code from TokyoEdTech
        https://pastebin.com/WvmEtZDg
        '''
        self.cards.clear()
        values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]

        # Loops through every suit and card value, creating a new Card and adding it to the deck.
        for i, value in enumerate(values):
            for suit in suits:
                self.cards.append(Card(names[i], suit, value))
        self.shuffle()

    def shuffle(self):
        '''Shuffles the deck.'''
        random.shuffle(self.cards)

    def draw(self):
        '''Draws one card from the deck.'''
        return self.cards.pop()


# Calculates and prints cards in hand 
class Player:
    '''Represents a player in the game.'''
    def __init__(self,name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        '''Adds a card to the player's hand.'''
        self.hand.append(card)

    def hand_value(self):
        '''
        Calculates the total value of the player's hand.
        Special Rule for Aces: If the total goes over 21 
        and the player has an Ace, the Ace's value is 
        reduced from 11 to 1.
        '''
        value = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.name == "A")

        while value > MAX_SCORE and aces:
            value -= 10
            aces -= 1
        return value
    
    def print_hand(self):
        '''
        This function will visually mimic a hand of cards 
        by creating borders and displaying the suits and 
        names in a structured format, making it 
        easy to understand what cards are being held.
        '''
        print("\n" + " ".join(["+---+" for _ in self.hand]))
        print(" ".join([f"|{card.suit}  |" for card in self.hand]))
        print(" ".join([f"| {card.name} |" for card in self.hand]))
        print(" ".join([f"|  {card.suit}|" for card in self.hand]))
        print(" ".join(["+---+" for _ in self.hand]))

    def is_busted(self):
        '''Checks if the player's total exceeds 21 (they "bust").'''
        return self.hand_value() > MAX_SCORE

class BlackjackGame:
    '''Manages the State and logic of Lucky 21 Blackjack game.'''
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_wins = 0
        self.dealer_wins = 0
    
    # Displays current game state
    def print_game_state(self, player, dealer, hide_dealer_card=True):
        ''' 
        Clears the screen and displays the game status.
        If hide_dealer_card is True, one of the dealer's 
        cards is hidden.
        '''
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***********************************************")
        print("*   ♣ ♠ ♥ ♦ ~ Welcome to Lucky 21 ~ ♦ ♥ ♠ ♣   *")
        print("***********************************************")
    
        print(f"\n--- {dealer.name}'s Hand ---")
        '''
        This code is responsible for displaying the hands and 
        scores of both dealer and player. It conditionally 
        shows the dealer's card based on whether it should be 
        hidden, while always showing the player's hand value.
        '''
        if hide_dealer_card:
            print("[Hidden Card]")
            dealer.hand[1].print_card()
        else:
            dealer.print_hand()
            print(f"{dealer.name}'s Score: {dealer.hand_value()}")

        print(f"\n--- {player.name}'s Hand ---")
        player.print_hand()
        print(f"{player.name}'s Score: {player.hand_value()}")

        print("\n----------------------------")


    def print_scoreboard(self):  
        '''Displays the current scoreboard.'''  
        print(f"\nSCORE - {self.player_name}: {self.player_wins} | Dealer: {self.dealer_wins}")  


    def lucky_21(self):
        '''
        This is the main logic that runs the game.
        A new deck of cards is created and shuffled,
        and both the player and dealer get two cards.
        '''
        deck = Deck()
        player = Player(name=self.player_name)
        dealer = Player(name="Dealer")

        # Initial deal 
        for _ in range(2):
            player.add_card(deck.draw())
            dealer.add_card(deck.draw())

        # Check for Blackjack immediately after the initial deal
        if player.hand_value() == MAX_SCORE:
            time.sleep(1)
            self.print_game_state(player, dealer, hide_dealer_card=False)
            print(f"{player.name} hits Blackjack! {player.name} wins!")
            self.player_wins += 1  # Update player wins  
            self.print_scoreboard() 
            return
        if dealer.hand_value() == MAX_SCORE:
            time.sleep(1)
            self.print_game_state(player, dealer, hide_dealer_card=False)
            print("Dealer hits Blackjack! Dealer wins!")
            self.dealer_wins += 1  # Update dealer wins  
            self.print_scoreboard()
            return

        # Players turn 
        while True:
            self.print_game_state(player, dealer)
            if player.is_busted():
                time.sleep(0.2)
                print(f"{player.name} busts! Dealer wins.")
                self.dealer_wins += 1
                self.print_scoreboard()
                return
            
            if len(player.hand) == 5:
                '''Player wins if they draw 5 cards without busting.'''
                self.print_game_state(player, dealer, hide_dealer_card=False)
                print(f"{player.name} wins by drawing 5 cards without busting!")
                self.player_wins += 1
                self.print_scoreboard()
                return

            while True:
                choice = input("Would you like to [H]it or [S]tand ?:\n").lower()
                if choice in ['h', 's',]:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print("Input invalid. Enter 'H' to hit or 'S' to stand.")

            if choice == 'h':
                time.sleep(0.2)
                player.add_card(deck.draw())
            else:
                break

        # Dealer's turn
        '''
        The dealer logic uses a while True loop to make it 
        easier to read. It checks the dealer's hand value 
        once per turn to decide whether to hit, clarifying 
        the drawing rules and improving performance.
        '''
        while True:
            if dealer.hand_value() < DEALER_STAND_SCORE:
                dealer.add_card(deck.draw())
            elif dealer.hand_value() == 17 and any(card.name == 'A' for card in dealer.hand):
                dealer.add_card(deck.draw())
            else:
                break
            
            if len(dealer.hand) == 5:
                self.print_game_state(player, dealer, hide_dealer_card=False)
                print("Dealer wins by drawing 5 cards without busting!")
                self.dealer_wins += 1
                self.print_scoreboard()
                return

        self.print_game_state(player, dealer, hide_dealer_card=False)

        # Determine the winner of round
        if dealer.is_busted():
            print(f"Dealer busts! {player.name} wins!")
            self.player_wins += 1
        elif player.hand_value() > dealer.hand_value():
            print(f"{player.name} wins!")
            self.player_wins += 1
        elif dealer.hand_value() > player.hand_value():
            print("Dealer wins!")
            self.dealer_wins += 1
        else:
            # Tie-breaker logic
            if len(player.hand) < len(dealer.hand):
                print(f"{player.name} wins by having fewer cards!")
                self.player_wins += 1
            elif len(player.hand) > len(dealer.hand):
                print("Dealer wins by having fewer cards!")
                self.dealer_wins += 1
            else:
                print("It's a tie!")

        self.print_scoreboard()

# Game insructions
def show_instructions():
    os.system("clear")
    print("""
    **************************************************
    *              HOW TO PLAY LUCKY 21              *
    **************************************************
    - The goal is to get as close to 21 as possible without exceeding it.
    - Number cards (2-10/T) are worth their face value.
    - Face cards (K, Q, J) are worth 10 points each.
    - Aces are worth 11 or 1, depending on what benefits you.
    - Type 'H' to Hit (draw a card).
    - Type 'S' to Stand (keep your current hand).
    - The dealer must draw until reaching at least 17.
    - If you go over 21, you bust and lose the game.
    - If the dealer goes over 21, the dealer busts and you win.
    - If both you and the dealer stand, the hand closest to 21 wins.
    - In case of a tie, the game is a draw.
    **************************************************
    """)
    input("Press Enter to continue...\n")
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Game loop
if __name__ == "__main__":
    os.system("clear")
    show_instructions() 
    while True:
        player_name = input("Enter your name to play:\n").strip()
        if player_name:
            player_name = player_name.capitalize()
            time.sleep(0.5)
            break
        else:
            print("Name cannot be empty. Please enter your name.")

    game = BlackjackGame(player_name)

    while True:
        game.lucky_21()  
        while True:
            play_again = input("Press ENTER to continue or type 'Q' to quit: ").upper()
            if play_again in ['', 'Q']:
                time.sleep(0.5)
                break
            else:
                print("Invalid input. Please press ENTER to continue or type 'Q' to quit.")
        if play_again == 'Q':
            print(f"THANKS FOR PLAYING, {player_name}!".upper())
            break