from data import *
from functions import *
import random
import time

# user picks username
player = Player("", 10, 0, "None")
printDelay("You wake up in a house...")
printDelay("random npc: 'Hey you, you're finally awake.'")
printDelay("random npc: 'What is your name if i may ask?'")
player.name = input("Input username: ")
printDelay(f"random npc: 'Hello '{player.name}' it's nice to meet you.'")

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
    death(player.name, player.gold, player.weapon, play_again)

# user decides if theP want a sword or not
time.sleep(1)
weapon = input("You first need a weapon , do you want me to give a sword? (Y/N): ").upper()
while weapon != "Y" and weapon != "N":
    print("Invalid answer...")
    weapon = input("Do you want a sword? (Y/N): ").upper()

if weapon == "Y":
    printDelay("Great! Take good care of it!")
    player.weapon = iron_sword
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
    death(player.name, player.gold, player.weapon, play_again)


# first fight, they decide fight or run
time.sleep(1)
while fight_again:
    player.hp, player.gold = run_or_fight(player.name, player.hp, player.gold, player.weapon, "goblin")
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
player.hp, player.gold = run_or_fight(player.name, player.hp, player.gold, player.weapon, "skeleton")
player.weapon = dragon_sword

printDelay("You proceed to walk further into the forest")
printDelay("You hear some weird noises, you went to check it out.")
printDelay("You find the dragon nibbling on some dead sheep")

time.sleep(1)
if player.weapon != dragon_sword:
    death(player.name, player.gold, player.gold, play_again)
else:
    run_or_fight(player.name, player.hp, player.gold, player.weapon, "dragon")
