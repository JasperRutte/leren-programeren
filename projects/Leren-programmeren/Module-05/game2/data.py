class Player:
    def __init__(self, name: str, hp: int, gold: int, weapon: str):
        self.name = name
        self.hp = hp
        self.gold = gold
        self.weapon = weapon

class Monster:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

# weapons
no_sword = "None"
iron_sword = "Iron Sword"
dragon_sword = "Dragon Sword"


# other data
play = True
fight_again = True
