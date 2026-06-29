import random
from hangman_words import word_list          # TODO-1
from hangman_art import stages, logo         # TODO-3

lives = 6

print(logo)  # Print logo at start

chosen_word = random.choice(word_list)
# print(chosen_word)  # Uncomment for debugging

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []   # Track all guesses

while not game_over:

    # TODO-6: Show lives left
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    # TODO-4: Warn if letter already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
    guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: Handle incorrect guess
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    # Win condition
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: Print hangman stage
    print(stages[lives])
