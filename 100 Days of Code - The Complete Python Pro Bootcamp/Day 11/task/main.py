import random
import os
import time

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ASCII Art Logo (clean + colored)
logo = f"""
{CYAN}{BOLD}
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/     
{RESET}
"""

# Face card ASCII art with color (no f-string to avoid warnings)
def color_card(art):
    return YELLOW + BOLD + art + RESET

cards_art = {
    "A": color_card(r"""
   _____
  |A .  |
  | / \ |
  | \ / |
  |  .  |
  |____V|
"""),
    "K": color_card(r"""
   _____
  |K  WW|
  |   {)|
  |  WW |
  | {)  |
  |____K|
"""),
    "Q": color_card(r"""
   _____
  |Q   w|
  |   C |
  |  ww |
  |  C  |
  |____Q|
"""),
    "J": color_card(r"""
   _____
  |J  ww|
  |   {)|
  |  ww |
  | {)  |
  |____J|
"""),
}


# Deck of cards
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    return random.choice(deck)

# Animated dealing effect
def deal_animation(target="Player"):
    frames = ["🂠", "🂡", "🂢", "🂣", "🂤", "🂥"]
    for frame in frames:
        print(f"{CYAN}{BOLD}{target} is being dealt a card... {frame}{RESET}", end="\r")
        time.sleep(0.08)
    print(" " * 60, end="\r")  # clear animation line

def calculate_score(hand):
    score = 0
    aces = hand.count("A")

    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
        else:
            score += int(card)

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def display_hand(player, hand):
    score = calculate_score(hand)
    color = GREEN if score <= 21 else RED

    print(f"\n{BOLD}{player}'s Hand:{RESET} {color}{hand}  (Score: {score}){RESET}")

    for card in hand:
        if card in cards_art:
            print(cards_art[card])
        else:
            print(f"{MAGENTA}[ {card} ]{RESET}")

def blackjack_game():
    clear()
    print(logo)
    print(f"{BLUE}Welcome to Blackjack!{RESET}\n")

    player_hand = []
    dealer_hand = []

    # Initial dealing with animation
    deal_animation("Player")
    player_hand.append(deal_card())
    deal_animation("Player")
    player_hand.append(deal_card())

    deal_animation("Dealer")
    dealer_hand.append(deal_card())
    deal_animation("Dealer")
    dealer_hand.append(deal_card())

    game_over = False

    while not game_over:
        display_hand("Player", player_hand)
        print(f"\nDealer shows: {YELLOW}{dealer_hand[0]}{RESET}")

        if calculate_score(player_hand) == 21:
            print(f"\n{GREEN}{BOLD}Blackjack! You win!{RESET}")
            return

        choice = input(f"\n{CYAN}Hit or Stand? (h/s): {RESET}").lower()

        if choice == "h":
            deal_animation("Player")
            player_hand.append(deal_card())
            if calculate_score(player_hand) > 21:
                display_hand("Player", player_hand)
                print(f"\n{RED}{BOLD}You busted! Dealer wins.{RESET}")
                return
        else:
            game_over = True

    clear()
    print(logo)
    print(f"{BLUE}Dealer's turn...{RESET}\n")
    time.sleep(1)

    while calculate_score(dealer_hand) < 17:
        deal_animation("Dealer")
        dealer_hand.append(deal_card())
        time.sleep(0.3)

    display_hand("Dealer", dealer_hand)
    display_hand("Player", player_hand)

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"\n{BOLD}RESULTS:{RESET}")
    if dealer_score > 21:
        print(f"{GREEN}Dealer busts! You win!{RESET}")
    elif player_score > dealer_score:
        print(f"{GREEN}You win!{RESET}")
    elif player_score < dealer_score:
        print(f"{RED}Dealer wins!{RESET}")
    else:
        print(f"{YELLOW}It's a tie!{RESET}")

if __name__ == "__main__":
    blackjack_game()
