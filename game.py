
import random

def greet_player():
    print("Howdy, what's your name?")
    name = input("(type in your name) ")
    return name

def choose_random_number():
    return random.randint(1, 100)

def get_guess():
    guess = int(input("Your guess? "))
    return guess

def give_hint(secret_number, player_guess):
    if secret_number < player_guess:
        print("Your guess is too high, try again.")
    else:
        print("Your guess is too low, try again.")

def play_game():
    player_name = greet_player()
    secret_number = choose_random_number()
    num_guesses = 0

    print(f"{player_name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    while True:
        player_guess = get_guess()
        num_guesses += 1

        if player_guess != secret_number:
            give_hint(secret_number, player_guess)
        else:
            print(f"Well done, {player_name}! You found my number in {num_guesses} tries.")
            break

# Start the game
play_game()


