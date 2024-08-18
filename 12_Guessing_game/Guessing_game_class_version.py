import random

EASY_MODE = 10
HARD_MODE = 5

def pick_number():
    number = random.choice(range(1, 100))
    return number

def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high")
        return attempts - 1
    elif guess < answer:
        print("Too low")
        return attempts - 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}")

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

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts, remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        
        if attempts == 0:
            print("You lose")
            return
        elif guess != answer:
            print("Guess again")
        
game()