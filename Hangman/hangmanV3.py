import random


def import_secret_word(level):
    list = []
    if level == 6:
        f = open("E:\Codecool\Programing Basics\Week pair 1\Python\Hangman\easy.txt", "rt")
        list = f.read().splitlines()
        secret_word = random.choice(list)
    else:
        f = open("E:\Codecool\Programing Basics\Week pair 1\Python\Hangman\hard.txt", "rt")
        list = f.read().splitlines()
        secret_word = random.choice(list)

    return secret_word


def levels():
    lives = 0

    game_mode = input("Choose a game mode! Easy or Hard: ")
    game_mode = game_mode.upper()

    if game_mode == "EASY":
        lives = 6
        return lives

    elif game_mode == "HARD":
        lives = 3
        return lives

    return levels()


def play(word):
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    lives = levels()
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess, "\n", "Guessed letters:", guessed_letters)
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_ " not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")

def display_hangman(lives):
    if lives == 6:
        hang_easy = ["""
Hangman

   +---+
   |   |
       |
       |
       |
       |
=========""", """
Hangman
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
        return hang_easy

    else:
        hang_hard = ["""
Hangman

   +---+
   |   |
       |
       |
       |
       |
=========""", """
Hangman
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
Hangman
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
        return hang_hard


def main():
    word = import_secret_word(levels())
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = import_secret_word(levels())
        play(word)


main()
