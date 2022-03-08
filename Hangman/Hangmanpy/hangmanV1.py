import random

def underscore_secret_word(secret_word):
    print(secret_word)
    underscore = "_ " * len(secret_word)
    return underscore


def import_secret_word(level):
    list = []
    if level == 10:
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
        lives = 10
        return lives

    elif game_mode == "HARD":
        lives = 5
        return lives

    else:
        return levels()


print(underscore_secret_word(import_secret_word(levels())))




#def play_functions(secret_word, lives):
    #guessed_letters = []
    #user_guess = input("Guess a word! ")
    #if user_guess == "quit":
        #break

        
