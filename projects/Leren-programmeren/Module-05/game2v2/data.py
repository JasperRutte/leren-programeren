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
no_weapon = "None"
iron_sword = "Iron sword"
dragon_sword = "Dragon Sword"

# other
fight_again = True
play_again = True

PLAYER = Player("", 1, 0, no_weapon)