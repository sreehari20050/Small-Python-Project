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
value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if value == 0:
    print(rock)
elif value == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: ")

value1 = ['rock','scissors','paper']
value2 = random.choice(value1)

if value2 == 'rock':
    print(rock)
elif value2 == 'scissors':
    print(scissors)
else:
    print(paper)

if (value2 == 'rock' and value == 0) or (value2 == 'scissors' and value == 2) or (value2 == 'paper' and value == 1):
    print("It's a draw")
elif (value == 0 and value2 == 'scissors') or (value == 1 and value2 == 'rock') or (value == 2 and value2 == 'paper'):
    print('You win!')
else:
    print('You lose')
