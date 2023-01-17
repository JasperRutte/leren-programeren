from data import *
from functions import *
import random
import time

# user picks username
Player = Player("", 10, 0, "None")
printDelay("You wake up in a house...")
printDelay("random npc: 'Hey you, you're finally awake.'")
printDelay("random npc: 'What is your name if i may ask?'")
Player.name = input("Input username: ")
printDelay(f"random npc: 'Hello '{Player.name}' it's nice to meet you.'")

# user decides if they help the village
time.sleep(1)
helpVillage = input("random npc: There is a dragon near the village will you help us kill it?' (Y/N): ").upper()
while helpVillage != "Y" and helpVillage != "N":
    print("Invalid answer...")
    helpVillage = input("Help the village? (Y/N): ").upper()

if helpVillage == "Y":
    printDelay("random npc: 'Thank you so much, you are a true hero.'")
elif helpVillage == "N":
    printDelay("The village later got destroyed by the dragon.")
    death(Player.name, Player.gold, Player.weapon, play_again)

# user decides if theP want a sword or not
time.sleep(1)
weapon = input("You first need a weapon , do you want me to give a sword? (Y/N): ").upper()
while weapon != "Y" and weapon != "N":
    print("Invalid answer...")
    weapon = input("Do you want a sword? (Y/N): ").upper()

if weapon == "Y":
    printDelay("Great! Take good care of it!")
    Player.weapon = iron_sword
else:
    printDelay("The choice was yours...")


# user decides to train or fight the dragon immediately
dragonFight1 = input("Do you first want to train or immediately fight the dragon? (Train/Fight): ").upper()
while dragonFight1 != "FIGHT" and dragonFight1 != "TRAIN":
    print("Invalid answer")
    dragonFight1 = input("Do you wish to train or fight? (Train/Fight): ").upper()

if dragonFight1 == "TRAIN":
    printDelay("Good, you shall now go to the forest and start your training\n")
    printDelay("You start wandering through the forest")
else:
    printDelay("You tried fighting the dragon but sadly failed...")
    printDelay("To fight the dragon you  need a dragon sword!")
    death(Player.name, Player.gold, Player.weapon, play_again)


# first fight, they decide fight or run
time.sleep(1)
while fight_again:
    Player.hp, Player.gold = run_or_fight(Player.name, Player.hp, Player.gold, Player.weapon, "goblin")
    fight_again = False
    fight_again = input("Do want to fight more goblins or walk deeper into the forest? (fight/walk): ").upper()
    while fight_again != "FIGHT" and fight_again != "WALK":
        printDelay("Invalid answer")
        fight_again = input("Do want to fight more goblins or walk deeper into the forest? (fight/walk): ").upper()
    if fight_again == "FIGHT":
        fight_again = True
    else:
        fight_again = False


# second fight, they decide fight or run
printDelay("You continue wandering in the forest...")
printDelay("You encounter a skeleton wielding a strange sword")
fightRun = input("Do you want to fight it run? (Fight/Run): ").upper()
if fightRun == "FIGHT":
    Player.hp, Player.gold = run_or_fight(Player.name, Player.hp, Player.gold, Player.weapon, "skeleton")
    Player.weapon = dragon_sword

# boss fight, they need dragon sword to fight in and hit boss 3 times
printDelay("You are now going to fight the dragon!")
if not Player.weapon != dragon_sword:
    death(Player.name, Player.gold, Player.gold, play_again)
else:
    run_or_fight(Player.name, Player.hp, Player.gold, Player.weapon, "dragon")