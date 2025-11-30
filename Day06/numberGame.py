# Guess the Number Game
# Concepts Used: while loop and user input.
# Sample Run:
# Guess a number between 1 and 10: 4
# Wrong guess! Try again.
# Guess again: 7
# Congratulations, Saumya! You guessed it right 🎉

import random

name = input("Enter your name : ")
i = random.randint(1,10)  # secret number
guessedNumber =int(input("Guess a number between 1 to 10:"))
while guessedNumber != i :
    print("Wrong guess! Try again.")
    guessedNumber =input("Guess a number again : ")
    print(f"Congratulations, {name}! You guessed it right 🎉")    
  