import random
import time

def fightWinLose(i):
    x = random.randint(0, 10)
    if 0 < i < 10:
        if i == x:
            print("You died")
            exit()
        elif i != x:
            print("You won!")
        else:
            print("invalid answer")
            exit()
    else:
        print("Number is too big/small")
        exit()


def escapeWinLose(i):
    x = random.randint(0, 3)
    if 0 < i < 3:
        if i == x:
            print("You died")
            exit()
        elif i != x:
            print("You successfully escaped")
        else:
            print("invalid answer")
            exit()
    else:
        print("Number is too big/small")
        exit()


def printDelay(t: str, d=0.75):
    time.sleep(d)
    print(t)


printDelay("You wake up in a house...")
printDelay("random npc: 'Hey you, you're finally awake.'")
printDelay("random npc: 'What is your name if i may ask?'")
username = input("Input username: ")
print(f"random npc: 'Hello '{username}' it's nice to meet you.'")


time.sleep(1)
helpVillage = input("random npc: There is a dragon near the village will you help us kill it?' (Y/N): ").upper()
if helpVillage == "Y":
    printDelay("random npc: 'Thank you so much, you are a true hero.'")
elif helpVillage == "N":
    print("The village later got destroyed by the dragon.")
    print("game over")
    exit()
else:
    print("invalid answer... Game over")
    exit()

time.sleep(1)
weapon = input("You first need a weapon , do you want me to give a sword? (Y/N): ").upper()
if weapon == "N":
    weaponSure = input("Are you sure you dont want a sword? (Y/N): ").upper()
    if weaponSure == "N":
        printDelay("Okay... The choice was yours")
    elif weaponSure == "Y":
        printDelay("Take good care of the sword")
elif weapon == "Y":
    printDelay("Take good care of the sword")
else:
    print("Invalid answer... Game over")
    exit()


dragonFight1 = input("Do you first want to train or immediately fight the dragon? (Train/Fight): ").upper()
if dragonFight1 == "FIGHT":
    printDelay("You tried fighting the dragon but sadly failed...")
    printDelay("To fight the dragon you  need a dragon sword!")
    exit()
elif dragonFight1 == "TRAIN":
    printDelay("Good, you shall now go to the forest and start your training")
else:
    print("invalid answer... Game over")
    exit()

time.sleep(1)
print("You encountered a goblin!")
firstFight = input("Do you wish to fight it or run? (Fight/Run)").upper()
if firstFight == "FIGHT":
    fightWinLose(int("Enter a even number: "))
elif firstFight == "RUN":
    escapeWinLose("Enter a even number")
else:
    print("Invalid answer... Game over")
    exit()


