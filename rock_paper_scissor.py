import random

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)'
---.__(___)'
"""
print('"WELCOME TO ROCK PAPER SCISSOR!')
#PLAYER INPUT
user_choice=int(input('WHAT DO YOU WANT TO CHOOSE?\nTYPE"0"FOR ROCK\nTYPE"1"FOR PAPER\nTYPE"2"FOR SCISSOR\n'))
game_images=[rock,paper,scissor]
if user_choice>=0 and user_choice<3:
   print(game_images[user_choice])
#COMPUTER
x=[rock,paper,scissor]
computer_choice=random.randint(0,2)
print("COMPUTER CHOOSE:")
print(game_images[computer_choice])
#deciding who won and lost
if user_choice==0 and computer_choice==2:
    print("YOU WON!")
elif user_choice==2 and computer_choice==0:
    print("YOU LOST")
elif user_choice==2 and computer_choice==1:
    print("YOU WON")
elif user_choice==1 and computer_choice==0:
    print("YOU LOST")
elif computer_choice>user_choice:
    print("YOU LOST")
elif computer_choice==user_choice:
    print("IT IS A DRAW")
else:
    print("YOU TYPED AN INVALID NUMBER")
