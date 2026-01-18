'''
1for snake
-1 for water
0 for gun
The game is played between the user and the computer. The user is prompted to enter their choice
'''
from random import random


import random


computer = random.choice([-1, 0, 1]) # -1 for snake, 0 for gun, 1 for water
print("Welcome to Snake, Water, Gun game!")
print("Enter 's' for Snake, 'w' for Water, and 'g' for Gun.")
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
you = youdict[youstr]

print(f"Computer chose {computer}")
print(f"You chose {you}")

if(computer == -1 and you == 1):
    print("You win")
elif(computer == 1 and you == -1):
    print("Computer wins")
elif(computer == 0 and you == 1):   
    print("Computer wins")
elif(computer == 1 and you == 0):
    print("You win")
elif(computer == 0 and you == -1):
    print("You win")
elif(computer == -1 and you == 0):
    print("Computer wins")
else:
    print("It's a tie")
