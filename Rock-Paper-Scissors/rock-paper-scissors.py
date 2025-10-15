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
value = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors"))
if value ==0:
    print(rock)
elif value ==1:
    print(paper)
else:
    print(scissors)

print("Computer Chose:")

random_list = [rock, paper, scissors]
random = random.choice(random_list)
print(random)
