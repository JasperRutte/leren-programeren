import random
import time

def fightWinLose(i: int):
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

def escapeWinLose(i: int):
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

def fighting(i: str):
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

def dragonFight(i: int):
    counter = random.randint(1, 5)
    if 0 < i < 6:
        if counter == i:
            print("You died")
            exit()
    else:
        print("hit")

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
    if weaponSure == "Y":
        printDelay("Okay... The choice was yours")
    elif weaponSure == "N":
        printDelay("Take good care of the sword")
        weapon = "Y"
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
    printDelay("You start wandering through the forest")

else:
    print("invalid answer... Game over")
    exit()

time.sleep(1)
print("You encountered a goblin!")
fightRun = input("Do you want to fight it run? (Fight/Run): ").upper()
fighting(fightRun)

printDelay("You continue wandering in the forest...")
printDelay("You encounter a skeleton wielding a strange sword")
fightRun = input("Do you want to fight it run? (Fight/Run): ").upper()
if fightRun == "FIGHT":
    dragonSword = True
else:
    dragonSword = False
fighting(fightRun)

printDelay("You are now going to fight the dragon!")
if not dragonSword:
    print("You died because you didnt have the dragon sword...")
    exit()
else:
    userNumber = int(input("Enter a number between 1-5"))
    dragonFight(userNumber)
    userNumber = int(input("Enter a number between 1-5"))
    dragonFight(userNumber)
    userNumber = int(input("Enter a number between 1-5"))
    dragonFight(userNumber)
print(f"Congrats '{username}'! You are the village their saviour!")
