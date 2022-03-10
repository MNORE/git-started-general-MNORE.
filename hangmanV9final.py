import random
import os


def import_secret_word(lives):
    list = []
    if lives == 6:
        f = open("D:\Downloads\Python\Hangmanpy\easy.txt", "rt")
        list = f.read().splitlines()
        secret_word = random.choice(list)
    else:
        f = open("D:\Downloads\Python\Hangmanpy\hard.txt", "rt")
        list = f.read().splitlines()
        secret_word = random.choice(list)

    return secret_word.upper()


def choose_game_mode():
    os.system('cls')
    answer = input("Choose a game mode! Easy or Hard: ").upper()
    is_good_answer = False
    while not is_good_answer:
        if answer == "EASY" or answer == "HARD":
            is_good_answer = True
        else:
            answer = input("Only Easy or Hard answer is valid, mode: ").upper()

    return answer


def levels(game_mode):
    if game_mode == "EASY":
        lives = 6
        return lives

    elif game_mode == "HARD":
        lives = 3
        return lives


def play(word, lives, game_mode):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    print("Let's play Hangman!")
    print("Your lives", lives)
    print(display_hangman(lives, game_mode))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter: ").upper()
        os.system('cls')
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
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print("Your lives", lives)
        print(display_hangman(lives, game_mode))
        print(word_completion)
        print("\n")
    return lives


def display_hangman(lives, game_mode):
    if game_mode == "EASY":
        hang_easy = ["""
Hangman
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
========="""]
        return hang_easy[lives]

    else:
        hang_hard = ["""
 Hangman
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
      |
      |
=========""", """
Hangman
  +---+
  |   |
      |
      |
      |
      |
========="""]
        return hang_hard[lives]


def play_again():
    answer = input("Play Again? (YES/QUIT) ").upper()
    if answer == "YES":
        return answer
    elif answer == "QUIT":
        return answer
    else:
        play_again().upper()


def main():
    game_mode = choose_game_mode()
    word = import_secret_word(levels(game_mode))
    lives = levels(game_mode)
    result = play(word, lives, game_mode)
    if result > 0:
        print("Congratulation!")
    else:
        print("Game over!")
    print("The answer was", word)
    answer = play_again().upper()
    if answer == "YES":
        main()
    else:
        quit()


main()
