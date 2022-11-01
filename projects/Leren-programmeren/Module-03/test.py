class Weapon:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type

steel_sword = Weapon("Steel dagger", 50, "Dagger")

print(steel_sword.__dict__)