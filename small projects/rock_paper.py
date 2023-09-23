 #game rock paper scissors
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

#Write your code below this line 👇
user = int(
    input("what do u choose ?? type 0 for rock, 1 for paper, 2 for scissors "))
if (user<0) or (user>=3):
  print("invalid input try again..")
else:

  if user == 0:
    print(rock)
  elif user == 1:
    print(paper)
  elif user == 2:
    print(scissors)
  
  
  computer = random.randint(0, 2)
  print("computer choice = ")
  if computer == 0:
    print(rock)
  elif computer == 1:
    print(paper)
  elif computer == 2:
    print(scissors)
  
  if user == 0 and computer == 1:
    print("you lose")
  elif user == 1 and computer == 2:
    print("you lose")
  elif user == 2 and computer == 0:
    print("you lose")
  elif user == computer:
    print("match draw ")
  else:
    print("you won")
  