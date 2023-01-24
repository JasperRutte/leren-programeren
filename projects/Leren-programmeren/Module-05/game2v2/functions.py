import random
import time
from data import *


def printDelay(t: str, d=0.25):  # function to print with delay
    time.sleep(d)
    print(t)


def retry(death: bool):  # When game is over, user decides to play again or not
    if PLAYER.hp == 0:
        printDelay("GAME OVER\n")
        printDelay(f"{PLAYER.name} had {PLAYER.gold} gold.")
    elif death:
        printDelay("GAME OVER\n")
        printDelay(f"{PLAYER.name} had {PLAYER.gold} gold.")
    else:
        printDelay("Congratulations! You won!")
        printDelay(f"You finished the game with {PLAYER.gold}!")

    playAgain = input("Do you wish to play again? (Y/N): ").upper()
    while playAgain != "Y" and play_again != "N":
        printDelay("Invalid answer")
        playAgain = input("Play again? (Y/N): ")

    if playAgain == "Y":
        print("Sending you back in:")
        for x in range(3, 0, -1):
            printDelay(f"{x}")
        return
    else:
        print("Stopping game in:")
        for x in range(3, 0, -1):
            printDelay(f"{x}")
        exit()


def run_fight(monster):  # function to decide whether user wants to run or fight
    printDelay(f"You encountered a {monster.name}!")

    printDelay(f"""
    {PLAYER.name} Stats:
    HP: {PLAYER.hp}
    GOLD: {PLAYER.gold}
    WEAPON: {PLAYER.weapon}\n""")

    choice = input(f"Do you wish to run or fight the {monster.name}? (RUN/FIGHT): ").upper()
    while choice != "FIGHT" and choice != "RUN":
        printDelay("Invalid answer")
        choice = input("Do you wish to run or fight? (RUN/FIGHT): ").upper()

    if choice == "FIGHT":
        fight(monster)
    else:
        run()


def fight(monster):  # function for fighting monsters
    printDelay(f"You chose to fight the {monster.name}!\n")

    if PLAYER.weapon == "None":
        printDelay("You died since you didn't have a weapon...")
        return retry(True)

    if monster.name == "Skeleton":
        PLAYER.weapon = dragon_sword

    if PLAYER.weapon != "Dragon Sword" and monster.name == "Dragon":
        printDelay("You tried fighting the dragon without the Dragon Sword")
        return retry(True)

    while PLAYER.hp != 0:
        user_hit = random.randint(0, 4)
        if user_hit != 1:
            monster.hp -= 1
            printDelay("You hit!")
            printDelay(f"{monster.name} HP: {monster.hp}")
        else:
            printDelay("You missed!")
        if monster.hp == 0:
            break

        monster_hit = random.randint(0, 6)
        if monster_hit == 1:
            PLAYER.hp -= 1
            printDelay(f"{monster.name} hit you!")
            printDelay(f"{PLAYER.name} HP: {PLAYER.hp}")
        else:
            printDelay(f"{monster.name} missed!")

    if monster.hp == 0:
        gold_drop(monster)
        printDelay(f"""
        {PLAYER.name} Stats:
        HP: {PLAYER.hp}
        GOLD: {PLAYER.gold}
        WEAPON: {PLAYER.weapon}\n""")
        return
    else:
        return retry(True)


def run():
    printDelay("You decided to run away!")
    escape_win = random.randint(0, 4)
    user_num = input("Pick a number between 1-3: ")
    while user_num != "1" and user_num != "2" and user_num != "3":
        printDelay("Invalid answer...")
        user_num = input("Pick a number between 1-3: ")

    if user_num == escape_win:
        printDelay("You successfully ran away!")
        return
    else:
        PLAYER.hp = 0
        printDelay("You failed to run away and died!")
        return retry(True)


def gold_drop(monster):
    if monster.name == "Goblin":
        PLAYER.gold += random.randint(1, 5)
    elif monster.name == "Skeleton":
        PLAYER.gold += random.randint(5, 10)
    elif monster.name == "Dragon":
        PLAYER.gold += random.randint(20, 30)

    return
