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
game_images = [rock, paper, scissors]

user_choice = int (input("what do you chose? \n "))
if user_choice >= 3 or user_choice <0:
  print("you typed invalida number and You Lose!")
else:
  print(game_images[user_choice])  
  computer_choice = random.randint(0,2)
  print("Computer choose : ")
  print(game_images[computer_choice])


  if user_choice == 0 and computer_choice == 2: 
    print("You Win!")
  elif computer_choice == 0 and user_choice == 2: 
    print("You Lose!")
  elif computer_choice > user_choice:
    print("You Lose!")
  elif user_choice > computer_choice:
    print("You Win!")
  elif computer_choice == user_choice :
    print("ïts draw")
 