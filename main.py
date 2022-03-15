#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)

import random 

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 of 100!")

def dificulty_levls(answer,guess,ATTEMPTS):
  attempts = ATTEMPTS
  #print(f"You have {attempts} attempts to guess the Number")
  while attempts > 1 and answer != guess:
  
    play_game(answer, guess)
    attempts -= 1
    print(f"You have {attempts} attempts to guess the Number")
    guess = int(input("Make a Guess: "))
    
  if attempts <= 1:
    print("You've run out of guesses, You lose")
  else:
    print(f"You win, the answer is {answer}")
  
def play_game(answer,guess):
  if answer == guess:
    return print(f"You got it! the answer was {answer}")
  if answer > guess:
    print("Too Low")
    print("Guess Again")
    
  elif guess >  answer:
    print("Too High")
    print("Guess Again")


answer = random.randint(1,101)
dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
if dificulty == 'easy':
  guess = int(input("Make a Guess: "))
  ATTEMPTS = 10
  dificulty_levls(answer, guess,ATTEMPTS)
elif dificulty == 'hard':
  guess = int(input("Make a Guess: "))
  ATTEMPTS = 5
  dificulty_levls(answer, guess,ATTEMPTS)  
   