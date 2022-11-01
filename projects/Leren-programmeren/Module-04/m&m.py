import random

kleuren = ("oranje ", "blauw ", "groen ", "bruin ")
aantal = int(input("hoeveel m&m's?: "))

mEnM = []
for i in range(aantal):
    random_num = random.randint(0, 3)
    random_color = kleuren[random_num]
    mEnM.append(random_color)

print(mEnM)
