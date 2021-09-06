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
import random
import pyfiglet
graphics = pyfiglet.figlet_format("Rock-Paper-Scissor Game", font="slant")
print(graphics)







def play(direction):
  user_chs = input("What do you choose? Type 0 for Rock, 1 for paper, and 2 for scissor")
  user_ch = int(user_chs)
  game(user_ch)


def game(user_ch):
  if user_ch == 0:
      print(f"YOU CHOSE \n {rock}")
  elif user_ch ==1:
      print(f"YOU CHOSE \n {paper}")
  else:
      print(f"YOU CHOSE \n {scissors}")

  comp_ch = random.randint(0,2)

  if comp_ch == 0:
    print(f"COMPUTER CHOSE \n {rock}")
  elif comp_ch == 1:
    print(f"COMPUTER CHOSE \n {paper}")
  else:
    print(f"COMPUTER CHOSE \n {scissors}")

  if user_ch==0 and comp_ch==0:
    print("DRAW \n GAME OVER \n Agli chance me haraduunga 😁😁😁😁 ")
    direction_choice()
  elif user_ch==0 and comp_ch==1:
    print("YOU LOOSE \n LE computer: hahahahahahaha 😁😁😁😁")
    direction_choice()
  elif user_ch==0 and comp_ch==2:
    print("YOU WIN \n Le Computer:agli baar nahi chorunga")
    direction_choice()
  elif user_ch==1 and comp_ch==0:
    print("YOU WIN \n Le Computer:agli baar nahi chorunga")
    direction_choice()
  elif user_ch==1 and comp_ch==1:
    print("DRAW \n GAME OVER")
    direction_choice()
  elif user_ch==1 and comp_ch==2:
    print("YOU LOOSE \n LE computer: hahahahahahaha 😁😁😁😁")
    direction_choice()
  elif user_ch==2 and comp_ch==0:
    print("YOU LOOSE \n LE computer: hahahahahahaha 😁😁😁😁")
    direction_choice()
  elif user_ch==2 and comp_ch==1:
    print("YOU WIN \n Le Computer:agli baar nahi chorunga")
    direction_choice()
  elif user_ch==0 and comp_ch==2:
    print("DRAW \n GAME OVER")
    direction_choice()

def direction_choice():
  direction = input("Do you want to try more chances?")
  if direction == "yes":
    play(direction)
  else:
    print("GAME FINISHED")



user_chs=input("What do you choose? Type 0 for Rock, 1 for paper, and 2 for scissor")
user_ch=int(user_chs)
game(user_ch)

