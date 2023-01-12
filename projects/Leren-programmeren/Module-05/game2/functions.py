import random
import time
from data import *

def printDelay(t: str, d=0.75):  # function to print with delay
    time.sleep(d)
    print(t)

def death(username: str, gold: int):
    print("GAME OVER...")
    printDelay(f"{username} had {gold} gold on him")


def run_or_fight(user_hp: int, user_gold: int, monster: str):
    printDelay(f"""
User stats: 
HP: {user_hp}
Gold: {user_gold}""")

    if monster == "goblin":
        monster_hp = 3
    elif monster == "skeleton":
        monster_hp = 5

    printDelay(f"You encountered a {monster}!")
    printDelay(f"It has {monster_hp} hp")
    printDelay("Do you want to run or fight it?")
    choice = input("fight/run: ").upper()
    while choice != "FIGHT" and choice != "RUN":
        print("Invalid answer...")
        choice = input("fight/run: ").upper()
    if choice == "FIGHT":
        fight(user_hp, user_gold, monster, monster_hp)
    else:
        run()


def fight(user_hp: int, user_gold: int, monster: str, monster_hp: int):
    print(f"You decided to fight the {monster}!")
    while user_hp != 0 and monster_hp != 0:
        user_attack = random.randint(0, 3)
        time.sleep(0.5)
        if user_attack != 1:
            monster_hp -= 1
            printDelay("You hit!")
            print(f"{monster} hp: {monster_hp}")
        else:
            printDelay("You missed!")

        if monster_hp == 0:
            break
        monster_attack = random.randint(1, 10)
        time.sleep(0.5)
        if monster_attack == 1:
            user_hp -= 1
            printDelay(f"The {monster} hit you!")
            print(f"HP: {user_hp}")
        else:
            printDelay(f"The {monster} missed!")

    if monster_hp == 0:
        gold_gained = random.randint(1, 6)
        user_gold += gold_gained
        printDelay(f"You won and gained {gold_gained} gold!")
        printDelay(f"""User stats:
HP: {user_hp}
Gold: {user_gold}""")
        return user_hp, user_gold


def run():
    printDelay("You decided to run away!")
    random_num = random.randint(1,4)
    user_num = int(input("Choose a number between 1-3: "))
    while user_num != 1 and user_num != 2 and user_num != 3:
        print("invalid answer...")
        user_num = int(input("Choose a number between 1-3: "))
    if random_num == user_num:
        print("You successfully ran away!")
    else:
        print("You failed to run away...")
