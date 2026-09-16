# PROJECT 1: SNAKE, WATER, GUN GAME 
# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user.

import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}   # youdict and reversedict is use because user not will provide number it will provide a letter because the user experience should be good that's why.
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")

if (computer == you):
    print("Its a draw")

else:
    if (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == 1 and you == 0):
        print("You Win!")

    elif (computer == -1 and you == 1):
        print("You Win!")

    elif (computer == -1 and you == 0):
        print("You lose!")

    elif (computer == 0 and you == 1):
        print("You lose!")

    elif (computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong")