# Lucky 21 Blackjack Game

## Overview

Lucky 21 is a simple command-line-based blackjack game where players compete against a dealer. The goal is to get as close to 21 as possible without exceeding it. The game features standard blackjack rules, including the handling of face cards and Aces.

### Features

- Play against the dealer.
- Hit or stand based on your hand value.
- Dealer automatically plays according to standard rules.
- Clear display of game state, including player and dealer hands.
- Handles Aces as either 1 or 11 to optimize the player's hand value.
- Instructions provided for new players.

### Requirements

- Python 3.x
- No external libraries are required; the game uses built-in libraries (random and os).

### Installation

Clone the repository or download the script file.
Ensure you have Python 3.x installed on your system.
Open your terminal or command prompt.
Navigate to the directory where the script is located.

### Usage

Run the game by executing the script:
bash
python lucky_21.py  
Follow the on-screen instructions to enter your name and start playing.
Choose to hit (draw a card) or stand (keep your current hand) when prompted.

## Game Rules

### Card Values

- Aces can be worth 1 or 11, depending on which value is more advantageous for the player.
- Face cards (Kings, Queens, Jacks) and Tens are worth 10.
- Number cards are worth their face value.

### Gameplay

- Each player starts with two cards.
- Players can choose to hit or stand.
- The dealer must draw until reaching a total of at least 17.
- The player wins by having a higher hand value than the dealer without exceeding 21.
- If the player or dealer exceeds 21, they bust and lose the round.

## Example Game Flow

1. The player enters their name.
2. The game displays the initial hands of the player and dealer.
3. The player decides whether to hit or stand.
4. The dealer plays according to the rules.
5. The game announces the winner or if it’s a tie.

## Acknowledgments

Special thanks to TokyoEdTech for the original card game code inspiration.
