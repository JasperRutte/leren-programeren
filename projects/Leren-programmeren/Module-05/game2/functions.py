import random
import time


def fightWinLose(i: int):  # int generator for winning and losing fights
    x = random.randint(1, 4)
    if 0 < i < 5:
        if i == x:
            print("You died")
            exit()
        else:
            print("You won!")
    else:
        print("Number is too big/small")
        print("Game over...")
        exit()

def escapeWinLose(i: int):  # int generator to decide if you escape or not
    x = random.randint(1, 2)
    if 0 < i < 3:
        if i == x:
            print("You died")
            exit()
        else:
            print("You successfully escaped")
    else:
        print("Number is too big/small")
        print("Game over...")
        exit()

def fighting(i: str):  # function to see if user wants to run or fight
    if i == "FIGHT":
        if weapon == "N":
            print("You lost because you didnt have a sword...")
            exit()
        else:
            usernumber = int(input("Enter a number between 1-4: "))
            fightWinLose(usernumber)
    elif i == "RUN":
        usernumber = int(input("Enter 1 or 2: "))
        escapeWinLose(usernumber)
    else:
        print("Invalid answer... Game over")
        exit()

def dragonFight(i: int):    # int generator to fight the dragon
    counter = random.randint(1, 5)
    if 0 < i < 6:
        if counter == i:
            print("You died")
            exit()
    else:
        print("hit")

def printDelay(t: str, d=0.75):  # function to print with delay
    time.sleep(d)
    print(t)