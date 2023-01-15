import random
from art import logo

playing = True
difficulty_options = ["easy", "hard"]

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

difficulty = ""
while difficulty not in difficulty_options:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while playing:
    print(f"You have {attempts} attempts remaining to guess the number.")

    player_guess = 0
    while player_guess < 1 or player_guess > 100:
        try:
            player_guess = int(
                input("Guess a number. Must be between 1 and 100: "))
        except:
            print("Error: You must type a number between 1 and 100..")

    if player_guess == answer:
        print(f"You guessed the right number! The number was {answer}!")
        playing = False
    elif player_guess > answer:
        print("Wrong. Guess is too high.")
    elif player_guess < answer:
        print("Wrong. Guess is too low.")

    attempts -= 1
    if attempts == 0:
        print("Sorry, you have run out of attempts. Try again!")
        playing = False
