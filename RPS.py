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
print("welcome to rock paper scissors game !")
print("this is the game rule  0 for Rock 1 for paper or 2 for scissors.\n")
Images = [rock, scissors, paper]
user_input = int(input(f"please input any number between 0 - 2\n"))
print(Images[user_input])
Computer_choice = random.randint(0, 2)
print(Images[Computer_choice] )
print(f"Computer chose {Computer_choice}")
print(f"You choose {user_input}")
if user_input > 2:
 print("you have input an invalid number please choose between 0 - 2")
if Computer_choice == 0 and user_input == 1:
 print("you loose and computer win")
elif Computer_choice == 1 and user_input == 2:
 print("you loose ! Computer Wins!")
elif Computer_choice == 2 and user_input == 1:
 print("you win ! sad computer lose")
elif user_input == 0 and Computer_choice ==1:
 print("You win! sad computer loose")
elif user_input == 1 and Computer_choice ==2:
  print("you win ! sad computer loose") 
elif user_input == 2 and Computer_choice == 0:
  print("computer wins ! ")
elif Computer_choice == user_input:
 print("This is Draw Pls Play again ")