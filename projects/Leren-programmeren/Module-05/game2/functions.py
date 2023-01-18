import random
import time


def printDelay(t: str, d=0.25):  # function to print with delay
    time.sleep(d)
    print(t)


def death(username: str, gold: int, weapon: str, play_again: bool):
    print("GAME OVER...")
    printDelay(f"'{username}' had {gold} gold")

    retry = input("Do you  want to play again? (Y/N): ").upper()
    while retry != "Y" and retry != "N":
        printDelay("Invalid answer...")
        retry = input("Do you  want to play again? (Y/N): ").upper()

    if retry == "Y":
        play_again = True
        gold = 0
        username = ""
        weapon = "None"
        print("Sending you back in: ")
        for x in range(3, 0, -1):
            printDelay(x)
        return username, gold, weapon, play_again
    else:
        print("Closing game in: ")
        for x in range(3, 0, -1):
            printDelay(x)
        exit()


def run_or_fight(username: str, user_hp: int, user_gold: int, weapon_type: str, monster: str):
    printDelay(f"""
{username} stats: 
HP: {user_hp}
Gold: {user_gold}
Weapon: {weapon_type}\n""")

    if monster == "goblin":
        monster_hp = 3
    elif monster == "skeleton":
        monster_hp = 5
    elif monster == "dragon":
        monster_hp = 8

    printDelay(f"You encountered a {monster}!")
    printDelay(f"It has {monster_hp} hp")
    printDelay("Do you want to run or fight it?")
    choice = input("fight/run: ").upper()
    while choice != "FIGHT" and choice != "RUN":
        print("Invalid answer...")
        choice = input("fight/run: ").upper()

    if choice == "FIGHT":
        return fight(username, user_hp, user_gold, weapon_type, monster, monster_hp)
    else:
        return run(username, user_gold, weapon_type, False)


def fight(username: str, user_hp: int, user_gold: int, weapon: str, monster: str, monster_hp: int):
    print(f"You decided to fight the {monster}!")
    if weapon == "None":
        printDelay("You died since you dont have a weapon")
        death(username, user_gold, weapon, True)

    if monster == "dragon" and weapon != "Dragon Sword":
        printDelay("You died since you didnt have the Dragon Sword")
        death(username, user_gold, weapon, True)

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
        printDelay(f"""{username} stats:
HP: {user_hp}
Gold: {user_gold}
Weapon: {weapon}""")
    return user_hp, user_gold


def run(username: str, gold: int, weapon: str, play_again: bool):
    printDelay("You decided to run away!")
    random_num = 1
    user_num = int(input("Choose a number between 1-3: "))
    while user_num != 1 and user_num != 2 and user_num != 3:
        print("invalid answer...")
        user_num = int(input("Choose a number between 1-3: "))
    if random_num == user_num:
        print("You successfully ran away!")
        return gold, weapon
    else:
        print("You failed to run away...")
        return death(username, gold, weapon, play_again)


def gold_drops(monster: str):
    if monster == "dragon":
        gold_gained = random.randint(10, 15)
    elif monster == "skeleton":
        gold_gained = random.randint(5, 10)
    elif monster == "goblin":
        gold_gained = random.randint(1, 5)
