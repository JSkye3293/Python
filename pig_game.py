#JSkye

import random
import string
import sys


saved_roll = 0

bot_score = 0
man_score = 0

debug = 0
attempt = 0

def slightOfHand():
    cheat.randint(0,1000)

def dice_roll():
    di_roll.randint(1,6)

def randomString(stringLength=5000):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def roll_dice(debug, mode):
    hold = 1
    while hold == 1:
        di_roll = dice_roll()

        if debug == 1:
            print("\n #####DEBUG#####\n Returned " + di_roll)

        if mode == 1:

            print("**********************\nHUMAN, YOU ROLLED " + di_roll +"\n******************")

            if di_roll > 4:
                print("BOOOOO!!! don't keep it I dare you!")
            answer = input("***KEEP?***\n<Press ENTER to keep rolling, or type yes/y to keep.>")

        if mode == 2:
            print("**********************\n BOT ROLLED " + di_roll +"\n******************")

            if di_roll > 1:
                print("ANOTHER SUCCESFULL MOVE")
            answer = input("***KEEP?***\n<Press ENTER to keep rolling, or type yes/y to keep.>")




def main():
    bot_name = randomString(5)
    name = input("HUMAN: \n PLEASE STATE YOUR NAME: ")
    print("WELCOME HUMAN "+ name + " YOU ARE DESTINED TO PLAY A GAME WITH THE \nEVIL ROBOT OVERLORD NAMED " + bot_name + "!!!")


main()
