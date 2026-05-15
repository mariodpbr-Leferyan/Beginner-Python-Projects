"""
Hangman Game
------------
A classic word-guessing game played in the terminal.
The player guesses one letter at a time and has 6 lives.
Each wrong guess updates the ASCII hangman drawing.
"""

import random
from hangman_art import logo, stages
from hangman_words import word_list


def build_display(chosen_word, correct_letters):
    """
    Builds the current word display with guessed letters revealed.

    Args:
        chosen_word (str): The word the player is trying to guess.
        correct_letters (list): Letters correctly guessed so far.

    Returns:
        str: The word with underscores for unguessed letters.
             e.g. "_ a _ _ o _"
    """
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    return display


def get_guess(correct_letters, wrong_letters):
    """
    Prompts the player to enter a single letter and validates input.
    Warns if the letter has already been guessed.

    Args:
        correct_letters (list): Already correctly guessed letters.
        wrong_letters (list): Already incorrectly guessed letters.

    Returns:
        str: A valid, single lowercase letter not yet guessed,
             or None if the letter was already guessed.
    """
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        return None

    if guess in correct_letters or guess in wrong_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.\n")
        return None

    return guess


def play_hangman():
    """
    Runs a full game of Hangman.
    Picks a random word, handles the game loop, and
    prints the result (win or lose) at the end.
    """
    lives = 6
    correct_letters = []
    wrong_letters = []
    game_over = False

    chosen_word = random.choice(word_list)

    print(logo)
    print(stages[lives])

    while not game_over:
        display = build_display(chosen_word, correct_letters)

        print(f"{'*' * 28} {lives}/6 LIVES LEFT {'*' * 28}")
        print("Word to guess: " + " ".join(display) + "\n")

        if wrong_letters:
            print(f"Wrong guesses: {', '.join(wrong_letters)}\n")

        guess = get_guess(correct_letters, wrong_letters)

        if guess is None:
            continue

        if guess in chosen_word:
            correct_letters.append(guess)
            print(f"\n✅ '{guess}' is in the word!\n")
        else:
            wrong_letters.append(guess)
            lives -= 1
            print(f"\n❌ '{guess}' is not in the word. You lose a life.\n")
            print(stages[lives])

        display = build_display(chosen_word, correct_letters)

        if "_" not in display:
            game_over = True
            print("Word to guess: " + " ".join(display))
            print("\n****************************YOU WIN!****************************")
            print(f"You guessed '{chosen_word}' correctly! 🎉")

        elif lives == 0:
            game_over = True
            print(f"\n***********************YOU LOSE**********************")
            print(f"The word was: '{chosen_word}'.")


def main():
    """Entry point — starts the game and offers a replay option."""
    while True:
        play_hangman()
        replay = input("\nPlay again? (yes / no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nThanks for playing Hangman! Goodbye. 👋")
            break


if __name__ == "__main__":
    main()
