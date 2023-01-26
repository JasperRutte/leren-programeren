import random
import time
from functions import *
from data import *

dragon = Monster("Dragon", 10)
skeleton = Monster("Skeleton", 7)

# user picks username
while play_again:
    PLAYER.name = ""
    PLAYER.gold = 0
    PLAYER.hp = 10
    PLAYER.weapon = no_weapon

    printDelay("You wake up in a house...")
    printDelay("random npc: 'Hey you, you're finally awake.'")
    printDelay("random npc: 'What is your name if i may ask?'")
    PLAYER.name = input("Input username: ")
    printDelay(f"random npc: 'Hello '{PLAYER.name}' it's nice to meet you.'")

    # user decides if they help the village
    time.sleep(1)
    helpVillage = input("random npc: There is a dragon near the village will you help us kill it?' (Y/N): ").upper()
    while helpVillage != "Y" and helpVillage != "N":
        printDelay("Invalid answer...")
        helpVillage = input("Help village? (Y/N): ").upper()
        print(helpVillage)

    if helpVillage == "Y":
        printDelay("random npc: 'Thank you so much, you are a true hero.'")
    else:
        printDelay("random npc: 'Youre a horrible person!'")
        for x in range(3):
            printDelay("")
        printDelay("The village later got destroyed by the dragon")
        play_again = retry(True)
        continue

    # user decides if they want a sword or not
    time.sleep(1)
    weapon = input("You first need a weapon , do you want me to give a sword? (Y/N): ").upper()
    while weapon != "Y" and weapon != "N":
        printDelay("Invalid answer...")
        weapon = input("Do you want a weapon? (Y/N): ")

    if weapon == "Y":
        printDelay("Take good care of the sword")
        PLAYER.weapon = iron_sword

    else:
        printDelay("Okay... The choice was yours")

    # user decides to train or fight the dragon immediately
    dragonFight1 = input("Do you first want to train or immediately fight the dragon? (Train/Fight): ").upper()
    while dragonFight1 != "FIGHT" and dragonFight1 != "TRAIN":
        printDelay("Invalid answer...")
        dragonFight1 = input("Do you want to train or immediately fight the dragon? (Train/Fight): ").upper()

    if dragonFight1 == "FIGHT":
        printDelay("You tried to encounter the dragon but died because of the strong aura from the dragon...")
        printDelay("You need to get the Dragon Sword to block this aura and come close to fight the dragon")
        retry(True)
        continue
    elif dragonFight1 == "TRAIN":
        printDelay("Good, you shall now go to the forest and start your training")
        printDelay("You start wandering through the forest")

    # first fight, they decide fight or run
    time.sleep(1)
    fight_again = True
    while fight_again and PLAYER.hp != 0:
        goblin = Monster("Goblin", 5)
        run_fight(goblin)
        while fight_again != "Y" and fight_again != "N" and PLAYER.hp > 0:
            fight_again = input("Do you want to fight more goblins? (Y/N): ").upper()
            if fight_again == "N":
                fight_again = False
            break
    if PLAYER.hp == 0:
        continue

    # second fight, they decide fight or run
    printDelay("You continue wandering in the forest...")
    printDelay("You see a skinny figure wielding a mysterious sword.")
    run_fight(skeleton)
    if PLAYER.hp == 0:
        continue

    # boss fight, they need dragon sword to fight in and hit boss 3 times
    printDelay("You are now going to fight the dragon!")
    run_fight(dragon)
    if PLAYER.hp == 0:
        continue

    retry(False)
