# Rock Paper Scissors

import random


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

choice = [rock, paper, scissors]

# For your Choice
print("What do you want to choose? 'rock' 'paper' or 'scissor'?")
your_choice = input("> ").lower()

if your_choice == "rock":
    your_choice = 0
elif your_choice == "paper":
    your_choice = 1
elif your_choice == "scissors":
    your_choice = 2
else:
    your_choice = None
    print("Invalid input. Choose your option again!")

if your_choice != None:
    print(f"You Chose: \n {choice[your_choice]}")

# For Computer choice
computer_choice = random.choice(choice)
print(f"Computer Chose: \n {computer_choice}")

# Determine the winner
if your_choice == 0 and computer_choice == scissors:
    print("You Win! Rock beats Scissors.")
elif your_choice == 1 and computer_choice == rock:
    print("You Win! Paper beats Rock.")
elif your_choice == 2 and computer_choice == paper:
    print("You Win! Scissors beats Paper.")
elif your_choice == 0 and computer_choice == paper:
    print("You Lose! Paper beats Rock.")
elif your_choice == 1 and computer_choice == scissors:
    print("You Lose! Scissors beats Paper.")
elif your_choice == 2 and computer_choice == rock:
    print("You Lose! Rock beats Scissors.")
else:
    print("It's a tie! You both chose the same.")



