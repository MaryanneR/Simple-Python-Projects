import random
import sys

# Game ASCII Images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img = [rock, paper, scissors]
choice_list = ['Rock', 'Paper', 'Scissors']

# Game Greeting + Get Input from User
print("Welcome to Rock Paper Scissors! Are you ready to play?")
choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if choice > 2 or choice < 0:
    print("Please enter a valid number.")
    sys.exit()
print(img[choice])

# Computer Choice
com_choice = random.randint(0, 2)
print("Computer chose: ")
print(img[com_choice])

# Determining Winner
if choice == com_choice:
    print("Tie! Try again.")
elif choice == 0 and com_choice == 2:
    print("Rock beats Scissors. You win!")
elif choice == 2 and com_choice == 1:
    print("Scissors beats Paper. You win!")
elif choice == 1 and com_choice == 0:
    print("Paper beats Rock. You win!")
else:
    print(f"{choice_list[com_choice]} beats {choice_list[choice]}")
    print("You lose!")