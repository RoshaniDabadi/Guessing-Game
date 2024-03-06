"""A number-guessing game."""

import random

def greet_player():
    print("Hi!")

def get_player_name():
    name = input("What's your name? ")
    return name

def choose_random_number():
    return random.randint(1, 100)

def get_guess():
    guess = int(input("Guess the number between 1 and 100: "))
    return guess

def give_hint(secret_number, player_guess):
    if secret_number < player_guess:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

def play_game():
    greet_player()
    player_name = get_player_name
    secret_number = choose_random_number()
    num_guesses = 0

    while True:
        player_guess = get_guess()
        num_guesses += 1

        if player_guess != secret_number:
            give_hint(secret_number, player_guess)

        else:
            print(f"Congratulations, {player_name}! You guessed the number in {num_guesses} guesses.")
            break
    
#Start the game
play_game()





