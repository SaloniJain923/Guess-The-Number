
import random
from replit import clear
from art import logo

def play():
  print(logo)
  print("Welcome to Guess The Number Game")

  numbers = list(range(1,100))
  print("Thinking of a number from 1 to 100 .........")
  main_number = int(random.choice(numbers))
  level = input("Choose the Difficulty Level, Type 'easy' or 'hard' : ").lower()
  if level == 'easy':
    attempts = 10
  elif level == 'hard':
    attempts = 5
  else:
    print("Enter Proper Level of Difficulty !!")

  def guess_a_number(attempts):
    game_over = False
    while game_over != True :
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Guess a number : "))
      if guess == main_number :
        print("You did it 👍. You Guessed The Number😃 \nYou Win 🏆")
        game_over = True
      elif guess < main_number:
        print("Too Low \nGuess Again 😉")
        attempts -= 1
      else:
        print("Too High \nGuess Again 😉")
        attempts -= 1

      if attempts == 0:
        game_over = True
        print("You have no attempts remaining\nYou Lose👎")
  guess_a_number(attempts)

while input("Play Game? Type 'y' or 'no' : ") == 'y':
  clear()
  play()