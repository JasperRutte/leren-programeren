from functions import *
from data import *
import random
import time

# user picks username
printDelay("You wake up in a house...")
printDelay("random npc: 'Hey you, you're finally awake.'")
printDelay("random npc: 'What is your name if i may ask?'")
username = input("Input username: ")
print(f"random npc: 'Hello '{username}' it's nice to meet you.'")


# user decides if they help the village
time.sleep(1)
helpVillage = input("random npc: There is a dragon near the village will you help us kill it?' (Y/N): ").upper()
while helpVillage != "Y" and helpVillage != "N":
    print("Invalid answer...")
    helpVillage = input("Help the village? (Y/N): ").upper()
    print(helpVillage)

if helpVillage == "Y":
    printDelay("random npc: 'Thank you so much, you are a true hero.'")
elif helpVillage == "N":
    print("The village later got destroyed by the dragon.")
    print("game over")
    exit()

# user decides if they want a sword or not
time.sleep(1)
weapon = input("You first need a weapon , do you want me to give a sword? (Y/N): ").upper()
while weapon != "Y" and weapon != "N":
    print("Invalid answer...")
    weapon = input("Do you want a sword (Y/N): ").upper()

if weapon == "Y":
    printDelay("Great! Take good care of it!")
    weapon = True
else:
    weapon = input(printDelay("Are you sure you dont want the sword? (Y/N")).upper
    if weapon == "Y":
        weapon = True
        printDelay("Good choice! Here take good care of it.")
    else:
        print("The choice was yours...")


# user decides to train or fight the dragon immediately
dragonFight1 = input("Do you first want to train or immediately fight the dragon? (Train/Fight): ").upper()
while dragonFight1 != "FIGHT" and dragonFight1 != "TRAIN":
    print("Invalid answer")
    dragonFight1 = input(printDelay("Do you wish to train or fight? (Train/Fight): "))

if dragonFight1 == "TRAIN":
    printDelay("Good, you shall now go to the forest and start your training")
    printDelay("You start wandering through the forest")
else:
    printDelay("You tried fighting the dragon but sadly failed...")
    printDelay("To fight the dragon you  need a dragon sword!")
    exit() 

# first fight, they decide fight or run
time.sleep(1)
print("You encountered a goblin!")
run_or_fight(user_hp, gold, "goblin")

# second fight, they decide fight or run
printDelay("You continue wandering in the forest...")
printDelay("You encounter a skeleton wielding a strange sword")
fightRun = input("Do you want to fight it run? (Fight/Run): ").upper()
if fightRun == "FIGHT":
    dragonSword = True
else:
    dragonSword = False
fighting(fightRun)

# boss fight, they need dragon sword to fight in and hit boss 3 times
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
