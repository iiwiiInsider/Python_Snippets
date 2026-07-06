import random
from game_data import data

# ASCII ART (raw strings prevent escape warnings)
logo = r"""
 _   _ _       _               
| | | (_)     | |              
| |_| |_  __ _| |__   ___ _ __ 
|  _  | |/ _` | '_ \ / _ \ '__|
| | | | | (_| | | | |  __/ |   
\_| |_/_|\__, |_| |_|\___|_|   
          __/ |                
         |___/                 
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def get_random_account():
    return random.choice(data)

def format_account(account):
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    return guess == "B"

def game():
    print(logo)
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"Correct! Current score: {score}\n")
        else:
            print(f"Wrong! Final score: {score}")
            game_should_continue = False

if __name__ == "__main__":
    game()
