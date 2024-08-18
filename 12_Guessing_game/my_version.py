import random

EASY_MODE = 10
HARD_MODE = 5

def pick_number():
    return random.choice(range(1, 100))

def set_difficulty():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == "easy":
        return EASY_MODE
    else:
        return HARD_MODE

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = pick_number()
    attempts = set_difficulty()

    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        print(f"You have {attempts} attempts, remaining to guess the number.")
        if attempts == 0:
            print(f"You lose. The answer was {answer}")
            game_over = True
        else:
            if guess > answer:
                print("Too high")
                attempts -= 1
            elif guess < answer:
                print("Too low")
                attempts -= 1
            else:
                print(f"You got it, the answer was {answer}!")
                game_over = True

game()