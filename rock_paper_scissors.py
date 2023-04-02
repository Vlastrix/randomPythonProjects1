import random
from time import sleep
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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
if choice == 1:
  print(paper)
if choice == 2:
  print(scissors)
while choice >= 6:
  print("How about I BLOW up your PC JAJAJAJ")
  choice -= 0.1
  sleep(1.5)
  

items = [rock, paper, scissors]
chosen = random.choice(items)
print(f"Computer chose:{chosen}")

#draws
if choice == 0 and chosen == items[0]:
  print("It's a draw")
if choice == 1 and chosen == items[1]:
  print("It's a draw")
if choice == 2 and chosen == items[2]:
  print("It's a draw")
#wins
if choice == 0 and chosen == items[2]:
  print("You win!")
if choice == 1 and chosen == items[0]:
  print("You win!")
if choice == 2 and chosen == items[1]:
  print("You win!")
#loses
if choice == 0 and chosen == items[1]:
  print("You lose")
if choice == 1 and chosen == items[2]:
  print("You lose")
if choice == 2 and chosen == items[0]:
  print("You lose")

  
# otra forma de hacer el codigo en la linea 37 y 38 Pd: los dos inventados por mi pero no es gran cosa xdddd
# random_n = random.randint(0, 2)
# if random_n == 0:
#   print(rock)
# if random_n == 1:
#   print(paper)
# if random_n == 2:
#   print(scissors)