import random

# range the value of dice
min_val = 1
max_val = 6

# to loop the rolling through the user input
roll_again = "yes"

# loop
while roll_again == "yes":
    print("rolling the dices... ")
    print("the values are : ")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))

    roll_again = input("roll the dice again? ").lower()
