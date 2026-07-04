logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

import random

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy   (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard   (5 attempts)")

    while True:
        choice = input("Select 1, 2, or 3: ")
        if choice == "1":
            return 15
        elif choice == "2":
            return 10
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Try again.")

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    attempts_allowed = choose_difficulty()
    secret_number = random.randint(1, 100)
    attempts_used = 0

    while attempts_used < attempts_allowed:
        try:
            guess = int(input(f"Attempt {attempts_used+1}/{attempts_allowed} — Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts_used += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\nCorrect! The number was {secret_number}.")
            print(f"You guessed it in {attempts_used} attempts.")
            return

    print("\nOut of attempts!")
    print(f"The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
